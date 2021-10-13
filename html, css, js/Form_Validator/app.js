const form=document.getElementById( 'form' );
const username=document.getElementById( 'username' );
const email=document.getElementById( 'email' );
const password=document.getElementById( 'password' );
const password2=document.getElementById( 'password2' );

function showError ( input, message )
{
    const formControl=input.parentElement;
    formControl.className='form-control error';
    const small=formControl.querySelector( 'small' );
    small.innerText=message;
}

function showSuccess ( input )
{
    const formControl=input.parentElement;
    formControl.className='form-control success';


}

function isValidEmail ( email )
{
    const re=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test( String( email ).toLowerCase() );
}

//Event Listeners
form.addEventListener( 'submit', function ( e )
{
    e.preventDefault();
    // @ts-ignore
    if ( username.value==='' )
    {
        showError( username, 'Username is required' );
    }
    else
    {
        showSuccess( username );
    }
    // @ts-ignore
    if ( email.value==='' )
    {
        showError( email, 'Email is required' );
    }
    else if ( !isValidEmail( email.value ) )
    {
        showError( email, 'Email is not valid' );

    }
    else
    {
        showSuccess( email );
    }
    // @ts-ignore
    if ( password.value==='' )
    {
        showError( password, 'Password is required' );
    }
    else
    {
        showSuccess( password );
    }
    // @ts-ignore
    if ( password2.value==='' )
    {
        showError( password2, 'Password2 is required' );
    }
    else
    {
        showSuccess( password2 );
    }
} );