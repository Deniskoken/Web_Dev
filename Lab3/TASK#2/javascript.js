const addBtn = document.getElementById('addBtn');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

addBtn.addEventListener('click', function () {

    const taskText = taskInput.value.trim();
    if (taskText === '') return;

    const li = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', function () {
        li.classList.toggle('completed');
    });

    const span = document.createElement('span');
    span.textContent = taskText;

    const deleteBtn = document.createElement('span');
    deleteBtn.innerHTML = '&#128465;'; 
    deleteBtn.className = 'delete-btn';
    deleteBtn.addEventListener('click', function () {
        li.remove();
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);

    taskList.appendChild(li);

    taskInput.value = '';
});
