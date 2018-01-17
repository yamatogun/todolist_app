console.log("update status script");

var checkboxes = document.getElementsByClassName("status-checkbox");
var csrf_token = document.getElementById("csrf-token").content;
var url = "/updatestatus";

for (var i=0; i<checkboxes.length; i++){
  var checkbox = checkboxes[i];
  var tid = checkbox.id.split('-')[1];
  checkbox.onchange = (function(tid){
    function change_handler(){
      var request = new XMLHttpRequest();
      request.open("POST", url);
      request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      request.setRequestHeader("X-CSRFToken", csrf_token);

      request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status === 200){
          var selector = "li[id=todo-" + tid + "]" + " table";
          var table =  document.querySelectorAll(selector)[0];
          if (todo_status === "true"){
            table.className = table.className + " " + 'todo-completed';
            console.log("className: " + table.className);
          }
          else{
            table.className = "todolist-table";
            console.log("className: " + table.className);
          }
        }
      };

      var pairs = [];

      if (this.checked) var todo_status = "true";
      else var todo_status = "false";
      todo_status = encodeURIComponent(todo_status);
      var par = encodeURIComponent("todo-status");
      var pair = par + "=" + todo_status;
      pairs.push(pair)

      par = encodeURIComponent("tid");
      pair = par + "=" + tid;
      pairs.push(pair)

      pairs = pairs.join("&");
      request.send(pairs);
    };
  return change_handler;
  }(tid));
}

