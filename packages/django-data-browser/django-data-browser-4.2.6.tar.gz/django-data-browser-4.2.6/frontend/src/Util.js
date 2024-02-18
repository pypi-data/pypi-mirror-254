import React, { useState, useEffect, useRef, useContext } from "react";
import { Redirect } from "react-router-dom";

import { ShowTooltip, HideTooltip } from "./Tooltip";

import "./App.scss";

const assert = require("assert");
let fetchInProgress = false;
let nextFetch = undefined;

const version = document.getElementById("backend-version").textContent.trim();
const csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;

function CopyText(props) {
    const { text } = props;
    const ref = useRef(null);
    return (
        <>
            <span ref={ref}>{text}</span>{" "}
            <TLink
                className="CopyToClipboard"
                onClick={(event) => {
                    const range = document.createRange();
                    range.selectNodeContents(ref.current);
                    window.getSelection().removeAllRanges();
                    window.getSelection().addRange(range);
                    document.execCommand("copy");
                    window.getSelection().removeAllRanges();
                    event.target.blur();
                }}
            >
                (copy to clipboard)
            </TLink>
        </>
    );
}

function TLink(props) {
    const { className, onClick, children } = props;
    return (
        <button {...{ onClick }} type="button" className={`TLink ${className}`}>
            {children}
        </button>
    );
}

function SLink(props) {
    const { className, onClick, children } = props;
    return (
        <button
            {...{ onClick }}
            type="button"
            className={`SLink material-icons ${className}`}
        >
            {children}
        </button>
    );
}

class AbortError extends Error {
    name = "AbortError";
}

function doFetch(url, options, process) {
    if (fetchInProgress) {
        if (nextFetch) {
            nextFetch.reject(new AbortError("skipped"));
        }
        return new Promise((resolve, reject) => {
            nextFetch = { resolve, reject, url, options, process };
        });
    }

    fetchInProgress = true;

    return fetch(url, options)
        .then((response) => {
            // do we have a next fetch we need to trigger
            const next = nextFetch;
            nextFetch = undefined;
            fetchInProgress = false;

            if (next) {
                doFetch(next.url, next.options, next.process).then(
                    (res) => next.resolve(res),
                    (err) => next.reject(err)
                );
                throw new AbortError("superceeded");
            } else {
                return response;
            }
        })
        .then((response) => {
            // check status
            assert.ok(response.status >= 200);
            assert.ok(response.status < 300);
            return response;
        })
        .then((response) => {
            // check server version
            const response_version = response.headers.get("x-version");
            if (response_version !== version) {
                console.log(
                    "Version mismatch, hard reload",
                    version,
                    response_version
                );
                window.location.reload(true);
            }
            return response;
        })
        .then((response) => process(response)); // process data
}

function doGet(url) {
    return doFetch(url, { method: "GET" }, (response) => response.json());
}

function doDelete(url) {
    return doFetch(
        url,
        {
            method: "DELETE",
            headers: { "X-CSRFToken": csrf_token },
        },
        (response) => response
    );
}

function doPatch(url, data) {
    return doFetch(
        url,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
            body: JSON.stringify(data),
        },
        (response) => response.json()
    );
}

function doPost(url, data) {
    return doFetch(
        url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
            body: JSON.stringify(data),
        },
        (response) => response.json()
    );
}

function syncPost(url, data) {
    const form = document.createElement("form");
    form.method = "post";
    form.action = url;

    data.push(["csrfmiddlewaretoken", csrf_token]);

    for (const [key, value] of data) {
        const hiddenField = document.createElement("input");
        hiddenField.type = "hidden";
        hiddenField.name = key;
        hiddenField.value = value;

        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);
    form.submit();
}

function useData(url) {
    const [data, setData] = useState();
    useEffect(() => {
        doGet(url).then((response) => setData(response));
    }, [url]);
    return [
        data,
        (updates) => {
            setData((prev) => ({ ...prev, ...updates }));
            doPatch(url, updates)
                .then((response) =>
                    setData((prev) => ({ ...prev, ...response }))
                )
                .catch((e) => {
                    if (e.name !== "AbortError") throw e;
                });
        },
    ];
}

function Save(props) {
    const { name, apiUrl, data, redirectUrl } = props;
    const [state, setState] = useState("save");
    if (state === "save")
        return (
            <TLink
                onClick={(event) => {
                    setState("saving");
                    doPost(apiUrl, data).then((response) => setState(response));
                }}
            >
                Save {name || ""}
            </TLink>
        );
    else if (state === "saving") return <>Saving {name || ""}</>;
    else {
        const url =
            typeof redirectUrl === "function"
                ? redirectUrl(state) // state here is the save response
                : redirectUrl;
        return <Redirect to={url} />;
    }
}

const CONFIRM_PROMPT = "Are you sure?";
const CONFIRM_TIMEOUT = 1000;

