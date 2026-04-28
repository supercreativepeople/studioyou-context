Reactor SDK
> Realtime Video AI SDKs for web and Python applications. Build powerful Realtime Video AI applications in minutes.

Reactor makes working with and using Realtime Video AI a breeze. The platform provides a **JavaScript SDK** (with React components/hooks and an imperative API) and a **Python SDK** (async, decorator-based) for connecting to AI video generation models running on Reactor's cloud infrastructure.

</h2></h2>
- JS Package: <code>@reactor-team/js-sdk</code> — <code>npm install @reactor-team/js-sdk</code>

- Python Package: <code>reactor-sdk</code> — <code>pip install reactor-sdk</code>

- Website: https://reactor.inc

- GitHub: https://github.com/reactor-team/reactor-experiments

- Support: team@reactor.inc

</h2></h2>
| Model Name | Description |

|------------|-------------|

| Helios | Interactive real-time video generation with infinite streaming |

</h2></h2>
A Reactor connection goes through four states:

```
```
DISCONNECTED → CONNECTING → WAITING → READY

```
```
- **disconnected**: No active connection

- **connecting**: Connecting to the Reactor API

- **waiting**: Connected to API, waiting for GPU assignment

- **ready**: Connected to GPU, can send and receive messages

**Important:** You must wait for <code>"ready"</code> status before sending commands.

---

</h2></h2>
</h3></h3>
Exchange the API key for a token by making a <code>POST</code> request to the <code>/tokens</code> endpoint:

```
```
const r = await fetch("https://api.reactor.inc/tokens", {

method: "POST",

headers: { "Reactor-API-Key": process.env.REACTOR_API_KEY! },

});

const { jwt } = await r.json();

```
```
Although the SDK works in any JavaScript environment including the browser, do not store your API key in client-side code. Use your server as a proxy to generate short-lived tokens.

</h3></h3>
</h4></h4>
| Prop | Type | Required | Description |

|------|------|----------|-------------|

| <code>modelName</code> | <code>string</code> | Yes | Model to connect to (e.g., <code>helios</code>) |

| <code>jwtToken</code> | <code>string</code> | No | Token from your backend |

