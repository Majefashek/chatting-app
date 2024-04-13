$(document).ready(function () {
  console.log(window.location.host + "/messages/room/");
  function getUserInfo() {
    var sender_id = $("#user2").data('id');
    var user_id = $(this).data("id");
    return { sender_id: sender_id, user_id: user_id };
  }
  user_info = getUserInfo();
  sender_id = user_info.sender_id;
  reciever_id = user_info.user_id;
  console.log(sender_id)
  function getRoomName(user_id) {
    id = user_id;
    $.ajax({
      url: window.location.host + "/messages/room/" + id,
      type: "GET",
      success: function (response) {
        updateMessages(response);
      },
      error: function () {
        console.log("Error retrieving room name.");
      },
    });
  }

  // Function to handle user clicks

  // Function to fetch messages via AJAX
  // function fetchMessages(username) {
  // $.ajax({
  //url: "/messages/" + username + "/",
  //type: "GET",
  //success: function (response) {
  //updateMessages(response);
  //},
  //});
  //}

  // Function to update messages section
  function updateMessages(messages) {
    $("#messages").html(messages);
  }

  // Function to handle WebSocket communication
  function handleWebSocket(room_name) {
    var socket = new WebSocket(
      "ws://localhost:8000/ws/chat/" + room_name + "/"
    );
    socket.onmessage = function (e) {
      updateMessages("<div>" + e.data + "</div>");
    };
  }

  function handleUserClick() {
    user_info = getUserInfo();
    sender_id = user_info.sender_id;
    reciever_id = user_info.user_id;
    console.log(reciever_id);
    var room_name = getRoomName(reciever_id);
    handleWebSocket(room_name); 
  }

  // Attach click event handler to user elements
  $(".user").click(handleUserClick);

  // Establish WebSocket connection
  //handleWebSocket();
});
