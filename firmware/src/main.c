#include <zephyr/kernel.h>
#include <zephyr/bluetooth/bluetooth.h>

void main(void) {
    // Enable Bluetooth stack
    bt_enable(NULL);
    printk("Bluefi boot complete 🌀💙\n");

    // Keep the firmware alive
    while (1) {
        k_sleep(K_SECONDS(1));
    }
}
