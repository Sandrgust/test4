[Unit]
Description=Apache Jmeter server
Documentation=https://jmeter.apache.org/usermanual/remote-test.html
Wants=network-online.target
After=network-online.target

[Service]
LimitNOFILE=10240
Type=simple
Restart=on-failure
RestartSec=180s
WorkingDirectory=/tmp
ExecStart=/opt/jmeter/bin/jmeter-server

[Install]
WantedBy=multi-user.target
