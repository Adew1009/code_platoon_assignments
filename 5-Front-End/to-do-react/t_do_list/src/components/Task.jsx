import React from 'react'

const Task = (props) => {
  const completion = (props.task.completed) ? "completed" : "incomplete"
  return (
    <li>
      <div className={completion} id={props.task.id}>{props.task.description}</div>
    </li>
  );
}

export default Task