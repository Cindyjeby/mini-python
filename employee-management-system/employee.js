const apiUrl = "http://127.0.0.1:5000";

async function sendRequest(url, method, data = {}) {
    try {
        const response = await fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const responseData = await response.json();
        return { success: true, data: responseData };
    } catch (error) {
        console.error('Error:', error);
        return { success: false, error: error.message || 'Unknown error' };
    }
}

async function addEmployee() {
    try {
        const employeeData = {
            Id: prompt("Enter Employee Id"),
            Name: prompt("Enter Employee Name"),
            Post: prompt("Enter Employee Post"),
            Salary: prompt("Enter Employee Salary"),
        };

        const response = await sendRequest(apiUrl + '/add_employee', 'POST', employeeData);

        if (response.success) {
            console.log("Employee added successfully");
        } else {
            console.error('Error:', response.error);
        }
    } catch (error) {
        console.error('Unexpected error:', error);
    }
}

async function removeEmployee() {
    try {
        const employeeId = prompt("Enter Employee Id to remove");
        const response = await sendRequest(apiUrl + `/remove_employee/${employeeId}`, 'DELETE');

        if (response.success) {
            console.log("Employee removed successfully");
        } else {
            console.error('Error:', response.error);
        }
    } catch (error) {
        console.error('Unexpected error:', error);
    }
}

async function promoteEmployee() {
    try {
        const employeeId = prompt("Enter Employee Id to promote");
        const amount = prompt("Enter increase in Salary");

        const response = await sendRequest(apiUrl + `/promote_employee/${employeeId}`, 'PUT', { amount });

        if (response.success) {
            console.log("Employee promoted successfully");
        } else {
            console.error('Error:', response.error);
        }
    } catch (error) {
        console.error('Unexpected error:', error);
    }
}

async function displayEmployees() {
    try {
        const response = await sendRequest(apiUrl + '/display_employees', 'GET');

        if (response.success) {
            console.log("Employees retrieved successfully:", response.data);
        } else {
            console.error('Error:', response.error);
        }
    } catch (error) {
        console.error('Unexpected error:', error);
    }
}
