export function SummaryText(props){
    return (
    <div className="bg-gray-800 p-4 rounded-lg" style = {{position : "absolute", top : "30%" ,height : "fit-content", width: "70%", overflowY: "auto"}}>
    <p className="text-white">{props.summaryText.data}</p>
    </div>
  )
}