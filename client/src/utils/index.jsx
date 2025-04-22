export function formatCurrency(amount){
    return  new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'COL'
    }).format(amount)
}