
function login() {
    document.getElementById("card").style.display="none"
    if (!validation(document.getElementById("password").value,document.getElementById("userName").value))
    {document.getElementById("cardTitle").innerText="Validation Error"
        document.getElementById("cardText").innerText="all fields are required "
        document.getElementById("card").style.display="block"
        return}

    const data = { username: document.getElementById("userName").value,
        password:document.getElementById("password").value };
    fetch('http://127.0.0.1:8000/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            if (data.token){
                localStorage.setItem("NotificationTaskToken",data.token)
                localStorage.setItem("NotificationTaskUserId",data.userId)
                window.open("Notification.html","_self")
                document.getElementById("signInForm").style.display="none"
                }
            else if (data.non_field_errors){
                document.getElementById("card").style.display="block"
                document.getElementById("cardTitle").innerText="error while signing in"
                document.getElementById("cardText").innerText=data.non_field_errors
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById("card").style.display="block"
            document.getElementById("cardTitle").innerText="error while signing in"
            document.getElementById("cardText").innerText=error
        });

}
function validation(password,userName){

    if (password==""||userName=="")
    {
    return false
    }
    return true
}
function SignUp(){
    document.getElementById("cardSU").style.display="none"
    if (!validation(document.getElementById("passwordSU").value,document.getElementById("userNameSU").value))
    { document.getElementById("cardTitleSU").innerText="Validation Error"
    document.getElementById("cardTextSU").innerText="all fields are required "
    document.getElementById("cardSU").style.display="block"
    return}
    const data = { username: document.getElementById("userNameSU").value,
        password:document.getElementById("passwordSU").value };
    fetch('http://127.0.0.1:8000/auth/signUp/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
             },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success){
            alert(data.message);
            location.reload();}
            else if (!data.success){
                document.getElementById("cardSU").style.display="block"
                document.getElementById("cardTitleSU").innerText="error while signing up"
                document.getElementById("cardTextSU").innerText=data.errors
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById("cardSU").style.display="block"
            document.getElementById("cardTitleSU").innerText="error while signing up"
            document.getElementById("cardTextSU").innerText=error
        });


}
