\> \#\# Documentation Index  
\> Fetch the complete documentation index at: https://docs.reactor.inc/llms.txt  
\> Use this file to discover all available pages before exploring further.

\# Quickstart

\> Get a real-time world model running in minutes

\<Tabs\>  
  \<Tab title="JavaScript"\>  
    Connect a React app to a real-time world model. By the end of this guide, video will be streaming in  
    your browser in real-time.

    \#\# Prerequisites

    \* Node.js 18+  
    \* A \[Reactor API key\](https://docs.reactor.inc/authentication)

    \#\# Option 1: CLI command

    The easiest way to get started is by using the \`create-reactor-app\` CLI. This tool generates a  
    ready-to-run Next.js app with the SDK installed and secure auth already configured.

    \<Steps\>  
      \<Step title="Create your app"\>  
        \<CodeGroup\>  
          \`\`\`shell npm theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
          npx create-reactor-app my-app  
          \`\`\`

          \`\`\`shell pnpm theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
          pnpm create reactor-app my-app  
          \`\`\`  
        \</CodeGroup\>

        This will clone our example application and install dependencies.  
      \</Step\>

      \<Step title="Add your API key"\>  
        Move into the new directory, create a copy of \`.env.example\` and name it \`.env\`.

        \`\`\`bash theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        cd my-app  
        cp .env.example .env  
        \`\`\`

        Add your API key to \`.env\`:

        \`\`\`bash theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        REACTOR\_API\_KEY=rk\_your\_api\_key\_here  
        \`\`\`  
      \</Step\>

      \<Step title="Run your app"\>  
        \`\`\`shell theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        npm run dev  
        \`\`\`

        \<Check\>  
          Open \[http://localhost:3000\](http://localhost:3000). Click \*\*Connect\*\*, then enter a prompt to start streaming video.  
        \</Check\>  
      \</Step\>  
    \</Steps\>

    \#\# Option 2: Manual setup

    \<Steps\>  
      \<Step title="Install the SDK"\>  
        \<CodeGroup\>  
          \`\`\`shell npm theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
          npm install @reactor-team/js-sdk  
          \`\`\`

          \`\`\`shell pnpm theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
          pnpm add @reactor-team/js-sdk  
          \`\`\`  
        \</CodeGroup\>  
      \</Step\>

      \<Step title="Build your component"\>  
        Create an API route to exchange your key for a token:

        \`\`\`typescript api/token/route.ts theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        import { NextResponse } from "next/server";

        export async function POST() {  
          const r \= await fetch("https://api.reactor.inc/tokens", {  
            method: "POST",  
            headers: { "Reactor-API-Key": process.env.REACTOR\_API\_KEY\! },  
          });  
          const { jwt } \= await r.json();

          return NextResponse.json({ jwt });  
        }  
        \`\`\`

        Then build your component:

        \`\`\`tsx theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        "use client";

        import { use } from "react";  
        import { ReactorProvider, ReactorView } from "@reactor-team/js-sdk";

        async function getToken() {  
          const r \= await fetch("/api/token", { method: "POST" });  
          const { jwt } \= await r.json();  
          return jwt;  
        }

        const tokenPromise \= getToken();

        export default function App() {  
          const token \= use(tokenPromise);

          return (  
            \<ReactorProvider modelName="your-model-name" jwtToken={token}\>  
              \<ReactorView className="w-full aspect-video" /\>  
            \</ReactorProvider\>  
          );  
        }  
        \`\`\`

        \<Info\>  
          This example fetches a token from your backend. See the \[Authentication guide\](/authentication)  
          for how to set up the \`/api/token\` route.  
        \</Info\>  
      \</Step\>

      \<Step title="Run your app"\>  
        Start your dev server and open your app in the browser. Click \*\*Connect\*\*, enter a prompt, and video will begin streaming.

        \<Check\>  
          You should see live video streaming once connected and a prompt is submitted.  
        \</Check\>  
      \</Step\>  
    \</Steps\>  
  \</Tab\>

  \<Tab title="Python"\>  
    Connect a Python script to a real-time world model and receive frames as NumPy arrays.

    \#\# Prerequisites

    \* Python 3.10+  
    \* A \[Reactor API key\](https://reactor.inc/)

    \<Steps\>  
      \<Step title="Install the SDK"\>  
        \`\`\`bash theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        pip install reactor-sdk  
        \`\`\`  
      \</Step\>

      \<Step title="Set your API key"\>  
        \`\`\`bash theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        export REACTOR\_API\_KEY=rk\_your\_api\_key\_here  
        \`\`\`  
      \</Step\>

      \<Step title="Write your script"\>  
        \`\`\`python theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        import asyncio  
        import os  
        from reactor\_sdk import Reactor

        async def main():  
            reactor \= Reactor(  
                model\_name="your-model-name",  
                api\_key=os.environ\["REACTOR\_API\_KEY"\],  
            )

            @reactor.on\_frame  
            def on\_frame(frame):  
                \# (H, W, 3\) uint8 RGB  
                print(f"Frame: {frame.shape}")

            await reactor.connect()  
            await asyncio.Event().wait()  \# run until interrupted

        asyncio.run(main())  
        \`\`\`  
      \</Step\>

      \<Step title="Run it"\>  
        \`\`\`bash theme={"theme":{"light":"github-light","dark":"github-dark-high-contrast"}}  
        python my\_script.py  
        \`\`\`

        \<Check\>  
          You should see \`Frame: (720, 1280, 3)\` printed to the console once the model connects.  
        \</Check\>  
      \</Step\>  
    \</Steps\>  
  \</Tab\>  
\</Tabs\>

\*\*\*

\#\# Next steps

\<CardGroup cols={2}\>  
  \<Card title="Authentication" icon="key" href="/authentication"\>  
    How to set up secure, production-ready auth for your app.  
  \</Card\>

  \<Card title="JavaScript SDK" icon="js" href="/javascript-guide"\>  
    Components, hooks, sending commands, and webcam input.  
  \</Card\>

  \<Card title="Python SDK" icon="python" href="/python-guide"\>  
    Multi-track video, publishing input, reconnection.  
  \</Card\>

  \<Card title="Helios model" icon="video" href="/models/helios"\>  
    All available commands and the messages Helios emits.  
  \</Card\>  
\</CardGroup\>

