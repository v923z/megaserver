function connect_callback() {
	var message = create_message('connect', $('#baudrate').val())
	var request = $.ajax({
		url: 'http://127.0.0.1:8080',
		type: 'POST',
		data: JSON.stringify(message, null, 4),
		dataType: 'json'
	})
	
	request.done(function(msg) {
		alert(msg)
	})
}

function create_message(message_type, message_content) {
	var message = new Object()
	message.command = message_type
	message.content = message_content
	return message
}
