import "./App.css";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div className="app">

      <Navbar />

      <Hero />

      <ChatBox />

    </div>
  );
}

export default App;