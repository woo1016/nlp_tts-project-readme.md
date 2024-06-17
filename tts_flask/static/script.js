function synthesizeText() {
    var form = document.getElementById('speechForm');
    var formData = new FormData(form);
    fetch('/synthesize', {
        method: 'POST',
        body: formData
    }).then(response => response.json()).then(data => {
        var audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = data.audio_url;
        audioPlayer.load();
        audioPlayer.play();
    }).catch(error => console.error('Error:', error));
}