const apiUrl = "http://127.0.0.1:5000";

async function sendRequest(url, method, data = {}) {
    return fetch(url, {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .catch(error => console.error('Error:', error));
}

async function addEmployee() {
    const employeeData = {
        Id: prompt("Enter Employee Id"),
        Name: prompt("Enter Employee Name"),
        Post: prompt("Enter Employee Post"),
        Salary: prompt("Enter Employee Salary"),
    };

    sendRequest(apiUrl + '/add_employee', 'POST', employeeData)
        .then(response => console.log(response));
}

async function removeEmployee() {
    const employeeId = prompt("Enter Employee Id to remove");
    sendRequest(apiUrl + `/remove_employee/${employeeId}`, 'DELETE')
        .then(response => console.log(response));
}

async function promoteEmployee() {
    const employeeId = prompt("Enter Employee Id to promote");
    const amount = prompt("Enter increase in Salary");

    sendRequest(apiUrl + `/promote_employee/${employeeId}`, 'PUT', { amount })
        .then(response => console.log(response));
}

async function displayEmployees() {
    sendRequest(apiUrl + '/display_employees', 'GET')
        .then(response => console.log(response));
}