| <code>apiUrl</code> | <code>string</code> | No | API URL (default: <code>https://api.reactor.inc</code>) |

| <code>local</code> | <code>boolean</code> | No | Connect to local runtime at localhost:8080 (default: false) |

| <code>connectOptions</code> | <code>object</code> | No | Connection behavior options (see below) |

**connectOptions:**

| Option | Type | Description |

|--------|------|-------------|

| <code>autoConnect</code> | <code>boolean</code> | Auto-connect on mount (default: **false**) |

| <code>maxAttempts</code> | <code>number</code> | Max SDP polling attempts (default: 6) |

```
```
<ReactorProvider

modelName="helios"

jwtToken={token}

connectOptions={{ autoConnect: true }}

>

```

</h4></h4>
```
Displays the video stream from the model.

| Prop | Type | Description |

|------|------|-------------|

| <code>track</code> | <code>string</code> | Video track to display (default: <code>"main_video"</code>) |

| <code>audioTrack</code> | <code>string</code> | Optional audio track to play alongside the video |

| <code>muted</code> | <code>boolean</code> | Whether the video element is muted (default: <code>true</code>) |

| <code>className</code> | <code>string</code> | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | Inline styles |

| <code>width</code> | <code>number</code> | Width of the video element |

| <code>height</code> | <code>number</code> | Height of the video element |

| <code>videoObjectFit</code> | <code>"contain" \| "cover" \| "fill" \| "none" \| "scale-down"</code> | Video fit mode (default: <code>"contain"</code>) |

</h4></h4>
Captures and auto-publishes webcam video to the model. Handles camera permissions, lifecycle, and auto-publishing/unpublishing.

| Prop | Type | Required | Description |

|------|------|----------|-------------|

| <code>track</code> | <code>string</code> | Yes | Send track name to publish to. Must match a sendonly track declared by the model. |

| <code>className</code> | <code>string</code> | No | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | No | Inline styles |

| <code>videoConstraints</code> | <code>MediaTrackConstraints</code> | No | Webcam constraints (default: 1280x720) |

| <code>showWebcam</code> | <code>boolean</code> | No | Show webcam preview (default: true) |

| <code>videoObjectFit</code> | <code>"contain" \| "cover" \| "fill" \| "none" \| "scale-down"</code> | No | Video fit mode (default: <code>"contain"</code>) |

```
```
import { WebcamStream } from "@reactor-team/js-sdk";

<ReactorProvider modelName="your-model-name" jwtToken={token}>

<WebcamStream

track="webcam"

className="w-full aspect-video"

videoObjectFit="cover"

/>

</ReactorProvider>

```

</h4></h4>
```
Auto-generates UI controls from the model's command schema. Intended for prototyping and debugging.

| Prop | Type | Description |

|------|------|-------------|

| <code>className</code> | <code>string</code> | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | Inline styles |

When the connection reaches <code>"ready"</code>, the component requests the model's capabilities and renders a form for each declared command.

</h4></h4>
```
```
const value = useReactor<T>(selector: (state: ReactorStore) => T): T

```
```
Available store properties:

| Property | Type | Description |

|----------|------|-------------|

| <code>status</code> | <code>ReactorStatus</code> | Current connection status |

| <code>lastError</code> | <code>ReactorError \| undefined</code> | Most recent error |

| <code>tracks</code> | <code>Record<string, MediaStreamTrack></code> | Received tracks by name |

| <code>sessionId</code> | <code>string \| undefined</code> | Current session ID |

| <code>connect</code> | <code>(jwtToken?: string) => Promise<void></code> | Connect to the model |

| <code>disconnect</code> | <code>(recoverable?: boolean) => Promise<void></code> | Disconnect from the model |

| <code>reconnect</code> | <code>(options?: ConnectOptions) => Promise<void></code> | Reconnect to an existing session |

| <code>sendCommand</code> | <code>(command: string, data: object) => Promise<void></code> | Send a command to the model |

| <code>publish</code> | <code>(name: string, track: MediaStreamTrack) => Promise<void></code> | Publish a named track |

| <code>unpublish</code> | <code>(name: string) => Promise<void></code> | Stop publishing a named track |

Best practice — select multiple related values as object:

```
```
const { status, connect, disconnect, sendCommand } = useReactor((state) => ({

status: state.status,

connect: state.connect,

disconnect: state.disconnect,

sendCommand: state.sendCommand,

}));

```

</h4></h4>
```
```typescript

useReactorMessage((message: any) => {

if (message.type === "state") {

console.log("Current frame:", message.data.current_frame);

}

});

```
```
Only receives `application`-scoped messages. Internal platform messages are handled by the SDK.

</h4></h4>
Returns live WebRTC connection statistics, updated every 2 seconds while connected.

```
```
const stats = useStats(); // ConnectionStats | undefined, updates every 2s

```

</h3></h3>
```
```typescript

import { Reactor } from "@reactor-team/js-sdk";

const reactor = new Reactor({

modelName: "helios",

});

reactor.on("trackReceived", (name, track, stream) => {

document.getElementById("video").srcObject = stream;

});

await reactor.connect(token);

await reactor.sendCommand("start", {});

```

</h4></h4>
```
| Option | Type | Required | Description |

|--------|------|----------|-------------|

| <code>modelName</code> | <code>string</code> | Yes | Model to connect to |

| <code>apiUrl</code> | <code>string</code> | No | API URL (default: <code>https://api.reactor.inc</code>) |

</h4></h4>
| Method | Signature | Description |

|--------|-----------|-------------|

| <code>connect()</code> | <code>(jwtToken?: string, options?: ConnectOptions) => Promise<void></code> | Connect to API and GPU |

| <code>disconnect()</code> | <code>(recoverable?: boolean) => Promise<void></code> | Disconnect (recoverable keeps session alive) |

| <code>reconnect()</code> | <code>(options?: ConnectOptions) => Promise<void></code> | Reconnect to an existing session |

| <code>sendCommand()</code> | <code>(command: string, data: any) => Promise<void></code> | Send command to the model |

| <code>publishTrack()</code> | <code>(name: string, track: MediaStreamTrack) => Promise<void></code> | Publish a named track to model |

| <code>unpublishTrack()</code> | <code>(name: string) => Promise<void></code> | Stop publishing a named track |

| <code>getStatus()</code> | <code>() => ReactorStatus</code> | Get current status |

| <code>getState()</code> | <code>() => ReactorState</code> | Get full state with error info |

| <code>getSessionId()</code> | <code>() => string \| undefined</code> | Get current session ID |

| <code>getLastError()</code> | <code>() => ReactorError \| undefined</code> | Get most recent error |

| <code>getCapabilities()</code> | <code>() => Capabilities \| undefined</code> | Get model capabilities (tracks, commands) |

| <code>getSessionInfo()</code> | <code>() => SessionInfo \| undefined</code> | Get full session response |

| <code>getStats()</code> | <code>() => ConnectionStats \| undefined</code> | Get WebRTC connection stats |

| <code>on()</code> | <code>(event: ReactorEvent, handler) => void</code> | Register event listener |

| <code>off()</code> | <code>(event: ReactorEvent, handler) => void</code> | Remove event listener |

</h4></h4>
| Event | Payload | Description |

|-------|---------|-------------|

| <code>statusChanged</code> | <code>ReactorStatus</code> | Connection status changed |

| <code>message</code> | <code>any</code> | Application message from model |

| <code>runtimeMessage</code> | <code>any</code> | Internal platform message (used by ReactorController) |

| <code>trackReceived</code> | <code>(name: string, track: MediaStreamTrack, stream: MediaStream)</code> | Named media track received from model |

| <code>error</code> | <code>ReactorError</code> | Error occurred |

| <code>sessionIdChanged</code> | <code>string \| undefined</code> | Session ID changed |

| <code>sessionExpirationChanged</code> | <code>number \| undefined</code> | Session expiration (Unix timestamp) |

| <code>capabilitiesReceived</code> | <code>Capabilities</code> | Model capabilities received |

| <code>statsUpdate</code> | <code>ConnectionStats</code> | WebRTC stats updated (every 2s while connected) |

</h3></h3>
```
```
type ReactorStatus = "disconnected" | "connecting" | "waiting" | "ready";

interface ReactorError {

code: string;                              // e.g., "AUTHENTICATION_FAILED"

message: string;                           // Human-readable message

timestamp: number;                         // Unix timestamp

recoverable: boolean;                      // Whether auto-recovery is possible

component: "api" | "gpu";                  // Source component

retryAfter?: number;                       // Suggested retry delay (seconds)

}

interface ReactorState {

status: ReactorStatus;

lastError?: ReactorError;

}

interface ConnectOptions {

maxAttempts?: number;  // Max SDP polling attempts (default: 6)

}

interface TrackCapability {

name: string;

kind: "video" | "audio";

direction: "recvonly" | "sendonly";

}

interface Capabilities {

protocol_version: string;

tracks: TrackCapability[];

commands?: CommandCapability[];

emission_fps?: number | null;

}

interface ConnectionStats {

timestamp: number;                    // When stats were collected (Unix ms)

rtt?: number;                         // Round-trip time in milliseconds

framesPerSecond?: number;             // Received video frames per second

jitter?: number;                      // Network jitter in seconds

packetLossRatio?: number;             // Packet loss ratio (0 to 1)

candidateType?: string;               // ICE candidate type

availableOutgoingBitrate?: number;    // Available outgoing bitrate in bits/second

connectionTimings?: ConnectionTimings; // Connection timing breakdown

}

// Thrown when model is already in use by another session

class ConflictError extends Error {}

```
```
Common error codes: `CONNECTION_FAILED`, `GPU_CONNECTION_ERROR`, `MESSAGE_SEND_FAILED`, `TRACK_PUBLISH_FAILED`, `RECONNECTION_FAILED`

</h3></h3>
```
```
// Imperative API

reactor.on("error", async (error) => {

console.error(<code>[${error.component}] ${error.code}: ${error.message}</code>);

if (error.recoverable) {

const delay = error.retryAfter || 3;

await new Promise(r => setTimeout(r, delay * 1000));

await reactor.reconnect();

}

});

// React API

function ErrorDisplay() {

const lastError = useReactor((state) => state.lastError);

if (!lastError) return null;

return <div>{lastError.code}: {lastError.message}</div>;

}

```

</h3></h3>
```
```typescript

import { useState, useEffect } from "react";

import {

ReactorProvider,

ReactorView,

useReactor,

useReactorMessage,

} from "@reactor-team/js-sdk";

function VideoPlayer() {

const { status, connect, sendCommand } = useReactor((s) => ({

status: s.status,

connect: s.connect,

sendCommand: s.sendCommand,

}));

const start = async () => {

await sendCommand("schedule_prompt", { prompt: "A sunset", chunk: 0 });

await sendCommand("start", {});

};

useReactorMessage((message) => {

if (message.type === "state") {

console.log("Frame:", message.data.current_frame);

}

});

return (

<div>

<ReactorView className="w-full aspect-video" videoObjectFit="cover" />

<p>Status: {status}</p>

<button onClick={connect} disabled={status !== "disconnected"}>Connect</button>

<button onClick={start} disabled={status !== "ready"}>Start</button>

</div>

);

}

export default function App() {

const [token, setToken] = useState<string | null>(null);

useEffect(() => {

async function fetchToken() {

const r = await fetch("/api/token", { method: "POST" });

const { jwt } = await r.json();

setToken(jwt);

}

fetchToken().catch(console.error);

}, []);

if (!token) return <div>Authenticating...</div>;

return (

<ReactorProvider

modelName="helios"

jwtToken={token}

connectOptions={{ autoConnect: false }}

>

<VideoPlayer />

</ReactorProvider>

);

}

```
```
---

</h2></h2>
</h3></h3>
Pass your API key directly to the constructor — the SDK handles token exchange automatically during <code>connect()</code>:

```
```
from reactor_sdk import Reactor

reactor = Reactor(model_name="helios", api_key="rk_your_api_key")

await reactor.connect()

```

</h3></h3>
```
```python

Reactor(

model_name: str,

api_key: str | None = None,

api_url: str = "https://api.reactor.inc",

local: bool = False,

)

```
```
| Parameter | Type | Required | Description |

|-----------|------|----------|-------------|

| <code>model_name</code> | <code>str</code> | Yes | Model to connect to |

| <code>api_key</code> | <code>str</code> | No | API key (auto-fetches token). Required unless <code>local=True</code> |

| <code>api_url</code> | <code>str</code> | No | API URL (default: <code>https://api.reactor.inc</code>). Ignored if <code>local=True</code> |

| <code>local</code> | <code>bool</code> | No | Connect to local runtime at localhost:8080 (default: False) |

</h3></h3>
| Method | Signature | Description |

|--------|-----------|-------------|

| <code>connect()</code> | <code>await reactor.connect() -> None</code> | Connect to API and wait for GPU |

| <code>disconnect()</code> | <code>await reactor.disconnect(recoverable: bool = False) -> None</code> | Disconnect (recoverable keeps session alive) |

| <code>reconnect()</code> | <code>await reactor.reconnect() -> None</code> | Reconnect to an existing session |

| <code>send_command()</code> | <code>await reactor.send_command(command: str, data: Any) -> None</code> | Send a command to the model |

| <code>get_status()</code> | <code>reactor.get_status() -> ReactorStatus</code> | Get current connection status |

| <code>get_state()</code> | <code>reactor.get_state() -> ReactorState</code> | Get full connection state |

| <code>get_session_id()</code> | <code>reactor.get_session_id() -> str \| None</code> | Get current session ID |

| <code>get_last_error()</code> | <code>reactor.get_last_error() -> ReactorError \| None</code> | Get most recent error |

| <code>get_capabilities()</code> | <code>reactor.get_capabilities() -> Capabilities \| None</code> | Get model capabilities (tracks, commands) |

| <code>get_session_info()</code> | <code>reactor.get_session_info() -> CreateSessionResponse \| None</code> | Get full session response |

| <code>get_remote_tracks()</code> | <code>reactor.get_remote_tracks() -> dict[str, MediaStreamTrack]</code> | Get received tracks by name |

| <code>publish_track()</code> | <code>await reactor.publish_track(name: str, track: MediaStreamTrack) -> None</code> | Publish a named track to the model |

| <code>unpublish_track()</code> | <code>await reactor.unpublish_track(name: str) -> None</code> | Stop publishing a named track |

| <code>set_frame_callback()</code> | <code>reactor.set_frame_callback(callback: FrameCallback \| None) -> None</code> | Set/clear frame receive callback |

| <code>on()</code> | <code>reactor.on(event: ReactorEvent, callback) -> None</code> | Register an event handler |

| <code>off()</code> | <code>reactor.off(event: ReactorEvent, callback) -> None</code> | Remove an event handler |

</h3></h3>
```
```
async with Reactor(model_name="helios", api_key=api_key) as reactor:

await reactor.send_command("start", {})

# Automatically disconnects on exit

```

</h3></h3>
```
```python

@reactor.on_frame

def handle_frame(frame):

"""Receive video frames as NumPy arrays (H, W, 3) RGB uint8"""

print(f"Frame shape: {frame.shape}")

@reactor.on_message

def handle_message(message):

"""Receive application messages from the model"""

print(f"Message: {message}")

@reactor.on_internal_message

def handle_internal(message):

"""Receive internal platform messages (rarely needed)"""

pass

@reactor.on_status(ReactorStatus.READY)

def on_ready(status):

"""React to specific status changes"""

print("Connected to GPU!")

@reactor.on_error

def handle_error(error):

"""Handle errors"""

print(f"Error: {error}")

@reactor.on_track("video")

def handle_track(track):

"""Access a named raw WebRTC MediaStreamTrack"""

print(f"Received track: {track.kind}")

```

</h3></h3>
```
| Event | Payload | Description |

|-------|---------|-------------|

| <code>"status_changed"</code> | <code>ReactorStatus</code> | Connection status changed |

| <code>"session_id_changed"</code> | <code>str \| None</code> | Session ID changed |

| <code>"message"</code> | <code>Any</code> | Application message from the model |

| <code>"runtime_message"</code> | <code>Any</code> | Internal platform message |

| <code>"track_received"</code> | <code>(name: str, track: MediaStreamTrack)</code> | Named track received |

| <code>"error"</code> | <code>ReactorError</code> | Error occurred |

| <code>"session_expiration_changed"</code> | <code>float \| None</code> | Session expiration time updated |

| <code>"capabilities_received"</code> | <code>Capabilities</code> | Model capabilities received |

Note: Python events use <code>snake_case</code> (e.g., <code>"status_changed"</code>) while JavaScript uses <code>camelCase</code> (e.g., <code>"statusChanged"</code>).

</h3></h3>
| Type | Kind | Values / Fields |

|------|------|-----------------|

| <code>ReactorStatus</code> | Enum | <code>DISCONNECTED</code>, <code>CONNECTING</code>, <code>WAITING</code>, <code>READY</code> |

| <code>ReactorState</code> | Dataclass | <code>status: ReactorStatus</code>, <code>last_error: ReactorError \| None</code> |

| <code>ReactorError</code> | Dataclass | <code>code: str</code>, <code>message: str</code>, <code>timestamp: float</code>, <code>recoverable: bool</code>, <code>component: Literal["api", "gpu"]</code>, <code>retry_after: float \| None</code> |

| <code>ReactorEvent</code> | Literal | <code>"status_changed"</code>, <code>"session_id_changed"</code>, <code>"message"</code>, <code>"runtime_message"</code>, <code>"track_received"</code>, <code>"error"</code>, <code>"session_expiration_changed"</code>, <code>"capabilities_received"</code> |

| <code>FrameCallback</code> | Type alias | <code>Callable[[NDArray[np.uint8]], None]</code> — receives RGB frame <code>(H, W, 3)</code> |

| <code>TrackCapability</code> | TypedDict | <code>name: str</code>, <code>kind: TrackKind</code>, <code>direction: TrackDirection</code> |

| <code>Capabilities</code> | TypedDict | <code>protocol_version: str</code>, <code>tracks: list[TrackCapability]</code>, <code>commands?: list[CommandCapability]</code>, <code>emission_fps?: float</code> |

| <code>ConflictError</code> | Exception | Raised when a connection conflict occurs |

| <code>VersionMismatchError</code> | Exception | Raised on 426/501 version negotiation failures |

Common error codes: <code>CONNECTION_FAILED</code>, <code>GPU_CONNECTION_ERROR</code>, <code>RECONNECTION_FAILED</code>

</h3></h3>
```
```
import asyncio

import os

from reactor_sdk import Reactor, ReactorStatus

async def main():

api_key = os.environ["REACTOR_API_KEY"]

async with Reactor(model_name="helios", api_key=api_key) as reactor:

@reactor.on_frame

def on_frame(frame):

print(f"Frame: {frame.shape}")

@reactor.on_status(ReactorStatus.READY)

def on_ready(status):

print("Connected! Sending commands...")

@reactor.on_message

def on_message(message):

print(f"Model says: {message}")

await reactor.connect()

await reactor.send_command("schedule_prompt", {

"prompt": "A sunset over the ocean",

"chunk": 0,

})

await reactor.send_command("start", {})

# Keep running

while reactor.get_status() != ReactorStatus.DISCONNECTED:

await asyncio.sleep(1)

asyncio.run(main())

```
```
---

</h2></h2>
Helios is an interactive, real-time video generation model with infinite streaming. Built on a 14B-parameter Diffusion Transformer, it generates video in 33-frame chunks. It supports text-to-video and image-to-video modes.

Model name: <code>helios</code>

| Command | Parameters | Description |

|---------|------------|-------------|

| <code>set_prompt</code> | <code>prompt: string</code> | Set the prompt (at chunk 0 if not started, current chunk if paused, next chunk if running) |

| <code>schedule_prompt</code> | <code>prompt: string</code>, <code>chunk: integer</code> | Schedule a prompt at a specific chunk index |

| <code>set_image</code> | <code>image_b64: string</code>, <code>transition?: "cut" \| "blend"</code> | Set a base64-encoded reference image (works before or during generation). Transition default: <code>"cut"</code>. |

| <code>clear_image</code> | none | Remove the reference image, continue with text-only conditioning |

| <code>set_seed</code> | <code>seed: integer</code> | Set the RNG seed for reproducible generation |

| <code>start</code> | none | Start generation (requires prompt at chunk 0) |

| <code>pause</code> | none | Pause generation after current chunk finishes |

| <code>resume</code> | none | Resume generation |

| <code>reset</code> | none | Reset to initial state, clears all prompts and history |

**Prompt scheduling rules:**

- Must schedule at least one prompt at chunk 0 before calling <code>start</code>

- Scheduling at an existing chunk overwrites the previous prompt

- Prompts scheduled at past chunks are rejected

- Prompts can be scheduled while generation is running

**Helios State Messages** (<code>type: "state"</code>):

```
```
{

"type": "state",

"data": {

"running": true,

"current_frame": 42,

"current_chunk": 2,

"current_prompt": "A serene mountain landscape",

"paused": false,

"scheduled_prompts": { "0": "A serene mountain landscape" }

}

}

```
```
**Helios Event Messages** (`type: "event"`):

- <code>generation_started</code> (with <code>prompt</code>)

- <code>generation_paused</code> (with <code>frame</code>, <code>chunk</code>)

- <code>generation_resumed</code> (with <code>frame</code>, <code>chunk</code>)

- <code>generation_reset</code> (with <code>frame</code>, <code>chunk</code>)

- <code>image_set</code> (with <code>width</code>, <code>height</code>, <code>transition</code>)

- <code>image_cleared</code>

- <code>seed_set</code> (with <code>seed</code>)

- <code>prompt_scheduled</code> (with <code>chunk</code>, <code>prompt</code>)

- <code>prompt_switched</code> (with <code>frame</code>, <code>chunk</code>, <code>new_prompt</code>, <code>previous_prompt</code>)

- <code>error</code> (with <code>message</code>)

</h3></h3>
```
```
const reactor = new Reactor({ modelName: "helios" });

await reactor.connect(token);

await reactor.sendCommand("set_seed", { seed: 42 });

await reactor.sendCommand("schedule_prompt", {

prompt: "A peaceful forest at dawn",

chunk: 0

});

await reactor.sendCommand("schedule_prompt", {

prompt: "A deer walking through the misty forest",

chunk: 10

});

await reactor.sendCommand("start", {});

```
```
---

</h2></h2>
- <code>/overview</code> — Introduction and example usage

- <code>/quickstart</code> — Getting started guide with CLI and manual setup

- <code>/authentication</code> — Authentication (JavaScript and Python)

- <code>/models/overview</code> — Available models index

- <code>/models/helios</code> — Helios model reference (autoregressive chunked video generation)

- <code>/javascript-guide</code> — JavaScript SDK usage patterns and best practices

- <code>/python-guide</code> — Python SDK usage patterns and best practices

- <code>/concepts/sessions</code> — Sessions, connection lifecycle, and reconnection

- <code>/concepts/commands-and-messages</code> — Commands and messages

- <code>/api-reference/overview</code> — API reference introduction (both SDKs)

- <code>/api-reference/reactor-class</code> — JavaScript Reactor class API

- <code>/api-reference/react-components</code> — ReactorProvider, ReactorView, WebcamStream, ReactorController

- <code>/api-reference/react-hooks</code> — useReactor, useReactorMessage, useStats

- <code>/api-reference/types</code> — JavaScript TypeScript type definitions

- <code>/api-reference/events</code> — JavaScript event types and handlers

- <code>/api-reference/python/reactor</code> — Python Reactor class API

- <code>/api-reference/python/decorators</code> — Python decorator-based event handlers

- <code>/api-reference/python/types</code> — Python types, enums, and utilities

Reactor SDK
> Realtime Video AI SDKs for web and Python applications. Build powerful Realtime Video AI applications in minutes.

Reactor makes working with and using Realtime Video AI a breeze. The platform provides a **JavaScript SDK** (with React components/hooks and an imperative API) and a **Python SDK** (async, decorator-based) for connecting to AI video generation models running on Reactor's cloud infrastructure.

</h2></h2>
- JS Package: <code>@reactor-team/js-sdk</code> — <code>npm install @reactor-team/js-sdk</code>

- Python Package: <code>reactor-sdk</code> — <code>pip install reactor-sdk</code>

- Website: https://reactor.inc

- GitHub: https://github.com/reactor-team/reactor-experiments

- Support: team@reactor.inc

</h2></h2>
| Model Name | Description |

|------------|-------------|

| Helios | Interactive real-time video generation with infinite streaming |

</h2></h2>
A Reactor connection goes through four states:

```
```
DISCONNECTED → CONNECTING → WAITING → READY

```
```
- **disconnected**: No active connection

- **connecting**: Connecting to the Reactor API

- **waiting**: Connected to API, waiting for GPU assignment

- **ready**: Connected to GPU, can send and receive messages

**Important:** You must wait for <code>"ready"</code> status before sending commands.

---

</h2></h2>
</h3></h3>
Exchange the API key for a token by making a <code>POST</code> request to the <code>/tokens</code> endpoint:

```
```
const r = await fetch("https://api.reactor.inc/tokens", {

method: "POST",

headers: { "Reactor-API-Key": process.env.REACTOR_API_KEY! },

});

const { jwt } = await r.json();

```
```
Although the SDK works in any JavaScript environment including the browser, do not store your API key in client-side code. Use your server as a proxy to generate short-lived tokens.

</h3></h3>
</h4></h4>
| Prop | Type | Required | Description |

|------|------|----------|-------------|

| <code>modelName</code> | <code>string</code> | Yes | Model to connect to (e.g., <code>helios</code>) |

| <code>jwtToken</code> | <code>string</code> | No | Token from your backend |

| <code>apiUrl</code> | <code>string</code> | No | API URL (default: <code>https://api.reactor.inc</code>) |

| <code>local</code> | <code>boolean</code> | No | Connect to local runtime at localhost:8080 (default: false) |

| <code>connectOptions</code> | <code>object</code> | No | Connection behavior options (see below) |

**connectOptions:**

| Option | Type | Description |

|--------|------|-------------|

| <code>autoConnect</code> | <code>boolean</code> | Auto-connect on mount (default: **false**) |

| <code>maxAttempts</code> | <code>number</code> | Max SDP polling attempts (default: 6) |

```
```
<ReactorProvider

modelName="helios"

jwtToken={token}

connectOptions={{ autoConnect: true }}

>

```

</h4></h4>
```
Displays the video stream from the model.

| Prop | Type | Description |

|------|------|-------------|

| <code>track</code> | <code>string</code> | Video track to display (default: <code>"main_video"</code>) |

| <code>audioTrack</code> | <code>string</code> | Optional audio track to play alongside the video |

| <code>muted</code> | <code>boolean</code> | Whether the video element is muted (default: <code>true</code>) |

| <code>className</code> | <code>string</code> | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | Inline styles |

| <code>width</code> | <code>number</code> | Width of the video element |

| <code>height</code> | <code>number</code> | Height of the video element |

| <code>videoObjectFit</code> | <code>"contain" \| "cover" \| "fill" \| "none" \| "scale-down"</code> | Video fit mode (default: <code>"contain"</code>) |

</h4></h4>
Captures and auto-publishes webcam video to the model. Handles camera permissions, lifecycle, and auto-publishing/unpublishing.

| Prop | Type | Required | Description |

|------|------|----------|-------------|

| <code>track</code> | <code>string</code> | Yes | Send track name to publish to. Must match a sendonly track declared by the model. |

| <code>className</code> | <code>string</code> | No | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | No | Inline styles |

| <code>videoConstraints</code> | <code>MediaTrackConstraints</code> | No | Webcam constraints (default: 1280x720) |

| <code>showWebcam</code> | <code>boolean</code> | No | Show webcam preview (default: true) |

| <code>videoObjectFit</code> | <code>"contain" \| "cover" \| "fill" \| "none" \| "scale-down"</code> | No | Video fit mode (default: <code>"contain"</code>) |

```
```
import { WebcamStream } from "@reactor-team/js-sdk";

<ReactorProvider modelName="your-model-name" jwtToken={token}>

<WebcamStream

track="webcam"

className="w-full aspect-video"

videoObjectFit="cover"

/>

</ReactorProvider>

```

</h4></h4>
```
Auto-generates UI controls from the model's command schema. Intended for prototyping and debugging.

| Prop | Type | Description |

|------|------|-------------|

| <code>className</code> | <code>string</code> | CSS class name |

| <code>style</code> | <code>CSSProperties</code> | Inline styles |

When the connection reaches <code>"ready"</code>, the component requests the model's capabilities and renders a form for each declared command.

</h4></h4>
```
```
const value = useReactor<T>(selector: (state: ReactorStore) => T): T

```
```
Available store properties:

| Property | Type | Description |

|----------|------|-------------|

| <code>status</code> | <code>ReactorStatus</code> | Current connection status |

| <code>lastError</code> | <code>ReactorError \| undefined</code> | Most recent error |

| <code>tracks</code> | <code>Record<string, MediaStreamTrack></code> | Received tracks by name |

| <code>sessionId</code> | <code>string \| undefined</code> | Current session ID |

| <code>connect</code> | <code>(jwtToken?: string) => Promise<void></code> | Connect to the model |

| <code>disconnect</code> | <code>(recoverable?: boolean) => Promise<void></code> | Disconnect from the model |

| <code>reconnect</code> | <code>(options?: ConnectOptions) => Promise<void></code> | Reconnect to an existing session |

| <code>sendCommand</code> | <code>(command: string, data: object) => Promise<void></code> | Send a command to the model |

| <code>publish</code> | <code>(name: string, track: MediaStreamTrack) => Promise<void></code> | Publish a named track |

| <code>unpublish</code> | <code>(name: string) => Promise<void></code> | Stop publishing a named track |

Best practice — select multiple related values as object:

```
```
const { status, connect, disconnect, sendCommand } = useReactor((state) => ({

status: state.status,

connect: state.connect,

disconnect: state.disconnect,

sendCommand: state.sendCommand,

}));

```

</h4></h4>
```
```typescript

useReactorMessage((message: any) => {

if (message.type === "state") {

console.log("Current frame:", message.data.current_frame);

}

});

```
```
Only receives `application`-scoped messages. Internal platform messages are handled by the SDK.

</h4></h4>
Returns live WebRTC connection statistics, updated every 2 seconds while connected.

```
```
const stats = useStats(); // ConnectionStats | undefined, updates every 2s

```

</h3></h3>
```
```typescript

import { Reactor } from "@reactor-team/js-sdk";

const reactor = new Reactor({

modelName: "helios",

});

reactor.on("trackReceived", (name, track, stream) => {

document.getElementById("video").srcObject = stream;

});

await reactor.connect(token);

await reactor.sendCommand("start", {});

```

</h4></h4>
```
| Option | Type | Required | Description |

|--------|------|----------|-------------|

| <code>modelName</code> | <code>string</code> | Yes | Model to connect to |

| <code>apiUrl</code> | <code>string</code> | No | API URL (default: <code>https://api.reactor.inc</code>) |

</h4></h4>
| Method | Signature | Description |

|--------|-----------|-------------|

| <code>connect()</code> | <code>(jwtToken?: string, options?: ConnectOptions) => Promise<void></code> | Connect to API and GPU |

| <code>disconnect()</code> | <code>(recoverable?: boolean) => Promise<void></code> | Disconnect (recoverable keeps session alive) |

| <code>reconnect()</code> | <code>(options?: ConnectOptions) => Promise<void></code> | Reconnect to an existing session |

| <code>sendCommand()</code> | <code>(command: string, data: any) => Promise<void></code> | Send command to the model |

| <code>publishTrack()</code> | <code>(name: string, track: MediaStreamTrack) => Promise<void></code> | Publish a named track to model |

| <code>unpublishTrack()</code> | <code>(name: string) => Promise<void></code> | Stop publishing a named track |

| <code>getStatus()</code> | <code>() => ReactorStatus</code> | Get current status |

| <code>getState()</code> | <code>() => ReactorState</code> | Get full state with error info |

| <code>getSessionId()</code> | <code>() => string \| undefined</code> | Get current session ID |

| <code>getLastError()</code> | <code>() => ReactorError \| undefined</code> | Get most recent error |

| <code>getCapabilities()</code> | <code>() => Capabilities \| undefined</code> | Get model capabilities (tracks, commands) |

| <code>getSessionInfo()</code> | <code>() => SessionInfo \| undefined</code> | Get full session response |

| <code>getStats()</code> | <code>() => ConnectionStats \| undefined</code> | Get WebRTC connection stats |

| <code>on()</code> | <code>(event: ReactorEvent, handler) => void</code> | Register event listener |

| <code>off()</code> | <code>(event: ReactorEvent, handler) => void</code> | Remove event listener |

</h4></h4>
| Event | Payload | Description |

|-------|---------|-------------|

| <code>statusChanged</code> | <code>ReactorStatus</code> | Connection status changed |

| <code>message</code> | <code>any</code> | Application message from model |

| <code>runtimeMessage</code> | <code>any</code> | Internal platform message (used by ReactorController) |

| <code>trackReceived</code> | <code>(name: string, track: MediaStreamTrack, stream: MediaStream)</code> | Named media track received from model |

| <code>error</code> | <code>ReactorError</code> | Error occurred |

| <code>sessionIdChanged</code> | <code>string \| undefined</code> | Session ID changed |

| <code>sessionExpirationChanged</code> | <code>number \| undefined</code> | Session expiration (Unix timestamp) |

| <code>capabilitiesReceived</code> | <code>Capabilities</code> | Model capabilities received |

| <code>statsUpdate</code> | <code>ConnectionStats</code> | WebRTC stats updated (every 2s while connected) |

</h3></h3>
```
```
type ReactorStatus = "disconnected" | "connecting" | "waiting" | "ready";

interface ReactorError {

code: string;                              // e.g., "AUTHENTICATION_FAILED"

message: string;                           // Human-readable message

timestamp: number;                         // Unix timestamp

recoverable: boolean;                      // Whether auto-recovery is possible

component: "api" | "gpu";                  // Source component

retryAfter?: number;                       // Suggested retry delay (seconds)

}

interface ReactorState {

status: ReactorStatus;

lastError?: ReactorError;

}

interface ConnectOptions {

maxAttempts?: number;  // Max SDP polling attempts (default: 6)

}

interface TrackCapability {

name: string;

kind: "video" | "audio";

direction: "recvonly" | "sendonly";

}

interface Capabilities {

protocol_version: string;

tracks: TrackCapability[];

commands?: CommandCapability[];

emission_fps?: number | null;

}

interface ConnectionStats {

timestamp: number;                    // When stats were collected (Unix ms)

rtt?: number;                         // Round-trip time in milliseconds

framesPerSecond?: number;             // Received video frames per second

jitter?: number;                      // Network jitter in seconds

packetLossRatio?: number;             // Packet loss ratio (0 to 1)

candidateType?: string;               // ICE candidate type

availableOutgoingBitrate?: number;    // Available outgoing bitrate in bits/second

connectionTimings?: ConnectionTimings; // Connection timing breakdown

}

// Thrown when model is already in use by another session

class ConflictError extends Error {}

```
```
Common error codes: `CONNECTION_FAILED`, `GPU_CONNECTION_ERROR`, `MESSAGE_SEND_FAILED`, `TRACK_PUBLISH_FAILED`, `RECONNECTION_FAILED`

</h3></h3>
```
```
// Imperative API

reactor.on("error", async (error) => {

console.error(<code>[${error.component}] ${error.code}: ${error.message}</code>);

if (error.recoverable) {

const delay = error.retryAfter || 3;

await new Promise(r => setTimeout(r, delay * 1000));

await reactor.reconnect();

}

});

// React API

function ErrorDisplay() {

const lastError = useReactor((state) => state.lastError);

if (!lastError) return null;

return <div>{lastError.code}: {lastError.message}</div>;

}

```

</h3></h3>
```
```typescript

import { useState, useEffect } from "react";

import {

ReactorProvider,

ReactorView,

useReactor,

useReactorMessage,

} from "@reactor-team/js-sdk";

function VideoPlayer() {

const { status, connect, sendCommand } = useReactor((s) => ({

status: s.status,

connect: s.connect,

sendCommand: s.sendCommand,

}));

const start = async () => {

await sendCommand("schedule_prompt", { prompt: "A sunset", chunk: 0 });

await sendCommand("start", {});

};

useReactorMessage((message) => {

if (message.type === "state") {

console.log("Frame:", message.data.current_frame);

}

});

return (

<div>

<ReactorView className="w-full aspect-video" videoObjectFit="cover" />

<p>Status: {status}</p>

<button onClick={connect} disabled={status !== "disconnected"}>Connect</button>

<button onClick={start} disabled={status !== "ready"}>Start</button>

</div>

);

}

export default function App() {

const [token, setToken] = useState<string | null>(null);

useEffect(() => {

async function fetchToken() {

const r = await fetch("/api/token", { method: "POST" });

const { jwt } = await r.json();

setToken(jwt);

}

fetchToken().catch(console.error);

}, []);

if (!token) return <div>Authenticating...</div>;

return (

<ReactorProvider

modelName="helios"

jwtToken={token}

connectOptions={{ autoConnect: false }}

>

<VideoPlayer />

</ReactorProvider>

);

}

```
```
---

</h2></h2>
</h3></h3>
Pass your API key directly to the constructor — the SDK handles token exchange automatically during <code>connect()</code>:

```
```
from reactor_sdk import Reactor

reactor = Reactor(model_name="helios", api_key="rk_your_api_key")

await reactor.connect()

```

</h3></h3>
```
```python

Reactor(

model_name: str,

api_key: str | None = None,

api_url: str = "https://api.reactor.inc",

local: bool = False,

)

```
```
| Parameter | Type | Required | Description |

|-----------|------|----------|-------------|

| <code>model_name</code> | <code>str</code> | Yes | Model to connect to |

| <code>api_key</code> | <code>str</code> | No | API key (auto-fetches token). Required unless <code>local=True</code> |

| <code>api_url</code> | <code>str</code> | No | API URL (default: <code>https://api.reactor.inc</code>). Ignored if <code>local=True</code> |

| <code>local</code> | <code>bool</code> | No | Connect to local runtime at localhost:8080 (default: False) |

</h3></h3>
| Method | Signature | Description |

|--------|-----------|-------------|

| <code>connect()</code> | <code>await reactor.connect() -> None</code> | Connect to API and wait for GPU |

| <code>disconnect()</code> | <code>await reactor.disconnect(recoverable: bool = False) -> None</code> | Disconnect (recoverable keeps session alive) |

| <code>reconnect()</code> | <code>await reactor.reconnect() -> None</code> | Reconnect to an existing session |

| <code>send_command()</code> | <code>await reactor.send_command(command: str, data: Any) -> None</code> | Send a command to the model |

| <code>get_status()</code> | <code>reactor.get_status() -> ReactorStatus</code> | Get current connection status |

| <code>get_state()</code> | <code>reactor.get_state() -> ReactorState</code> | Get full connection state |

| <code>get_session_id()</code> | <code>reactor.get_session_id() -> str \| None</code> | Get current session ID |

| <code>get_last_error()</code> | <code>reactor.get_last_error() -> ReactorError \| None</code> | Get most recent error |

| <code>get_capabilities()</code> | <code>reactor.get_capabilities() -> Capabilities \| None</code> | Get model capabilities (tracks, commands) |

| <code>get_session_info()</code> | <code>reactor.get_session_info() -> CreateSessionResponse \| None</code> | Get full session response |

| <code>get_remote_tracks()</code> | <code>reactor.get_remote_tracks() -> dict[str, MediaStreamTrack]</code> | Get received tracks by name |

| <code>publish_track()</code> | <code>await reactor.publish_track(name: str, track: MediaStreamTrack) -> None</code> | Publish a named track to the model |

| <code>unpublish_track()</code> | <code>await reactor.unpublish_track(name: str) -> None</code> | Stop publishing a named track |

| <code>set_frame_callback()</code> | <code>reactor.set_frame_callback(callback: FrameCallback \| None) -> None</code> | Set/clear frame receive callback |

| <code>on()</code> | <code>reactor.on(event: ReactorEvent, callback) -> None</code> | Register an event handler |

| <code>off()</code> | <code>reactor.off(event: ReactorEvent, callback) -> None</code> | Remove an event handler |

</h3></h3>
```
```
async with Reactor(model_name="helios", api_key=api_key) as reactor:

await reactor.send_command("start", {})

# Automatically disconnects on exit

```

</h3></h3>
```
```python

@reactor.on_frame

def handle_frame(frame):

"""Receive video frames as NumPy arrays (H, W, 3) RGB uint8"""

print(f"Frame shape: {frame.shape}")

@reactor.on_message

def handle_message(message):

"""Receive application messages from the model"""

print(f"Message: {message}")

@reactor.on_internal_message

def handle_internal(message):

"""Receive internal platform messages (rarely needed)"""

pass

@reactor.on_status(ReactorStatus.READY)

def on_ready(status):

"""React to specific status changes"""

print("Connected to GPU!")

@reactor.on_error

def handle_error(error):

"""Handle errors"""

print(f"Error: {error}")

@reactor.on_track("video")

def handle_track(track):

"""Access a named raw WebRTC MediaStreamTrack"""

print(f"Received track: {track.kind}")

```

</h3></h3>
```
| Event | Payload | Description |

|-------|---------|-------------|

| <code>"status_changed"</code> | <code>ReactorStatus</code> | Connection status changed |

| <code>"session_id_changed"</code> | <code>str \| None</code> | Session ID changed |

| <code>"message"</code> | <code>Any</code> | Application message from the model |

| <code>"runtime_message"</code> | <code>Any</code> | Internal platform message |

| <code>"track_received"</code> | <code>(name: str, track: MediaStreamTrack)</code> | Named track received |

| <code>"error"</code> | <code>ReactorError</code> | Error occurred |

| <code>"session_expiration_changed"</code> | <code>float \| None</code> | Session expiration time updated |

| <code>"capabilities_received"</code> | <code>Capabilities</code> | Model capabilities received |

Note: Python events use <code>snake_case</code> (e.g., <code>"status_changed"</code>) while JavaScript uses <code>camelCase</code> (e.g., <code>"statusChanged"</code>).

</h3></h3>
| Type | Kind | Values / Fields |

|------|------|-----------------|

| <code>ReactorStatus</code> | Enum | <code>DISCONNECTED</code>, <code>CONNECTING</code>, <code>WAITING</code>, <code>READY</code> |

| <code>ReactorState</code> | Dataclass | <code>status: ReactorStatus</code>, <code>last_error: ReactorError \| None</code> |

| <code>ReactorError</code> | Dataclass | <code>code: str</code>, <code>message: str</code>, <code>timestamp: float</code>, <code>recoverable: bool</code>, <code>component: Literal["api", "gpu"]</code>, <code>retry_after: float \| None</code> |

| <code>ReactorEvent</code> | Literal | <code>"status_changed"</code>, <code>"session_id_changed"</code>, <code>"message"</code>, <code>"runtime_message"</code>, <code>"track_received"</code>, <code>"error"</code>, <code>"session_expiration_changed"</code>, <code>"capabilities_received"</code> |

| <code>FrameCallback</code> | Type alias | <code>Callable[[NDArray[np.uint8]], None]</code> — receives RGB frame <code>(H, W, 3)</code> |

| <code>TrackCapability</code> | TypedDict | <code>name: str</code>, <code>kind: TrackKind</code>, <code>direction: TrackDirection</code> |

| <code>Capabilities</code> | TypedDict | <code>protocol_version: str</code>, <code>tracks: list[TrackCapability]</code>, <code>commands?: list[CommandCapability]</code>, <code>emission_fps?: float</code> |

| <code>ConflictError</code> | Exception | Raised when a connection conflict occurs |

| <code>VersionMismatchError</code> | Exception | Raised on 426/501 version negotiation failures |

Common error codes: <code>CONNECTION_FAILED</code>, <code>GPU_CONNECTION_ERROR</code>, <code>RECONNECTION_FAILED</code>

</h3></h3>
```
```
import asyncio

import os

from reactor_sdk import Reactor, ReactorStatus

async def main():

api_key = os.environ["REACTOR_API_KEY"]

async with Reactor(model_name="helios", api_key=api_key) as reactor:

@reactor.on_frame

def on_frame(frame):

print(f"Frame: {frame.shape}")

@reactor.on_status(ReactorStatus.READY)

def on_ready(status):

print("Connected! Sending commands...")

@reactor.on_message

def on_message(message):

print(f"Model says: {message}")

await reactor.connect()

await reactor.send_command("schedule_prompt", {

"prompt": "A sunset over the ocean",

"chunk": 0,

})

await reactor.send_command("start", {})

# Keep running

while reactor.get_status() != ReactorStatus.DISCONNECTED:

await asyncio.sleep(1)

asyncio.run(main())

```
```
---

</h2></h2>
Helios is an interactive, real-time video generation model with infinite streaming. Built on a 14B-parameter Diffusion Transformer, it generates video in 33-frame chunks. It supports text-to-video and image-to-video modes.

Model name: <code>helios</code>

| Command | Parameters | Description |

|---------|------------|-------------|

| <code>set_prompt</code> | <code>prompt: string</code> | Set the prompt (at chunk 0 if not started, current chunk if paused, next chunk if running) |

| <code>schedule_prompt</code> | <code>prompt: string</code>, <code>chunk: integer</code> | Schedule a prompt at a specific chunk index |

| <code>set_image</code> | <code>image_b64: string</code>, <code>transition?: "cut" \| "blend"</code> | Set a base64-encoded reference image (works before or during generation). Transition default: <code>"cut"</code>. |

| <code>clear_image</code> | none | Remove the reference image, continue with text-only conditioning |

| <code>set_seed</code> | <code>seed: integer</code> | Set the RNG seed for reproducible generation |

| <code>start</code> | none | Start generation (requires prompt at chunk 0) |

| <code>pause</code> | none | Pause generation after current chunk finishes |

| <code>resume</code> | none | Resume generation |

| <code>reset</code> | none | Reset to initial state, clears all prompts and history |

**Prompt scheduling rules:**

- Must schedule at least one prompt at chunk 0 before calling <code>start</code>

- Scheduling at an existing chunk overwrites the previous prompt

- Prompts scheduled at past chunks are rejected

- Prompts can be scheduled while generation is running

**Helios State Messages** (<code>type: "state"</code>):

```
```
{

"type": "state",

"data": {

"running": true,

"current_frame": 42,

"current_chunk": 2,

"current_prompt": "A serene mountain landscape",

"paused": false,

"scheduled_prompts": { "0": "A serene mountain landscape" }

}

}

```
```
**Helios Event Messages** (`type: "event"`):

- <code>generation_started</code> (with <code>prompt</code>)

- <code>generation_paused</code> (with <code>frame</code>, <code>chunk</code>)

- <code>generation_resumed</code> (with <code>frame</code>, <code>chunk</code>)

- <code>generation_reset</code> (with <code>frame</code>, <code>chunk</code>)

- <code>image_set</code> (with <code>width</code>, <code>height</code>, <code>transition</code>)

- <code>image_cleared</code>

- <code>seed_set</code> (with <code>seed</code>)

- <code>prompt_scheduled</code> (with <code>chunk</code>, <code>prompt</code>)

- <code>prompt_switched</code> (with <code>frame</code>, <code>chunk</code>, <code>new_prompt</code>, <code>previous_prompt</code>)

- <code>error</code> (with <code>message</code>)

</h3></h3>
```
```
const reactor = new Reactor({ modelName: "helios" });

await reactor.connect(token);

await reactor.sendCommand("set_seed", { seed: 42 });

await reactor.sendCommand("schedule_prompt", {

prompt: "A peaceful forest at dawn",

chunk: 0

});

await reactor.sendCommand("schedule_prompt", {

prompt: "A deer walking through the misty forest",

chunk: 10

});

await reactor.sendCommand("start", {});

```
```
---

</h2></h2>
- <code>/overview</code> — Introduction and example usage

- <code>/quickstart</code> — Getting started guide with CLI and manual setup

- <code>/authentication</code> — Authentication (JavaScript and Python)

- <code>/models/overview</code> — Available models index

- <code>/models/helios</code> — Helios model reference (autoregressive chunked video generation)

- <code>/javascript-guide</code> — JavaScript SDK usage patterns and best practices

- <code>/python-guide</code> — Python SDK usage patterns and best practices

- <code>/concepts/sessions</code> — Sessions, connection lifecycle, and reconnection

- <code>/concepts/commands-and-messages</code> — Commands and messages

- <code>/api-reference/overview</code> — API reference introduction (both SDKs)

- <code>/api-reference/reactor-class</code> — JavaScript Reactor class API

- <code>/api-reference/react-components</code> — ReactorProvider, ReactorView, WebcamStream, ReactorController

- <code>/api-reference/react-hooks</code> — useReactor, useReactorMessage, useStats

- <code>/api-reference/types</code> — JavaScript TypeScript type definitions

- <code>/api-reference/events</code> — JavaScript event types and handlers

- <code>/api-reference/python/reactor</code> — Python Reactor class API

- <code>/api-reference/python/decorators</code> — Python decorator-based event handlers

- <code>/api-reference/python/types</code> — Python types, enums, and utilities
