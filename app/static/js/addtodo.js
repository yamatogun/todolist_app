var submit = document.getElementById("addbutton");

submit.onclick = function(e){
  // prevent form from sending when clicking on submit button
  e.preventDefault();

  var newtodo = document.getElementById("entryfield");
  var value = newtodo.value; 
  encoded_value = encodeURIComponent(value);
  var name = encodeURIComponent("content");
  var pair = name + "=" + encoded_value;
  
  var csrf_token= document.getElementById("csrf-token").content;

  // Send data with Ajax in order to create an new todo task
  var request = new XMLHttpRequest();
  var url = "/addtodo";
  request.open("POST", url);
  request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  request.setRequestHeader("X-CSRFToken", csrf_token);

  request.onreadystatechange = function(){
    if (request.readyState == 4 && request.status === 200){
      console.log(request.responseText);
      todo_id = JSON.parse(request.responseText)["tid"]
      console.log(todo_id);
      // add a new task in the list
      var li = document.createElement("li");
      // give new rank to the li element
      li.id = "todo-" + todo_id;

      var table = document.createElement("table");
      table.className = 'todolist-table';
      li.appendChild(table);

      var tr = document.createElement("tr");
      table.appendChild(tr);

      var td = document.createElement("td");
      td.className = "todo-content todo-cell";
      tr.appendChild(td);

      var p = document.createElement("p");
      p.className = "todotext";
      p.textContent = value;
      td.appendChild(p);

      td = document.createElement("td");
      td.className = "delete-button todo-cell";
      tr.appendChild(td);

      var input = document.createElement('input');
      // input.id = "remove-"
      input.className = "remove-todo";
      input.type = "image";
      input.src = "../static/rubbish-bin.svg";
      input.style.visibility = "hidden";
      // see deleteNode in removetodo.js
      input.onclick = deleteTodo;
      input.id = "remove-" + todo_id
      td.appendChild(input);

      var todolist = document.getElementById("ul-todos");
      todolist.appendChild(li);

      li.onmouseover = function(){
        input.style.visibility = "visible";
      };

      li.onmouseout = function(){
        input.style.visibility = "hidden";
      };

      // clean the input field
      newtodo.value = '';
    }
      
  }
  request.send(pair);
};
