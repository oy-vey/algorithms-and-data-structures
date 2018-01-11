clear
$tests = Get-ChildItem -Path ./tests -Exclude *.a 
$answers = Get-ChildItem -Path ./tests/*.a 
for ($i=0; $i -lt $tests.Count; $i++) {
    echo "Test#" $tests[$i].Name
    $Result = type $tests[$i].FullName | python .\check_brackets.py
    $Answer = type $answers[$i].FullName
    
    If ($Result -ne $Answer) {
        echo "Failed" $tests[$i].Name
        echo "Result:" $Result
        echo "Correct answer:" $Answer
    }
    else{
        echo "Success"
    }
    echo "____________________"

}