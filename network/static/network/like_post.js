function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrf_token = getCookie('csrftoken');
if (!csrf_token) {
    console.error("No CSRF token found. The request might fail.");
}

function toggleLike(postId) {
    const likeButton = document.getElementById(`like-button-${postId}`);
    const likeCount = document.getElementById(`like-count-${postId}`);
    
    fetch(`/like_post/${postId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token  
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            likeCount.innerText = `${data.likes_count} Likes`;

            if (data.liked) {
                likeButton.innerHTML = '<i class="fas fa-heart"></i>';  
            } else {
                likeButton.innerHTML = '<i class="far fa-heart"></i>';  
            }
        }
    })
    .catch(error => {
        console.error("Error en la solicitud de like/unlike:", error);
    });
}
