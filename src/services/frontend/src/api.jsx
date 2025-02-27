const BACKEND_BASE_URL = "http://localhost:50051/";
const GET_HEADLINES_ENDPOINT = "headlines";

export async function getHeadlines(query) {
  return fetch(`${BACKEND_BASE_URL}${GET_HEADLINES_ENDPOINT}`, {
    headers: { "Content-Type": "application/json" },
    method: "POST",
    body: JSON.stringify({ query }),
  });
}
