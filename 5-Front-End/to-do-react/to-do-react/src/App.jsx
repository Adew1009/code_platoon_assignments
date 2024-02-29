import { useStatecd } from 'react'
import './App.css'
import taskData from "./tasks.json";


function App() {
  const [tasks, setTasks] = useState([taskData]);

  const addTask = (newTask) => {setTasks([...tasks, newTask]);

  const renderTask 

  return (
    <div>
      <button onClick={() => addTask({ id: tasks.length + 1, task: `newTask${tasks.length + 1}`, completed: false })}>
        Add Item
      </button>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task.task}</li>
        ))}
      </ul>
    </div>
  );
}
}
  
export default App
