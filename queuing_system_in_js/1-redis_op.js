import redis from "redis";

const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
