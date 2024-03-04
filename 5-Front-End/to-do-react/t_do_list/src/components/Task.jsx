import React from 'react'

const Task = (props) => {
  const completion = (props.task.completed) ? "completed" : "incomplete"
  return (
    <li>
      <div className={completion}>{props.task.description}</div>
    </li>
  );
}

export default Task