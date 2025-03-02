import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Skeleton } from "@/components/ui/skeleton";
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { getHeadlines } from "@/api";

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [headlinerResponse, setHeadlinerResponse] = useState("");
  const [userQuery, setUserQuery] = useState("");

  function handleQueryChange(event) {
    setUserQuery(event.target.value);
  }

  function handleKeyDown(event) {
    if (event.key === "Enter") {
      onClickSend();
    }
  }

  async function onClickSend() {
    setIsLoading(true);
    const response = await getHeadlines(userQuery);
    setHeadlinerResponse(response);
    setIsLoading(false);
  }

  const components = {
    h3: ({ children }) => (
      <h3 className="text-4xl font-semibold text-slate-800 mb-3">{children}</h3>
    ),
    a: ({ href, children }) => (
      <a href={href} className="text-2xl font-light text-slate-800/75">
        {children}
      </a>
    ),
    ul: ({ children }) => (
      <ul className="list-disc pl-2 marker:text-slate-700">{children}</ul>
    ),
  };

  return (
    <div className="flex flex-col items-center bg-sky-300/75 h-screen">
      <div className="flex flex-col items-center m-5 w-1/2">
        <h1 className="font-sans text-6xl font-semibold">Headliner</h1>
        <p className="italic text-lg">
          The first place to find the news that matter.
        </p>
        <div className="flex flex-row gap-2 w-2/3 my-5">
          <Input
            className="bg-slate-200"
            placeholder="What's new in tech in the London area?"
            onChange={handleQueryChange}
            onKeyDown={handleKeyDown}
            value={userQuery}
          />
          <Button
            type="button"
            variant="secondary"
            onClick={onClickSend}
            disabled={isLoading}
          >
            Send
          </Button>
        </div>
        <div className="w-2/3">
          {isLoading ? (
            <Skeleton className="h-screen" />
          ) : (
            <div className="h-screen">
              <ReactMarkdown components={components}>
                {headlinerResponse}
              </ReactMarkdown>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
