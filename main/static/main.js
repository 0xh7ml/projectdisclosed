const form = document.getElementById('markAsRead');
const baseURL = "http://127.0.0.1:8000/reports/";
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

if (form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const reportId = document.getElementById('report_id').value;
        const reportURL = `${baseURL}${reportId}`;
        
        const options = {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        };

        try {
            const response = await fetch(reportURL, options);
            if (!response.ok) {
                throw new Error('Failed to mark as read');
            }
            await showSuccessMessage();
            location.reload()
        } 
        catch (error) {
            await showErrorMessage();
        }
    });
}

async function showSuccessMessage() {
    await Swal.fire({
        title: 'Congrats!',
        icon: 'success',
        toast: true,
        customClass: {
            popup: 'custom-swal', 
        },
        background: '#28a745',
        position: 'top-end',
        timerProgressBar: true,
        timer: 1000,
        showConfirmButton: false
    });
}

async function showErrorMessage() {
    await Swal.fire({
        title:  'Something Wrong!',
        icon: 'warning',
        toast: true,
        width: '400px',
        customClass: {
            popup: 'custom-swal', 
        },
        background: '#dc3545',
        position: 'top-end',
        timer: 1500,
        timerProgressBar: true,
        showConfirmButton: false
    });
}



document.addEventListener("DOMContentLoaded", function() {
    const cweFilterInput = document.getElementById('cweFilter');
    const severityFilterSelect = document.getElementById('severityFilter');
    const readStatusFilterSelect = document.getElementById('readStatusFilter');

    const filterRows = () => {
        const cweFilter = cweFilterInput.value.trim().toLowerCase();
        const severityFilter = severityFilterSelect.value;
        const readStatusFilter = readStatusFilterSelect.value;

        const rows = document.querySelectorAll('#vulnerabilityTable tbody tr');

        rows.forEach(row => {
            const cwe = row.querySelector('[data-cwe]').getAttribute('data-cwe').toLowerCase();
            const severity = row.querySelector('[data-severity]').getAttribute('data-severity').toLowerCase();
            const readStatus = row.querySelector('[data-read]').getAttribute('data-read');

            const cweMatch = cwe.includes(cweFilter);
            const severityMatch = severity === severityFilter || severityFilter === "";
            const readStatusMatch = readStatus === readStatusFilter || readStatusFilter === "";

            if (cweMatch && severityMatch && readStatusMatch) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    };

    cweFilterInput.addEventListener('input', filterRows);
    severityFilterSelect.addEventListener('change', filterRows);
    readStatusFilterSelect.addEventListener('change', filterRows);
});