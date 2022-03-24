echo "INFO - Some JMeter prepare steps..."
ls -la

echo "INFO - Running JMeter..."
jmeter -n -t jmetr/test.jmx -Jhost=ya.ru -l index.html -e -o ./jmeter_report

echo "DEBUG - Some steps to prepare reports..."

echo "DEBUG - view files in ./jmeter_report:"
ls -la ./jmeter_report
echo "INFO - Report's data files are prepared to publish"
