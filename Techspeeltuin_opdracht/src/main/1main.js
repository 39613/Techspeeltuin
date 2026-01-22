import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ port: 8080 });

let latestDistance = null;

wss.on("connection", (ws) => {
  if (latestDistance !== null) {
    ws.send(JSON.stringify({ distance: latestDistance }));
  }
});

export function broadcast(distance) {
  latestDistance = distance;
  const msg = JSON.stringify({ distance });
  wss.clients.forEach(c => c.send(msg));
}
