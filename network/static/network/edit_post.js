function editPost(postId) {
    document.getElementById(`post-content-${postId}`).style.display = 'none';
    document.getElementById(`edit-area-${postId}`).style.display = 'block';

    document.getElementById(`save-button-${postId}`).style.display = 'inline-block';

    const currentContent = document.getElementById(`post-content-${postId}`).innerText;
    document.getElementById(`edit-area-${postId}`).value = currentContent;
}

function savePost(postId) {
    const newContent = document.getElementById(`edit-area-${postId}`).value;

    fetch(`/edit_post/${postId}/`, {
        method: 'PUT',
        body: JSON.stringify({
            content: newContent
        }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token 
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {

            document.getElementById(`post-content-${postId}`).innerText = newContent;

            document.getElementById(`post-content-${postId}`).style.display = 'block';
            document.getElementById(`edit-area-${postId}`).style.display = 'none';

            document.getElementById(`save-button-${postId}`).style.display = 'none';
        } else if (data.error) {
            alert(data.error);
        }
    });
}
