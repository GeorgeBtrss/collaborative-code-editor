import { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000");
const ROOM_ID = "test-room";

function App() {
  const [text, setText] = useState("");

  useEffect(() => {
    // ✅ JOIN THE ROOM
    socket.emit("join_room", ROOM_ID);

    socket.on("code_update", (newText) => {
      setText(newText);
    });

    return () => {
      socket.off("code_update");
    };
  }, []);

  const handleChange = (e) => {
    setText(e.target.value);

    socket.emit("code_change", {
      roomId: ROOM_ID,
      code: e.target.value,
    });
  };

  return (
    <textarea
      value={text}
      onChange={handleChange}
      style={{ width: "90%", height: "90vh", fontSize: "16px" }}
    />
  );
}

export default App;