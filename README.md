**Technical Interview Task: Node.js and Microcontroller Communication via MQTT**

In this task, you'll set up a simple communication protocol between a Node.js server and a microcontroller using MQTT. The goal is to have the server send a message in JSON format to the microcontroller, which will parse the message and send an acknowledgment back in JSON.

### Requirements

1. **Set up the Node.js server:**

   - Create a Node.js server that connects to an MQTT broker.
   - The server should send a JSON-formatted message to the microcontroller:
     ```json
     {
       "message": "hello"
     }
     ```

2. **Microcontroller Requirements:**

   - The microcontroller (provided) should connect to the same MQTT broker.
   - It should subscribe to the same topic that the server uses to send messages.
   - Upon receiving the JSON message, the microcontroller should parse the JSON and respond with a JSON message:
     ```json
     {
       "response": "hello received"
     }
     ```

3. **Acknowledgment Handling:**
   - The Node.js server should print the acknowledgment from the microcontroller to the console when it receives it.

### Notes

- You are recommended to use https://www.emqx.com/en as your mqtt broker.
