> ## Documentation Index

> Fetch the complete documentation index at: https://docs.reactor.inc/llms.txt

> Use this file to discover all available pages before exploring further.

Helios
> Interactive real-time video generation with infinite streaming

**Helios** is an interactive, real-time video generation model built on a 14B-parameter Diffusion Transformer. Unlike static generation APIs, Helios produces a continuous, infinite video stream that you can steer in real time — change prompts, swap reference images, and control playback while the video keeps playing.

</h2></h2>
<CardGroup cols={3}>

<Card title="Autoregressive Streaming" icon="film">

Continuous, infinite video stream with smooth temporal coherence across minutes of generation

</Card>

<Card title="Image-to-Video" icon="image">

Provide a reference image to guide generation and swap it mid-stream with cut or blend transitions

</Card>

<Card title="Real-Time Prompt Control" icon="wand-sparkles">

Schedule prompt changes at specific points during generation for dynamic scene transitions

</Card>

</CardGroup>

</h2></h2>
Get started with Helios in seconds:

<Tabs>

<Tab title="npm">

```
```
npx create-reactor-app my-helios-app helios-interactive

```
```
</Tab>

<Tab title="pnpm">

```
```
pnpm create reactor-app my-helios-app helios-interactive

```
```
</Tab>

</Tabs>

