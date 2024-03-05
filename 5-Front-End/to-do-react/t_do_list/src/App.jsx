// 
import { useState } from "react";
import tasks from "./tasks.json";
import "./App.css";
import Task from "./components/Task";

function App() {
  const [taskList, setTaskList] = useState(tasks);
  const [newListItem, setNewListItem] = useState("");

  function handleNewTask(event) {
    setNewListItem(event.target.value);
  }

  function MarkComplete(index) {
    const updatedTaskList = [...taskList];
    updatedTaskList[index].completed = !updatedTaskList[index].completed;
    setTaskList(updatedTaskList);
  }
  function removeComplete(index) {
   const newArr = taskList.filter((_,i) => i !== index);
   setTaskList(newArr);
   console.log(index)
   console.log(taskList);
  }

  function newToList(event) {
    event.preventDefault();
    setTaskList([
      ...taskList,
      { id: taskList.length, description: newListItem, completed: false },
    ]);
    setNewListItem("");
  }

  return (
    <>
      <div></div>
      <h1>To Do List</h1>
      <form onSubmit={newToList}>
        <input
          id="newTask"
          onChange={handleNewTask}
          placeholder="Task"
          type="text"
          value={newListItem}
        />
        <input type="submit" value="Submit" />
      </form>

      <ul>
        {taskList.map((taskObject, index) => (
          <div id={index} key={index} className="task-container">
            <Task task={taskObject} key={index} />
            <button key={"b" + index} onClick={() => MarkComplete(index)}>
              Complete?
            </button>
            <button key={"c" + index} onClick={() => removeComplete(index)}>
              Remove?
            </button>
          </div>
        ))}
      </ul>
    </>
  );
}

export default App;
