**Technical Interview Task: Node.js and Microcontroller Communication via MQTT**

In this task, you'll set up a simple communication protocol between a Node.js server and a local computer using MQTT. The goal is to build a CLI to send messages from your terminal to the server and have the server send an acknowledgment back in JSON.

### Requirements

1. **Set up the CLI Tool server:**

   - Write a CLI that connects to the MQTT client and sends hello
   - The CLI should send a JSON-formatted message to the server:
     ```json
     {
       "message": "hello"
     }
     ```

2. **Server Requirements:**

   - The Node Server should connect to the same MQTT broker.
   - It should subscribe to the same topic that the server uses to send messages.
   - Upon receiving the JSON message, the microcontroller should parse the JSON and respond with a JSON message:
     ```json
     {
       "response": "hello received"
     }
     ```

3. **Acknowledgment Handling:**
   - The CLI should print the acknowledgment from the server to the console when it receives it.

### Notes

- You are recommended to use https://www.emqx.com/en as your mqtt broker.
