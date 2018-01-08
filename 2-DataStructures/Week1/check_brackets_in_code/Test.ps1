clear
$tests = Get-ChildItem -Path ./tests -Exclude *.a 
$answers = Get-ChildItem -Path ./tests/*.a 
for ($i=0; $i -lt $tests.Count; $i++) {
    echo "_____________________"
    echo $tests[$i].FullName
    echo "Result: "
    type $tests[$i].FullName | python .\check_brackets.py
    echo "Correct Answer: "
    type $answers[$i].FullName
    echo "_____________________"

}