This creates a Next.js application from our [open-source example](https://github.com/reactor-team/reactor-experiments/tree/main/helios-interactive).

***

</h2></h2>
<code>helios</code>

***

</h2></h2>
Getting good results from Helios depends heavily on how you write your prompts. For a detailed breakdown of techniques and examples, see the [Prompt Guide](/models/prompt-guide).

<AccordionGroup>

<Accordion title="Be detailed and descriptive" icon="pen-fancy">

Helios responds best to **long, richly detailed prompts**. Instead of short descriptions, paint a full picture: describe the scene, lighting, camera angle, atmosphere, and any objects or characters present.

<Tabs>

<Tab title="Good">

```
```
A rotating camera view inside a large New York museum gallery, showcasing a towering stack of vintage televisions, each displaying different programs from the 1950s and 1970s. The televisions show a mix of 1950s sci-fi movies, horror films, news broadcasts, static, and a 1970s sitcom. The gallery space is filled with the nostalgic glow of the old TV screens, their edges worn and frames aged. The background features other vintage exhibits and artifacts, adding to the historical ambiance. The televisions are arranged in a dynamic, almost chaotic pattern, creating a sense of visual interest and movement. A wide-angle shot capturing the entire stack and the surrounding gallery space.

```
```
</Tab>

<Tab title="Too vague">

```
```
A desert with a camel

```
```
</Tab>

</Tabs>

</Accordion>

<Accordion title="Prompt transitions need detail too" icon="shuffle">

When updating the prompt mid-generation with <code>set_prompt</code> or <code>schedule_prompt</code>, the new prompt should be **just as detailed** as the original. Vague transition prompts will produce subtle or unnoticeable changes.

<Tabs>

<Tab title="Good">

```
```
A rotating camera view inside a large New York museum gallery, showcasing a towering stack of vintage televisions, each displaying different programs from the 1950s and 1970s. The televisions show the text REACTOR. The gallery space is filled with the nostalgic glow of the old TV screens, their edges worn and frames aged. The background features other vintage exhibits and artifacts, adding to the historical ambiance. The televisions are arranged in a dynamic, almost chaotic pattern, creating a sense of visual interest and movement. A wide-angle shot capturing the entire stack and the surrounding gallery space.

```
```
</Tab>

<Tab title="Too vague">

```
```
The televisions show the text REACTOR.

```
```
</Tab>

</Tabs>

</Accordion>

</AccordionGroup>

<Info>

Helios generates video in short segments called **chunks**, each 33 frames long. You can send commands at any time, but they take effect at the start of the next chunk. This means there can be a short delay between sending a command and seeing the change in the video.

</Info>

***

</h2></h2>
When you connect to Helios, the model is active and ready but won't start generating until you explicitly tell it to. Here's the workflow:

1. **Connect** to the model

2. **Set a prompt** using <code>set_prompt</code> or <code>schedule_prompt</code> at chunk 0 (required)

3. **Optionally upload and set a reference image** for image-to-video mode

4. **Start** generation

5. **Control** playback with pause/resume as needed

6. **Schedule** additional prompts at future chunks or reset to start over

7. **Change or remove the reference image** mid-generation with cut or blend transitions

<Note>

Helios generates video in short segments called **chunks**, each 33 frames long. You can send commands at any time, but they take effect at the start of the next chunk. This means there can be a short delay between sending a command and seeing the change in the video.

</Note>

***

</h2></h2>
Send commands to the model using <code>reactor.sendCommand()</code>. Below are all available commands:

| Command           | Description                                                 |

| ----------------- | ----------------------------------------------------------- |

| <code>set_prompt</code>      | Set the prompt (at chunk 0, or current chunk if running)    |

| <code>schedule_prompt</code> | Schedule a prompt at a specific chunk index                 |

| <code>set_image</code>       | Set or change a reference image (works mid-generation)      |

| <code>clear_image</code>     | Remove image anchor, continue with text only                |

| <code>set_seed</code>        | Set a seed for reproducible output — same seed = same video |

| <code>start</code>           | Begin video generation                                      |

| <code>pause</code>           | Pause generation                                            |

| <code>resume</code>          | Resume generation                                           |

| <code>reset</code>           | Reset to initial state                                      |

<Tabs>

<Tab title="set_prompt">

## set\_prompt

Convenience wrapper around <code>schedule_prompt</code> that automatically picks the right chunk index so you don't have to track it yourself:

* **Not started**: schedules at chunk 0

* **Paused**: schedules at the current chunk (takes effect on resume)

* **Running**: schedules at the next chunk (current chunk is already being processed)

This is the simplest way to change the prompt — just call <code>set_prompt</code> and the model figures out when to apply it.

**Parameters:**

| Parameter | Type   | Required | Description                           |

| --------- | ------ | -------- | ------------------------------------- |

| <code>prompt</code>  | string | Yes      | The prompt text to use for generation |

**Example:**

```
```
// Set initial prompt (before starting)

await reactor.sendCommand("set_prompt", {

prompt: "A serene mountain landscape at sunrise"

});

// Change prompt mid-generation — automatically applies at the next chunk

await reactor.sendCommand("set_prompt", {

prompt: "The landscape transitions to a stormy ocean"

});

```
```
</Tab>

<Tab title="schedule_prompt">

## schedule\_prompt

Schedule a prompt to be applied at a specific chunk index during video generation.

**Parameters:**

| Parameter | Type    | Required | Description                                  |

| --------- | ------- | -------- | -------------------------------------------- |

| <code>prompt</code>  | string  | Yes      | The prompt text to use                       |

| <code>chunk</code>   | integer | Yes      | The chunk index at which to apply the prompt |

**Behavior:**

* Scheduling a prompt at a chunk that already has a prompt will overwrite it

* Prompts scheduled in the past are rejected (e.g., if the model is at chunk 10 and you schedule at chunk 5, an error is emitted)

* A prompt must exist at chunk 0 before calling <code>start</code>

* Prompts can be scheduled while generation is running for real-time control

**Example:**

```
```
// Schedule initial prompt (required before start)

await reactor.sendCommand("schedule_prompt", {

prompt: "A serene mountain landscape at sunrise",

chunk: 0

});

// Schedule a transition at chunk 10

await reactor.sendCommand("schedule_prompt", {

prompt: "The mountain transforms into a futuristic city",

chunk: 10

});

```
```
</Tab>

<Tab title="set_image">

## set\_image

Set or change the reference image for image-to-video conditioning. Can be called before or during generation.

Upload the image first with <code>uploadFile()</code>, then pass the returned [<code>FileRef</code>](/api-reference/types#fileref) as the <code>image</code> parameter. See [File Uploads](/concepts/file-uploads) for more details.

**Parameters:**

| Parameter    | Type    | Required | Description                                                                          |

| ------------ | ------- | -------- | ------------------------------------------------------------------------------------ |

| <code>image</code>      | FileRef | Yes      | A reference to an uploaded image, returned by <code>uploadFile()</code>                         |

| <code>transition</code> | string  | No       | Transition mode: <code>"cut"</code> for immediate switch (default), <code>"blend"</code> for interpolation |

**Behavior:**

* Can be set before starting or while generation is running

* The image is resized to match the model's output resolution

* Use <code>transition: "blend"</code> for a smooth interpolation to the new image, or <code>"cut"</code> for an immediate switch

**Example:**

```
```
const ref = await reactor.uploadFile(imageFile);

await reactor.sendCommand("set_image", { image: ref });

// Swap mid-generation with a smooth blend

const newRef = await reactor.uploadFile(newImageFile);

await reactor.sendCommand("set_image", {

image: newRef,

transition: "blend"

});

```
```
</Tab>

<Tab title="clear_image">

## clear\_image

Remove the reference image anchor. Generation continues with text-only conditioning.

**Parameters:** None

**Example:**

```
```
await reactor.sendCommand("clear_image", {});

```
```
</Tab>

<Tab title="set_seed">

## set\_seed

Set a seed for reproducible output. Using the same seed with the same prompts will produce the same video.

**Parameters:**

| Parameter | Type    | Required | Description |

| --------- | ------- | -------- | ----------- |

| <code>seed</code>    | integer | Yes      | Seed value  |

**Behavior:**

* If generation hasn't started, the seed takes effect immediately

* If generation is running, the seed takes effect on the next <code>reset</code>

**Example:**

```
```
await reactor.sendCommand("set_seed", { seed: 42 });

```
```
</Tab>

<Tab title="start">

## start

Begin the video generation process.

**Parameters:** None

**Requirements:**

* A prompt must be scheduled at chunk 0 before calling this command (via <code>set_prompt</code> or <code>schedule_prompt</code>)

**Example:**

```
```
await reactor.sendCommand("start", {});

```
```
</Tab>

<Tab title="pause">

## pause

Pause the video generation after the current chunk finishes processing. The model retains its full state including history buffers.

**Parameters:** None

**Example:**

```
```
await reactor.sendCommand("pause", {});

```
```
</Tab>

<Tab title="resume">

## resume

Resume video generation from where it was paused.

**Parameters:** None

**Example:**

```
```
await reactor.sendCommand("resume", {});

```
```
</Tab>

<Tab title="reset">

## reset

Stop generation and reset the model to its initial state.

**Parameters:** None

**Effects:**

* Halts any ongoing generation

* Clears all scheduled prompts and history buffers

* Resets the seed

* Returns the model to a clean state ready for new prompts

**Example:**

```
```
await reactor.sendCommand("reset", {});

```
```
</Tab>

</Tabs>

***

</h2></h2>
Listen for messages from the model using <code>reactor.on("message", ...)</code> (imperative) or the <code>useReactorMessage()</code> hook (React). The model emits two types of messages:

</h3></h3>
State messages provide a snapshot of the current model state. They are emitted:

* When a prompt is scheduled

* When generation starts

* When generation is paused or resumed

* When a prompt switch occurs at a chunk boundary

* When generation is reset

* After each chunk is processed

```
```
{

type: "state",

data: {

running: boolean,                // Whether generation is actively running

current_frame: number,           // Global pixel frame counter

current_chunk: number,           // Current chunk index

current_prompt: string | null,   // Active prompt text (null if not started)

paused: boolean,                 // Whether generation is paused

scheduled_prompts: {             // Map of chunk indices to prompts

[chunk: number]: string

}

}

}

```
```
**Example handler:**

<CodeGroup>

```
```
reactor.on("message", (msg) => {

if (msg.type === "state") {

console.log(<code>Running: ${msg.data.running}</code>);

console.log(<code>Frame: ${msg.data.current_frame}</code>);

console.log(<code>Chunk: ${msg.data.current_chunk}</code>);

console.log(<code>Prompt: ${msg.data.current_prompt}</code>);

console.log(<code>Paused: ${msg.data.paused}</code>);

}

});

```
```
```tsx React API theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}

import { useReactorMessage } from "@reactor-team/js-sdk";

function StateDisplay() {

const [running, setRunning] = useState(false);

const [frame, setFrame] = useState(0);

const [chunk, setChunk] = useState(0);

const [prompt, setPrompt] = useState<string | null>(null);

const [paused, setPaused] = useState(true);

useReactorMessage((msg) => {

if (msg.type === "state") {

setRunning(msg.data.running);

setFrame(msg.data.current_frame);

setChunk(msg.data.current_chunk);

setPrompt(msg.data.current_prompt);

setPaused(msg.data.paused);

}

});

return <div>Running: {running ? "Yes" : "No"} | Chunk: {chunk} | Frame: {frame}</div>;

}

```
```
</CodeGroup>

</h3></h3>
Emitted when lifecycle events occur:

```
```
{

type: "event",

data: {

event: string,  // Event type

// Additional fields depending on event type

}

}

```

</h4></h4>
```
| Event                | Description                               | Additional Fields                                       |

| -------------------- | ----------------------------------------- | ------------------------------------------------------- |

| <code>generation_started</code> | Generation has begun                      | <code>prompt: string</code>                                        |

| <code>generation_paused</code>  | Generation was paused                     | <code>frame: number</code>, <code>chunk: number</code>                        |

| <code>generation_resumed</code> | Generation was resumed                    | <code>frame: number</code>, <code>chunk: number</code>                        |

| <code>generation_reset</code>   | Model was reset                           | <code>frame: number</code>, <code>chunk: number</code>                        |

| <code>image_set</code>          | Reference image was set or changed        | <code>width: number</code>, <code>height: number</code>, <code>transition: string</code> |

| <code>image_cleared</code>      | Reference image was removed               | —                                                       |

| <code>seed_set</code>           | Seed was updated                          | <code>seed: number</code>                                          |

| <code>prompt_scheduled</code>   | A prompt was scheduled                    | <code>chunk: number</code>, <code>prompt: string</code>                       |

| <code>prompt_switched</code>    | Active prompt changed at a chunk boundary | <code>frame</code>, <code>chunk</code>, <code>new_prompt</code>, <code>previous_prompt</code>       |

| <code>error</code>              | An error occurred                         | <code>message: string</code>                                       |

**Example handler:**

<CodeGroup>

```
```
reactor.on("message", (msg) => {

if (msg.type === "event") {

switch (msg.data.event) {

case "generation_started":

console.log(<code>Generation started with prompt: ${msg.data.prompt}</code>);

break;

case "generation_reset":

console.log(<code>Reset at frame ${msg.data.frame}, chunk ${msg.data.chunk}</code>);

break;

case "image_set":

console.log(<code>Reference image set: ${msg.data.width}x${msg.data.height}</code>);

break;

case "seed_set":

console.log(<code>Seed set to ${msg.data.seed}</code>);

break;

case "prompt_scheduled":

console.log(<code>Prompt scheduled at chunk ${msg.data.chunk}: ${msg.data.prompt}</code>);

break;

case "prompt_switched":

console.log(<code>Switched to: ${msg.data.new_prompt}</code>);

break;

case "error":

console.error(<code>Error: ${msg.data.message}</code>);

break;

}

}

});

```
```
```tsx React API theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}

import { useReactorMessage } from "@reactor-team/js-sdk";

function EventHandler() {

useReactorMessage((msg) => {

if (msg.type === "event") {

switch (msg.data.event) {

case "generation_started":

console.log(<code>Generation started with prompt: ${msg.data.prompt}</code>);

break;

case "generation_reset":

console.log(<code>Reset at frame ${msg.data.frame}, chunk ${msg.data.chunk}</code>);

break;

case "image_set":

console.log(<code>Reference image set: ${msg.data.width}x${msg.data.height}</code>);

break;

case "seed_set":

console.log(<code>Seed set to ${msg.data.seed}</code>);

break;

case "prompt_scheduled":

console.log(<code>Prompt scheduled at chunk ${msg.data.chunk}: ${msg.data.prompt}</code>);

break;

case "prompt_switched":

console.log(<code>Switched to: ${msg.data.new_prompt}</code>);

break;

case "error":

console.error(<code>Error: ${msg.data.message}</code>);

break;

}

}

});

return null; // This component just handles events

}

```
```
</CodeGroup>

***

</h2></h2>
```
```
import { Reactor } from "@reactor-team/js-sdk";

const reactor = new Reactor({

modelName: "helios",

});

// Set up video display

const videoElement = document.getElementById("video") as HTMLVideoElement;

reactor.on("trackReceived", (name, track, stream) => {

videoElement.srcObject = stream;

videoElement.play().catch(console.warn);

});

// Listen for state updates

reactor.on("message", (msg) => {

if (msg.type === "state") {

document.getElementById("info")!.textContent =

<code>Chunk: ${msg.data.current_chunk} | Frame: ${msg.data.current_frame}</code>;

}

if (msg.type === "event" && msg.data.event === "prompt_switched") {

console.log(<code>Now showing: ${msg.data.new_prompt}</code>);

}

});

// Connect (see Authentication guide for how to obtain a token)

await reactor.connect(token);

// Set a seed for reproducibility

await reactor.sendCommand("set_seed", { seed: 42 });

// Schedule prompts for a cinematic sequence

await reactor.sendCommand("schedule_prompt", {

prompt: "A peaceful forest at dawn, soft morning light filtering through the trees",

chunk: 0

});

await reactor.sendCommand("schedule_prompt", {

prompt: "Sunlight breaking through the canopy, golden rays illuminating the forest floor",

chunk: 5

});

await reactor.sendCommand("schedule_prompt", {

prompt: "A deer walking through the misty forest clearing",

chunk: 10

});

// Start generation

await reactor.sendCommand("start", {});

```
```
***

</h2></h2>
Use a reference image to guide generation. Upload the image first, then pass it to <code>set_image</code> before starting.

```
```
import { Reactor } from "@reactor-team/js-sdk";

const reactor = new Reactor({

modelName: "helios",

});

// Set up video display

const videoElement = document.getElementById("video") as HTMLVideoElement;

reactor.on("trackReceived", (name, track, stream) => {

videoElement.srcObject = stream;

videoElement.play().catch(console.warn);

});

// Connect

await reactor.connect(token);

// Upload a reference image

const fileInput = document.getElementById("file") as HTMLInputElement;

const imageFile = fileInput.files![0];

const imageRef = await reactor.uploadFile(imageFile);

// Set the reference image and a prompt

await reactor.sendCommand("set_image", { image: imageRef });

await reactor.sendCommand("set_prompt", {

prompt: "A cinematic slow zoom into the scene, golden hour lighting, gentle motion"

});

// Start generation

await reactor.sendCommand("start", {});

// Later: swap to a new image mid-generation with a smooth blend

const newInput = document.getElementById("new-file") as HTMLInputElement;

const newRef = await reactor.uploadFile(newInput.files![0]);

await reactor.sendCommand("set_image", {

image: newRef,

transition: "blend"

});

```

