set -eux pipefail

sudo systemctl stop unattended-upgrades  # not sure if this is proper but this service holds a lock on the apt cache

apt update -y
apt upgrade -y

apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa

sudo apt update
sudo apt install python3.13 python3.13-venv -y

python3.13 --version
python3.13 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# cool, now we can run the ai model in the dedicated python environment


mkdir -p artifacts/input
mkdir -p artifacts/output

sudo systemctl stop unattended-upgrades  # it's probably proper to just resume this

echo "✅ Provisioning complete"
