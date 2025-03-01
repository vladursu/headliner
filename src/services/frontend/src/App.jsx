import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Skeleton } from "@/components/ui/skeleton";
import { useState } from "react";
import { getHeadlines } from "@/api";

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [headlinerResponse, setHeadlinerResponse] = useState("");
  const [userQuery, setUserQuery] = useState("");

  function handleQueryChange(event) {
    setUserQuery(event.target.value);
  }

  async function onClickSend() {
    setIsLoading(true);
    response = await getHeadlines(userQuery);
    setHeadlinerResponse(response);
    setIsLoading(false);
  }

  return (
    <div className="flex flex-col items-center bg-sky-300 h-screen">
      <div className="flex flex-col items-center m-5 w-1/2">
        <h1 className="font-sans text-5xl font-semibold">Headliner</h1>
        <p className="italic text-lg">
          The first place to find the news that matters.
        </p>
        <div className="flex flex-row gap-2 w-2/3 my-5">
          <Input
            className="bg-slate-200"
            placeholder="What's new in tech in the London area?"
            onChange={handleQueryChange}
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
            <Skeleton className="h-40" />
          ) : (
            <div className="bg-sky-300/75 p-5">{headlinerResponse}</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
