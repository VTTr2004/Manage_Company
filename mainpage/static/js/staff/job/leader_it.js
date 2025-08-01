const csrftoken = getCookie('csrftoken');

function Action(work) {
    let url = '';
    let id = '';
    let change = '';

    if (work === 'asignWork') {
        url = '/asignWork/';
        id = document.getElementById("id").value;
        change = document.getElementById("id_staf").value;
    } else if (work === 'updateData') {
        url = '/updateData/';
        id = document.getElementById("id").value;
        change = document.getElementById("status").value;
    } else {
        alert("Loại công việc không hợp lệ");
        return;
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            role: 'ld_it',
            id: id,
            change: change
        })
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            alert('Cập nhật thất bại');
        }
    });
}
