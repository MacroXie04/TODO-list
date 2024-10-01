class TodoList {
    constructor(taskInputId, listContainerId) {
        this.inputBox = document.getElementById(taskInputId);
        this.listContainer = document.getElementById(listContainerId);
        this.tasks = JSON.parse(localStorage.getItem('tasks')) || [];

        this.bindEvents();
        this.renderTasks();
    }

    bindEvents() {
        // 输入时监听回车键
        this.inputBox.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                this.addTask();
            }
        });

        // 监听任务add按键
        this.listContainer.addEventListener('click', (e) => {
            if (e.target.tagName === 'LI') {
                this.toggleTaskCompletion(e.target);
            }
            if (e.target.tagName === 'SPAN') {
                this.deleteTask(e.target);
            }
        });
    }

    addTask() {
        const taskValue = this.inputBox.value.trim();
        if (taskValue === '') {
            alert('Please enter a task');
        } else {
            const task = {
                text: taskValue,
                completed: false
            };
            this.tasks.push(task);
            this.saveTasks();
            this.renderTasks();
        }
        this.inputBox.value = '';
    }

    toggleTaskCompletion(taskElement) {
        const index = Array.from(this.listContainer.children).indexOf(taskElement);
        if (index !== -1) {
            this.tasks[index].completed = !this.tasks[index].completed;
            this.saveTasks();
            this.renderTasks();
        }
    }

    deleteTask(spanElement) {
        const index = spanElement.dataset.index;
        if (index !== undefined) {
            this.tasks.splice(index, 1);
            this.saveTasks();
            this.renderTasks();
        }
    }

    saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(this.tasks));
    }

    renderTasks() {
        this.listContainer.innerHTML = '';
        this.tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.textContent = task.text;
            if (task.completed) {
                li.classList.add('checked');
            }

            const span = document.createElement('span');
            span.innerHTML = '\u00D7';
            span.dataset.index = index;
            li.appendChild(span);

            this.listContainer.appendChild(li);
        });
    }
}


const todoList = new TodoList('task', 'list-continer');