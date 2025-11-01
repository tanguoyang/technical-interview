Here’s a clear and professional **README** draft for **Part A** of your technical challenge:

---

# Part A: Designing a Finite State Machine for a Virtual Elevator

## 📘 Overview

This exercise introduces you to the **Finite State Machine (FSM)** design pattern — a foundational concept in real-time and embedded systems engineering. You’ll learn how to model system behavior as a collection of **states**, **events**, and **transitions**, then apply that understanding to design the logic of a **virtual elevator**.

---

## 🤖 What Is a Finite State Machine?

A **Finite State Machine (FSM)** is a computational model used to describe how a system reacts to events.
An FSM has:

- A **finite number of states**
- A **current active state**
- A set of **events** or **inputs** that trigger **transitions**
- Optional **actions** that occur during a transition

At any given time, the FSM can be in exactly **one** state. When an event occurs, it may cause the machine to transition to another state based on defined rules.

---

## 💡 Why Use FSMs?

Finite State Machines are ideal for systems that must respond to **external events** in a predictable and maintainable way — especially when timing, safety, or sequencing matters.
They help by:

- Making complex behavior **explicit** and **traceable**
- Preventing **ambiguous or invalid transitions**
- Allowing developers to reason about system behavior under all possible conditions

FSMs are widely used in:

- **Robotics** (navigation, actuation, task sequencing)
- **Embedded systems** (controllers, appliances)
- **Network protocols** (TCP, HTTP handshakes)
- **Games and UI flows** (menu navigation, animation states)

---

## ⚙️ Simple Examples

### Example 1 — Traffic Light Controller

| Event         | Current State | Next State |
| ------------- | ------------- | ---------- |
| Timer Expired | Green         | Yellow     |
| Timer Expired | Yellow        | Red        |
| Timer Expired | Red           | Green      |

**States:** Green → Yellow → Red → Green (loop)
**Why FSM helps:** Guarantees that the system never jumps directly from Green → Red.

---

### Example 2 — Door System

| Event                    | Current State | Next State |
| ------------------------ | ------------- | ---------- |
| Press Open               | Closed        | Opening    |
| Opening Complete         | Opening       | Open       |
| Press Close              | Open          | Closing    |
| Closing Complete         | Closing       | Closed     |
| Press Open While Closing | Closing       | Opening    |

**Why FSM helps:** Ensures the door can’t open and close at the same time, and adds clear safety logic.

---

## 🏗️ Your Task

Design a **Finite State Machine** that models the behavior of an **elevator cabin**.

Your FSM design should include:

1. **States** – e.g. Stationary, In Motion, Door Opening, Door Open, Door Closing
2. **Events** – e.g. Button Press, Arrival at Floor, Door Timer Expired
3. **Transitions** – What triggers a change from one state to another
4. **Timing and Safety Rules** – e.g. doors take time to open/close, can be interrupted by safety sensors

You may express your FSM as:

- A **state-transition diagram** (preferred)
- A **state table**
- Or **pseudocode** showing the state logic

Focus on **clarity** and **correctness** over code — we’ll implement it in **Part B**.
