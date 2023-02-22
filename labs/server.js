const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {

    myHostName=os.hostname();
    myTotalmem=(os.totalmem()/10000);
    myFreemem=(os.freemem()/10000);
    myUptime=os.uptime();		
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
	<h1>Hello</h1>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${myUptime /86400}, Hours: ${myUptime /2073600}, Minutes: ${myUptime /124416000} </p>
        <p>Total Memory: ${myTotalmem} MB </p>
        <p>Free Memory: ${myFreemem} MB </p>
        <p>Number of CPUs: ${os.cpus().length} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