function Update(props) {
    const { name, apiUrl, data, redirectUrl } = props;
    const [state, setState] = useState("initial");
    var timerID = null;
    if (state === "initial")
        return (
            <TLink
                onClick={(event) => {
                    timerID = setTimeout(
                        () => setState("initial"),
                        CONFIRM_TIMEOUT
                    );
                    setState("confirm");
                }}
            >
                Update {name || ""}
            </TLink>
        );
    else if (state === "confirm")
        return (
            <TLink
                onClick={(event) => {
                    setState("updating");
                    if (timerID) {
                        clearTimeout(timerID);
                        timerID = null;
                    }
                    doPatch(apiUrl, data).then((response) =>
                        setState("updated")
                    );
                }}
            >
                {CONFIRM_PROMPT}
            </TLink>
        );
    else if (state === "updating") return "Updating";
    else if (state === "updated") return <Redirect to={redirectUrl} />;
    else throw new Error(`unknown update state: ${state}`);
}

function Delete(props) {
    const { name, apiUrl, redirectUrl } = props;
    const [state, setState] = useState("initial");
    var timerID = null;
    if (state === "initial")
        return (
            <TLink
                onClick={(event) => {
                    timerID = setTimeout(
                        () => setState("initial"),
                        CONFIRM_TIMEOUT
                    );
                    setState("confirm");
                }}
            >
                Delete {name || ""}
            </TLink>
        );
    else if (state === "confirm")
        return (
            <TLink
                onClick={(event) => {
                    setState("deleting");
                    if (timerID) {
                        clearTimeout(timerID);
                        timerID = null;
                    }
                    doDelete(apiUrl).then((response) => setState("deleted"));
                }}
            >
                {CONFIRM_PROMPT}
            </TLink>
        );
    else if (state === "deleting") return "Deleting";
    else if (state === "deleted") return <Redirect to={redirectUrl} />;
    else throw new Error(`unknown delete state: ${state}`);
}

function Overlay(props) {
    if (!props.message) return null;
    return (
        <div className="Overlay">
            <h1>{props.message}</h1>
        </div>
    );
}

function is(x: any, y: any) {
    return (
        (x === y && (x !== 0 || 1 / x === 1 / y)) || (x !== x && y !== y) // eslint-disable-line no-self-compare
    );
}
const hasOwnProperty = Object.prototype.hasOwnProperty;
function shallowEqual(objA: mixed, objB: mixed): boolean {
    if (is(objA, objB)) {
        return true;
    }

    if (
        typeof objA !== "object" ||
        objA === null ||
        typeof objB !== "object" ||
        objB === null
    ) {
        return false;
    }

    const keysA = Object.keys(objA);
    const keysB = Object.keys(objB);

    if (keysA.length !== keysB.length) {
        console.log("different keys", keysA, keysB);
        return false;
    }

    // Test for A's keys different from B.
    for (let i = 0; i < keysA.length; i++) {
        if (
            !hasOwnProperty.call(objB, keysA[i]) ||
            !is(objA[keysA[i]], objB[keysA[i]])
        ) {
            console.log(
                "different key",
                keysA[i],
                objA[keysA[i]],
                objB[keysA[i]]
            );
            return false;
        }
    }

    return true;
}

function HasActionIcon(props) {
    const { modelField, message } = props;
    const showTooltip = useContext(ShowTooltip);
    const hideTooltip = useContext(HideTooltip);

    if (modelField.actions.length) {
        return (
            <>
                <span> </span>
                <span
                    className="Symbol material-icons-outlined"
                    onMouseEnter={(e) => showTooltip(e, [message])}
                    onMouseLeave={(e) => hideTooltip(e)}
                >
                    build_circle
                </span>
            </>
        );
    } else {
        return "";
    }
}

function HasToManyIcon(props) {
    const { modelField, message } = props;
    const showTooltip = useContext(ShowTooltip);
    const hideTooltip = useContext(HideTooltip);

    if (modelField.toMany) {
        return (
            <>
                <span> </span>
                <span
                    onMouseEnter={(e) => showTooltip(e, [message])}
                    onMouseLeave={(e) => hideTooltip(e)}
                >
                    {"\u21f6"}
                </span>
            </>
        );
    } else {
        return "";
    }
}

function useToggle(initial = false) {
    const [toggled, setToggled] = useState(initial);

    const toggleLink = (
        <SLink
            className="ToggleLink"
            onClick={() => setToggled((toggled) => !toggled)}
        >
            {toggled ? "remove" : "add"}
        </SLink>
    );

    return [toggled, toggleLink];
}

function usePersistentToggle(storageKey = null, initial = false) {
    const blah = localStorage.getItem(storageKey)
        ? localStorage.getItem(storageKey) === "true"
        : initial;

    const [toggled, setToggled] = useState(blah);

    const toggleLink = (
        <SLink
            className="ToggleLink"
            onClick={() =>
                setToggled((toggled) => {
                    localStorage.setItem(storageKey, !toggled);
                    return !toggled;
                })
            }
        >
            {toggled ? "remove" : "add"}
        </SLink>
    );

    return [toggled, toggleLink];
}

export {
    TLink,
    SLink,
    doPatch,
    doGet,
    doDelete,
    doPost,
    useData,
    version,
    Save,
    Update,
    Delete,
    CopyText,
    fetchInProgress,
    Overlay,
    shallowEqual,
    syncPost,
    HasActionIcon,
    HasToManyIcon,
    useToggle,
    usePersistentToggle,
};
