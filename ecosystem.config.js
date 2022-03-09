module.exports = {
  apps : [
    {
      name: "DA508",
      script: "./start.sh",
      interpreter: '/usr/bin/bash',
      watch: ["./admin_interface"]
    }
  ],
};
