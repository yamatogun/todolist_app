console.log("in da script");

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
