$(document).ready(function() {
    $('#chatbot-send').on('click', function() {
        sendMessage();
    });

    $('#chatbot-input').on('keypress', function(e) {
        if (e.which == 13) {
            sendMessage();
        }
    });

    $('#chatbot-close').on('click', function() {
        $('#chatbot').hide();
    });

    function sendMessage() {
        var userMessage = $('#chatbot-input').val();
        if (userMessage.trim() !== '') {
            $('#chatbot-messages').append('<div class="message user-message">' + userMessage + '</div>');
            $('#chatbot-input').val('');

            // Simulate a response from the bot
            setTimeout(function() {
                var botMessage = getBotResponse(userMessage);
                $('#chatbot-messages').append('<div class="message bot-message">' + botMessage + '</div>');
                $('#chatbot-messages').scrollTop($('#chatbot-messages')[0].scrollHeight);
            }, 500);
        }
    }

    function getBotResponse(message) {
        var lowerMessage = message.toLowerCase();
        var response = "I'm not sure how to respond to that. Could you please rephrase?";
        
        if (lowerMessage.includes("hello") || lowerMessage.includes("hi")) {
            response = "Hello! How can I assist you today?";
        } else if (lowerMessage.includes("donate")) {
            response = "You can donate blood if you meet the eligibility criteria. Would you like to check your eligibility?";
        } else if (lowerMessage.includes("eligibility")) {
            response = "To check your eligibility, please provide details about your last donation, frequency, and health status.";
        } else if (lowerMessage.includes("thank")) {
            response = "You're welcome! Is there anything else I can help you with?";
        } else if (lowerMessage.includes("bye") || lowerMessage.includes("goodbye")) {
            response = "Goodbye! Have a great day!";
        } else if (lowerMessage.includes("help")) {
            response = "Sure, I'm here to help! What do you need assistance with?";
        } else if (lowerMessage.includes("how are you")) {
            response = "I'm just a bot, but I'm here to assist you! How can I help today?";
        } else if (lowerMessage.includes("blood types")) {
            response = "The main blood types are A, B, AB, and O. Each can be positive or negative. Do you have a specific question about blood types?";
        } else if (lowerMessage.includes("contact")) {
            response = "You can contact us via email at support@blooddonationportal.com or call us at 123-456-7890.";
        } else if (lowerMessage.includes("appointment")) {
            response = "To schedule an appointment, please visit our website or call our office during business hours.";
        } else if (lowerMessage.includes("location")) {
            response = "We have multiple donation centers located throughout the city. Where are you located?";
        } else if (lowerMessage.includes("emergency")) {
            response = "If you have an emergency and need blood urgently, please call emergency services immediately.";
        } else if (lowerMessage.includes("register")) {
            response = "To register as a blood donor, please visit our website or contact our office for assistance.";
        } 
        else if (lowerMessage.includes("name")) {
            response = "My name is MSD. How can I assist you?";
        } else {
            // Add more response options here
            response = "I'm not sure I understand. Can you please provide more details?";
        } 
    
        return response;
    }
    
});
