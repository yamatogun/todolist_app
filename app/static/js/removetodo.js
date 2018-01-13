// when mouse over the todo: change color and make the bin button appear
var lis = document.getElementsByTagName("li");

for (var i=0; i < lis.length; i++){
  var li = lis[i];
  // make the garbage bin icon appear
  li.onmouseover = function(){
    var garbageBin = this.querySelectorAll("input")[0];
    garbageBin.style.visibility = "visible";
  };
  // make it disappear when the mouse moves out
  li.onmouseout = function(){
    var garbageBin = this.querySelectorAll("input")[0];
    garbageBin.style.visibility = "hidden";
  };
}

// Ajax request to send id of the todo to delete 

var delete_buttons = document.getElementsByClassName("remove-todo");
var url = "/removetodo";
var csrf_token = document.getElementById("csrf-token").content;

for (var i=0; i < delete_buttons.length; i++){
  var delete_button = delete_buttons[i];
  delete_button.onclick = function(e){
    e.preventDefault();  // mandatory ?
    var request = new XMLHttpRequest();
    request.open("POST", url);
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    request.setRequestHeader('X-CSRFToken', csrf_token);

    // what to do when server response is received
    request.onreadystatechange = function(){
      if (this.readyState == 4 && this.status === 200){
        // delete corresponding todo item
        var li_id = "todo-" + todo_id;
        var li = document.getElementById(li_id);
        li.parentNode.removeChild(li);
        
      }
    }
    
    var button_id = this.id;  // delete button and li ancestor have same id
    var todo_id = button_id.split("-")[1];  // could be improved
    todo_id = encodeURIComponent(todo_id);
    var data = "todo-id=" + todo_id;
    console.log(data);
    request.send(data);
  };
}
