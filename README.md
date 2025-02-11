# **Virtual Machines Microservice Deployment Report \- B22CS043**

## **Objective**

This report documents the process of creating and configuring multiple Virtual Machines (VMs) using Oracle VirtualBox, establishing a network between them, and deploying a microservice-based weather application using Flask.

---

## **1\. Installation of VirtualBox**

### **Steps to Install VirtualBox on Host Machine:**

1. Download the latest version of [Oracle VirtualBox](https://www.virtualbox.org/) from the official website.  
2. Install VirtualBox following the standard installation process for your operating system.  
3. (Optional) Download and install the VirtualBox Extension Pack for enhanced functionality. 

---

## **2\. Setting Up Virtual Machines (VMs)**

### **Minimum System Requirements to Run Ubuntu OS**

* **RAM:** 4 GB (per VM)  
* **CPU Cores:** 4 (per VM)  
* **Storage:** 25 GB (per VM)

### **Creating and Configuring Ubuntu VMs**

1. **Create a New VM in VirtualBox:**  
   * Open VirtualBox and click **New**.  
   * Set the name to `Ubuntu-VM1` and choose **Ubuntu (64-bit)**.  
   * Allocate 4 GB of RAM.  
   * Create a **25 GB Virtual Hard Disk**.  
   * Repeat the same process to create `Ubuntu-VM2`.  
2. **Install Ubuntu on Each VM:**  
   * Mount the Ubuntu ISO file and boot the VM.  
   * Follow the installation wizard and complete the OS installation.  
3. Install essential updates and packages after installation:

---

## 

## **3\. Configuring the Network Between VMs**

### **Creating a NAT Network in VirtualBox**

1. Open VirtualBox and navigate to **File \> Preferences \> Network**.  
2. Go to the **NAT Networks** tab and click **Add**.  
3. Set the network name to `Microservice Network` and configure:  
   * **Network CIDR:** `192.168.100.0/24`  
   * Enable **DHCP Server**  
4. Save and close the settings.

### **Assigning VMs to the NAT Network**

1. Open the **Settings** of each VM in VirtualBox.  
2. Go to **Network** and attach **Adapter 1** to `Microservice Network`.  
3. Set the **Adapter Type** to **Intel PRO/1000 MT Desktop**.  
4. Set each VM to have a static IP:  
   * VM1 (Client): `192.168.100.4`  
   * VM2 (Server): `192.168.100.5`

### **Verifying Network Connection**

Run the following command on VM1:

| ping 192.168.100.5 |
| :---- |

If successful, run the reverse check from VM2:

| ping 192.168.100.4 |
| :---- |

---

## **4\. Deploying the Microservice Application**

### **Installing Dependencies on Both VMs**

Run the following on **both** VMs:

| sudo apt install python3 python3-pip \-ypip3 install flask requests |
| :---- |

### **Configuring the Server (VM2 \- `192.168.100.5`)**

1. Create `server.py`:  
2. Run the server.

### **Configuring the Client (VM1 \- `192.168.100.4`)**

1. Create `client.py`:  
2. Run the client.

### **Testing the Application**

Open a browser and navigate to:  
 http://192.168.100.4:5000/

1. Enter a city name and get weather data fetched from VM2.


## **5\. Architecture Design**

Below is a simple diagram representing the connection between VMs:



---

## **7\. Additional Resources**

* [GitHub Repository (Source Code)](https://github.com/your_repo)  
* [Video Demo (Setup & Deployment)](https://your_video_link/)

---

## **Conclusion**

Successfully deployed a microservice-based Flask weather app across two VirtualBox VMs using a NAT network, resolving connectivity and API issues along the way.

