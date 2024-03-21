const formName = document.getElementById('markAsRead');
const baseURL = "http://127.0.0.1:8000/reports/";

if (formName) {
    formName.addEventListener('submit', (e) => {
        e.preventDefault();
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const reportId = document.getElementById('report_id').value;

        // Construct report URL
        const report_url = baseURL + reportId;

        // Options for the fetch request
        const options = {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        };
        try {
            // Make the POST request
            const response = fetch(report_url, options);
            Swal.fire({
                title: 'Congrats!',
                icon: 'success',
                toast: true,
                customClass: {
                popup: 'custom-swal', 
                } ,// Apply the custom text color class to the dialog content  
                background: '#28a745',
                position: 'top-end',
                timer: 1500,
                timerProgressBar: true,
                showConfirmButton: false
            }).then(()=>{
                location.reload()
            })
        } catch (error) {
            Swal.fire({
                title:  'Something Wrong!',
                icon: 'warning',
                toast: true,
                width: '400px',
                customClass: {
                popup: 'custom-swal', 
                } ,// Apply the custom text color class to the dialog content  
                background: '#dc3545',
                position: 'top-end',
                timer: 1500,
                timerProgressBar: true,
                showConfirmButton: false
            });
        }
    });
}
