# pix4_parameter_reference
> 使用gpt翻译pix4的参数，并且加上gpt的解释

> https://docs.px4.io/main/zh/advanced_config/parameter_reference.html

501. BAT1_V_CHANNEL (INT32)
- 名称：BAT1_V_CHANNEL (INT32)
- 参数描述：Battery 1 Voltage ADC Channel Comment: This parameter specifies the ADC channel used to monitor voltage of main power battery. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


502. BAT1_V_CHARGED (FLOAT)
- 名称：BAT1_V_CHARGED (FLOAT)
- 参数描述：Full cell voltage (5C load) Comment: Defines the voltage where a single cell of battery 1 is considered full under a mild load. This will never be the nominal voltage of 4.2V Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`4.05`
- 单位：`V`


503. BAT1_V_DIV (FLOAT)
- 名称：BAT1_V_DIV (FLOAT)
- 参数描述：Battery 1 voltage divider (V divider) Comment: This is the divider from battery 1 voltage to ADC voltage. If using e.g. Mauch power modules the value from the datasheet can be applied straight here. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1.0`
- 单位：``


504. BAT1_V_EMPTY (FLOAT)
- 名称：BAT1_V_EMPTY (FLOAT)
- 参数描述：Empty cell voltage (5C load) Comment: Defines the voltage where a single cell of battery 1 is considered empty. The voltage should be chosen before the steep dropoff to 2.8V. A typical lithium battery can only be discharged down to 10% before it drops off to a voltage level damaging the cells. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`3.6`
- 单位：`V`


505. BAT1_V_LOAD_DROP (FLOAT)
- 名称：BAT1_V_LOAD_DROP (FLOAT)
- 参数描述：Voltage drop per cell on full throttle Comment: This implicitly defines the internal resistance to maximum current ratio for battery 1 and assumes linearity. A good value to use is the difference between the 5C and 20-25C load. Not used if BAT1_R_INTERNAL is set. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.07, 0.5] (0.01)`
- 默认值：`0.1`
- 单位：`V`


506. BAT2_A_PER_V (FLOAT)
- 名称：BAT2_A_PER_V (FLOAT)
- 参数描述：Battery 2 current per volt (A/V) Comment: The voltage seen by the ADC multiplied by this factor will determine the battery current. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1.0`
- 单位：``


507. BAT2_CAPACITY (FLOAT)
- 名称：BAT2_CAPACITY (FLOAT)
- 参数描述：Battery 2 capacity Comment: Defines the capacity of battery 2 in mAh. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 100000] (50)`
- 默认值：`-1.0`
- 单位：`mAh`


508. BAT2_I_CHANNEL (INT32)
- 名称：BAT2_I_CHANNEL (INT32)
- 参数描述：Battery 2 Current ADC Channel Comment: This parameter specifies the ADC channel used to monitor current of main power battery. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


509. BAT2_N_CELLS (INT32)
- 名称：BAT2_N_CELLS (INT32)
- 参数描述：Number of cells for battery 2 Comment: Defines the number of cells the attached battery consists of. 参数对照:0: Unknown 1: 1S Battery 2: 2S Battery 3: 3S Battery 4: 4S Battery 5: 5S Battery 6: 6S Battery 7: 7S Battery 8: 8S Battery 9: 9S Battery 10: 10S Battery 11: 11S Battery 12: 12S Battery 13: 13S Battery 14: 14S Battery 15: 15S Battery 16: 16S Battery Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


510. BAT2_R_INTERNAL (FLOAT)
- 名称：BAT2_R_INTERNAL (FLOAT)
- 参数描述：Explicitly defines the per cell internal resistance for battery 2 Comment: If non-negative, then this will be used in place of BAT2_V_LOAD_DROP for all calculations. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 0.2] (0.0005)`
- 默认值：`0.005`
- 单位：`欧姆`


511. BAT2_SOURCE (INT32)
- 名称：BAT2_SOURCE (INT32)
- 参数描述：Battery 2 monitoring source Comment: This parameter controls the source of battery data. The value 'Power Module' means that measurements are expected to come from a power module. If the value is set to 'External' then the system expects to receive mavlink battery status messages. If the value is set to 'ESCs', the battery information are taken from the esc_status message. This requires the ESC to provide both voltage as well as current. 参数对照:-1: Disabled 0: Power Module 1: External 2: ESCs Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


512. BAT2_V_CHANNEL (INT32)
- 名称：BAT2_V_CHANNEL (INT32)
- 参数描述：Battery 2 Voltage ADC Channel Comment: This parameter specifies the ADC channel used to monitor voltage of main power battery. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


513. BAT2_V_CHARGED (FLOAT)
- 名称：BAT2_V_CHARGED (FLOAT)
- 参数描述：Full cell voltage (5C load) Comment: Defines the voltage where a single cell of battery 1 is considered full under a mild load. This will never be the nominal voltage of 4.2V Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`4.05`
- 单位：`V`


514. BAT2_V_DIV (FLOAT)
- 名称：BAT2_V_DIV (FLOAT)
- 参数描述：Battery 2 voltage divider (V divider) Comment: This is the divider from battery 2 voltage to ADC voltage. If using e.g. Mauch power modules the value from the datasheet can be applied straight here. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1.0`
- 单位：``


515. BAT2_V_EMPTY (FLOAT)
- 名称：BAT2_V_EMPTY (FLOAT)
- 参数描述：Empty cell voltage (5C load) Comment: Defines the voltage where a single cell of battery 1 is considered empty. The voltage should be chosen before the steep dropoff to 2.8V. A typical lithium battery can only be discharged down to 10% before it drops off to a voltage level damaging the cells. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`3.6`
- 单位：`V`


516. BAT2_V_LOAD_DROP (FLOAT)
- 名称：BAT2_V_LOAD_DROP (FLOAT)
- 参数描述：Voltage drop per cell on full throttle Comment: This implicitly defines the internal resistance to maximum current ratio for battery 1 and assumes linearity. A good value to use is the difference between the 5C and 20-25C load. Not used if BAT2_R_INTERNAL is set. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.07, 0.5] (0.01)`
- 默认值：`0.1`
- 单位：`V`


517. BAT_ADC_CHANNEL (INT32)
- 名称：BAT_ADC_CHANNEL (INT32)
- 参数描述：This parameter is deprecated. Please use BAT1_I_CHANNEL
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


518. BAT_AVRG_CURRENT (FLOAT)
- 名称：BAT_AVRG_CURRENT (FLOAT)
- 参数描述：Expected battery current in flight Comment: This value is used to initialize the in-flight average current estimation, which in turn is used for estimating remaining flight time and RTL triggering.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 500] (0.1)`
- 默认值：`15.0`
- 单位：`A`


519. BAT_CRIT_THR (FLOAT)
- 名称：BAT_CRIT_THR (FLOAT)
- 参数描述：Critical threshold Comment: Sets the threshold when the battery will be reported as critically low. This has to be lower than the low threshold. This threshold commonly will trigger RTL.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 0.25] (0.01)`
- 默认值：`0.07`
- 单位：`norm`


520. BAT_EMERGEN_THR (FLOAT)
- 名称：BAT_EMERGEN_THR (FLOAT)
- 参数描述：Emergency threshold Comment: Sets the threshold when the battery will be reported as dangerously low. This has to be lower than the critical threshold. This threshold commonly will trigger landing.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.03, 0.1] (0.01)`
- 默认值：`0.05`
- 单位：`norm`


521. BAT_LOW_THR (FLOAT)
- 名称：BAT_LOW_THR (FLOAT)
- 参数描述：Low threshold Comment: Sets the threshold when the battery will be reported as low. This has to be higher than the critical threshold.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.12, 0.5] (0.01)`
- 默认值：`0.15`
- 单位：`norm`


522. BAT_N_CELLS (INT32)
- 名称：BAT_N_CELLS (INT32)
- 参数描述：This parameter is deprecated. Please use BAT1_N_CELLS instead
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`3`
- 单位：``


523. BAT_V_CHARGED (FLOAT)
- 名称：BAT_V_CHARGED (FLOAT)
- 参数描述：This parameter is deprecated. Please use BAT1_V_CHARGED instead
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4.05`
- 单位：``


524. BAT_V_EMPTY (FLOAT)
- 名称：BAT_V_EMPTY (FLOAT)
- 参数描述：This parameter is deprecated. Please use BAT1_V_EMPTY instead
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`3.6`
- 单位：``


525. BAT_V_LOAD_DROP (FLOAT)
- 名称：BAT_V_LOAD_DROP (FLOAT)
- 参数描述：This parameter is deprecated. Please use BAT1_V_LOAD_DROP instead
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.3`
- 单位：``


526. BAT_V_OFFS_CURR (FLOAT)
- 名称：BAT_V_OFFS_CURR (FLOAT)
- 参数描述：Offset in volt as seen by the ADC input of the current sensor Comment: This offset will be subtracted before calculating the battery current based on the voltage.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


527. CAM_CAP_DELAY (FLOAT)
- 名称：CAM_CAP_DELAY (FLOAT)
- 参数描述：Camera strobe delay Comment: This parameter sets the delay between image integration start and strobe firing
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：`ms`


528. CAM_CAP_EDGE (INT32)
- 名称：CAM_CAP_EDGE (INT32)
- 参数描述：Camera capture edge  Values:0: Falling edge 1: Rising edge Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


529. CAM_CAP_FBACK (INT32)
- 名称：CAM_CAP_FBACK (INT32)
- 参数描述：Camera capture feedback Comment: Enables camera capture feedback Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


530. CAM_CAP_MODE (INT32)
- 名称：CAM_CAP_MODE (INT32)
- 参数描述：Camera capture timestamping mode Comment: Change time measurement 参数对照:0: Get absolute timestamp 1: Get timestamp of mid exposure (active high) 2: Get timestamp of mid exposure (active low) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


531. TRIG_ACT_TIME (FLOAT)
- 名称：TRIG_ACT_TIME (FLOAT)
- 参数描述：Camera trigger activation time Comment: This parameter sets the time the trigger needs to pulled high or low. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 3000]`
- 默认值：`40.0`
- 单位：`ms`


532. TRIG_DISTANCE (FLOAT)
- 名称：TRIG_DISTANCE (FLOAT)
- 参数描述：Camera trigger distance Comment: Sets the distance at which to trigger the camera. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (1)`
- 默认值：`25.0`
- 单位：`m`


533. TRIG_INTERFACE (INT32)
- 名称：TRIG_INTERFACE (INT32)
- 参数描述：Camera trigger Interface Comment: Selects the trigger interface 参数对照:1: GPIO 2: Seagull MAP2 (over PWM) 3: MAVLink (forward via MAV_CMD_IMAGE_START_CAPTURE) 4: Generic PWM (IR trigger, servo) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4`
- 单位：``


534. TRIG_INTERVAL (FLOAT)
- 名称：TRIG_INTERVAL (FLOAT)
- 参数描述：Camera trigger interval Comment: This parameter sets the time between two consecutive trigger events Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[4.0, 10000.0]`
- 默认值：`40.0`
- 单位：`ms`


535. TRIG_MIN_INTERVA (FLOAT)
- 名称：TRIG_MIN_INTERVA (FLOAT)
- 参数描述：Minimum camera trigger interval Comment: This parameter sets the minimum time between two consecutive trigger events the specific camera setup is supporting. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10000.0]`
- 默认值：`1.0`
- 单位：`ms`


536. TRIG_MODE (INT32)
- 名称：TRIG_MODE (INT32)
- 参数描述：Camera trigger mode  Values:0: Disable 1: Time based, on command 2: Time based, always on 3: Distance based, always on 4: Distance based, on command (Survey mode) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`0`
- 单位：``


537. TRIG_POLARITY (INT32)
- 名称：TRIG_POLARITY (INT32)
- 参数描述：Camera trigger polarity Comment: This parameter sets the polarity of the trigger (0 = active low, 1 = active high ) 参数对照:0: Active low 1: Active high Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


538. TRIG_PWM_NEUTRAL (INT32)
- 名称：TRIG_PWM_NEUTRAL (INT32)
- 参数描述：PWM neutral output on trigger pin    Reboot required: true
  - 翻译：触发引脚上的 PWM 中位值    需要重启: true
  - gpt注解：TRIG_PWM_NEUTRAL 参数用于指定触发引脚上的 PWM 中位值。设置此参数后需要重新启动飞行控制器。
- `[Min, Max]`：`[1000, 2000]`
- 默认值：`1500`
- 单位：`µs`


539. TRIG_PWM_SHOOT (INT32)
- 名称：TRIG_PWM_SHOOT (INT32)
- 参数描述：PWM output to trigger shot    Reboot required: true
  - 翻译：用于触发射击的 PWM 输出    需要重启: true
  - gpt注解：TRIG_PWM_SHOOT 参数用于指定触发射击的 PWM 输出。设置此参数后需要重新启动飞行控制器。
- `[Min, Max]`：`[1000, 2000]`
- 默认值：`1900`
- 单位：`µs`


540. CBRK_AIRSPD_CHK (INT32)
- 名称：CBRK_AIRSPD_CHK (INT32)
- 参数描述：Circuit breaker for airspeed sensor Comment: Setting this parameter to 162128 will disable the check for an airspeed sensor. The sensor driver will not be started and it cannot be calibrated. WARNING: ENABLING THIS CIRCUIT BREAKER IS AT OWN RISK Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 162128]`
- 默认值：`0`
- 单位：``


541. CBRK_BUZZER (INT32)
- 名称：CBRK_BUZZER (INT32)
- 参数描述：Circuit breaker for disabling buzzer Comment: Setting this parameter to 782097 will disable the buzzer audio notification. Setting this parameter to 782090 will disable the startup tune, while keeping all others enabled. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 782097]`
- 默认值：`0`
- 单位：``


542. CBRK_FLIGHTTERM (INT32)
- 名称：CBRK_FLIGHTTERM (INT32)
- 参数描述：Circuit breaker for flight termination Comment: Setting this parameter to 121212 will disable the flight termination action if triggered by the FailureDetector logic or if FMU is lost. This circuit breaker does not affect the RC loss, data link loss, geofence, and takeoff failure detection safety logic. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 121212]`
- 默认值：`121212`
- 单位：``


543. CBRK_IO_SAFETY (INT32)
- 名称：CBRK_IO_SAFETY (INT32)
- 参数描述：Circuit breaker for IO safety Comment: Setting this parameter to 22027 will disable IO safety. WARNING: ENABLING THIS CIRCUIT BREAKER IS AT OWN RISK
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 22027]`
- 默认值：`22027`
- 单位：``


544. CBRK_SUPPLY_CHK (INT32)
- 名称：CBRK_SUPPLY_CHK (INT32)
- 参数描述：Circuit breaker for power supply check Comment: Setting this parameter to 894281 will disable the power valid checks in the commander. WARNING: ENABLING THIS CIRCUIT BREAKER IS AT OWN RISK
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 894281]`
- 默认值：`0`
- 单位：``


545. CBRK_USB_CHK (INT32)
- 名称：CBRK_USB_CHK (INT32)
- 参数描述：Circuit breaker for USB link check Comment: Setting this parameter to 197848 will disable the USB connected checks in the commander, setting it to 0 keeps them enabled (recommended). We are generally recommending to not fly with the USB link connected and production vehicles should set this parameter to zero to prevent users from flying USB powered. However, for R&D purposes it has proven over the years to work just fine.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 197848]`
- 默认值：`197848`
- 单位：``


546. CBRK_VTOLARMING (INT32)
- 名称：CBRK_VTOLARMING (INT32)
- 参数描述：Circuit breaker for arming in fixed-wing mode check Comment: Setting this parameter to 159753 will enable arming in fixed-wing mode for VTOLs. WARNING: ENABLING THIS CIRCUIT BREAKER IS AT OWN RISK
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 159753]`
- 默认值：`0`
- 单位：``


547. COM_ACT_FAIL_ACT (INT32)
- 名称：COM_ACT_FAIL_ACT (INT32)
- 参数描述：Set the actuator failure failsafe mode Comment: Note: actuator failure needs to be enabled and configured via FD_ACT_* parameters. 参数对照:0: Warning only 1: Hold mode 2: Land mode 3: Return mode 4: Terminate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0`
- 单位：``


548. COM_ARMABLE (INT32)
- 名称：COM_ARMABLE (INT32)
- 参数描述：Flag to allow arming Comment: Set 0 to prevent accidental use of the vehicle e.g. for safety or maintenance reasons. 参数对照:0: Disallow arming 1: Allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


549. COM_ARM_AUTH_ID (INT32)
- 名称：COM_ARM_AUTH_ID (INT32)
- 参数描述：Arm authorizer system id Comment: Used if arm authorization is requested by COM_ARM_AUTH_REQ.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`10`
- 单位：``


550. COM_ARM_AUTH_MET (INT32)
- 名称：COM_ARM_AUTH_MET (INT32)
- 参数描述：Arm authorization method Comment: Methods: - one arm: request authorization and arm when authorization is received - two step arm: 1st arm command request an authorization and 2nd arm command arm the drone if authorized Used if arm authorization is requested by COM_ARM_AUTH_REQ. 参数对照:0: one arm 1: two step arm
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


551. COM_ARM_AUTH_REQ (INT32)
- 名称：COM_ARM_AUTH_REQ (INT32)
- 参数描述：Require arm authorization to arm Comment: By default off. The default allows to arm the vehicle without a arm authorization.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


552. COM_ARM_AUTH_TO (FLOAT)
- 名称：COM_ARM_AUTH_TO (FLOAT)
- 参数描述：Arm authorization timeout Comment: Timeout for authorizer answer. Used if arm authorization is requested by COM_ARM_AUTH_REQ.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.1)`
- 默认值：`1`
- 单位：`s`


553. COM_ARM_BAT_MIN (FLOAT)
- 名称：COM_ARM_BAT_MIN (FLOAT)
- 参数描述：Minimum battery level for arming Comment: Additional battery level check that only allows arming if the state of charge of the emptiest connected battery is above this value. A value of 0 disables the check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.9] (0.01)`
- 默认值：`0.`
- 单位：`norm`


554. COM_ARM_CHK_ESCS (INT32)
- 名称：COM_ARM_CHK_ESCS (INT32)
- 参数描述：Enable checks on ESCs that report telemetry Comment: If this parameter is set, the system will check ESC's online status and failures. This param is specific for ESCs reporting status. It shall be used only if ESCs support telemetry.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


555. COM_ARM_EKF_HGT (FLOAT)
- 名称：COM_ARM_EKF_HGT (FLOAT)
- 参数描述：Maximum EKF height innovation test ratio that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.05)`
- 默认值：`1.0`
- 单位：``


556. COM_ARM_EKF_POS (FLOAT)
- 名称：COM_ARM_EKF_POS (FLOAT)
- 参数描述：Maximum EKF position innovation test ratio that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.05)`
- 默认值：`0.5`
- 单位：``


557. COM_ARM_EKF_VEL (FLOAT)
- 名称：COM_ARM_EKF_VEL (FLOAT)
- 参数描述：Maximum EKF velocity innovation test ratio that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.05)`
- 默认值：`0.5`
- 单位：``


558. COM_ARM_EKF_YAW (FLOAT)
- 名称：COM_ARM_EKF_YAW (FLOAT)
- 参数描述：Maximum EKF yaw innovation test ratio that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.05)`
- 默认值：`0.5`
- 单位：``


559. COM_ARM_HFLT_CHK (INT32)
- 名称：COM_ARM_HFLT_CHK (INT32)
- 参数描述：Enable FMU SD card hardfault detection check Comment: This check detects if there are hardfault files present on the SD card. If so, and the parameter is enabled, arming is prevented.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


560. COM_ARM_IMU_ACC (FLOAT)
- 名称：COM_ARM_IMU_ACC (FLOAT)
- 参数描述：Maximum accelerometer inconsistency between IMU units that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.05)`
- 默认值：`0.7`
- 单位：`m/s^2`


561. COM_ARM_IMU_GYR (FLOAT)
- 名称：COM_ARM_IMU_GYR (FLOAT)
- 参数描述：Maximum rate gyro inconsistency between IMU units that will allow arming
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.02, 0.3] (0.01)`
- 默认值：`0.25`
- 单位：`rad/s`


562. COM_ARM_MAG_ANG (INT32)
- 名称：COM_ARM_MAG_ANG (INT32)
- 参数描述：Maximum magnetic field inconsistency between units that will allow arming Comment: Set -1 to disable the check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[3, 180]`
- 默认值：`60`
- 单位：`deg`


563. COM_ARM_MAG_STR (INT32)
- 名称：COM_ARM_MAG_STR (INT32)
- 参数描述：Enable mag strength preflight check Comment: Check if the estimator detects a strong magnetic disturbance (check enabled by EKF2_MAG_CHECK) 参数对照:0: Disabled 1: Deny arming 2: Warning only
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


564. COM_ARM_MIS_REQ (INT32)
- 名称：COM_ARM_MIS_REQ (INT32)
- 参数描述：Require valid mission to arm Comment: The default allows to arm the vehicle without a valid mission.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


565. COM_ARM_ODID (INT32)
- 名称：COM_ARM_ODID (INT32)
- 参数描述：Enable Drone ID system detection and health check Comment: This check detects if the Open Drone ID system is missing. Depending on the value of the parameter, the check can be disabled, warn only or deny arming. 参数对照:0: Disabled 1: Warning only 2: Enforce Open Drone ID system presence
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


566. COM_ARM_SDCARD (INT32)
- 名称：COM_ARM_SDCARD (INT32)
- 参数描述：Enable FMU SD card detection check Comment: This check detects if the FMU SD card is missing. Depending on the value of the parameter, the check can be disabled, warn only or deny arming. 参数对照:0: Disabled 1: Warning only 2: Enforce SD card presence
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


567. COM_ARM_SWISBTN (INT32)
- 名称：COM_ARM_SWISBTN (INT32)
- 参数描述：Arm switch is a momentary button Comment: 0: Arming/disarming triggers on switch transition. 1: Arming/disarming triggers when holding the momentary button down for COM_RC_ARM_HYST like the stick gesture.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


568. COM_ARM_WO_GPS (INT32)
- 名称：COM_ARM_WO_GPS (INT32)
- 参数描述：Allow arming without GPS  Values:0: Require GPS lock to arm 1: Allow arming without GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


569. COM_CPU_MAX (FLOAT)
- 名称：COM_CPU_MAX (FLOAT)
- 参数描述：Maximum allowed CPU load to still arm Comment: A negative value disables the check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 100] (1)`
- 默认值：`95.0`
- 单位：`%`


570. COM_DISARM_LAND (FLOAT)
- 名称：COM_DISARM_LAND (FLOAT)
- 参数描述：Time-out for auto disarm after landing Comment: A non-zero, positive value specifies the time-out period in seconds after which the vehicle will be automatically disarmed in case a landing situation has been detected during this period. A zero or negative value means that automatic disarming triggered by landing detection is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.1)`
- 默认值：`2.0`
- 单位：`s`


571. COM_DISARM_PRFLT (FLOAT)
- 名称：COM_DISARM_PRFLT (FLOAT)
- 参数描述：Time-out for auto disarm if not taking off Comment: A non-zero, positive value specifies the time in seconds, within which the vehicle is expected to take off after arming. In case the vehicle didn't takeoff within the timeout it disarms again. A negative value disables autmoatic disarming triggered by a pre-takeoff timeout.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.1)`
- 默认值：`10.0`
- 单位：`s`


572. COM_DL_LOSS_T (INT32)
- 名称：COM_DL_LOSS_T (INT32)
- 参数描述：GCS connection loss time threshold Comment: After this amount of seconds without datalink, the GCS connection lost mode triggers
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[5, 300] (1)`
- 默认值：`10`
- 单位：`s`


573. COM_FAIL_ACT_T (FLOAT)
- 名称：COM_FAIL_ACT_T (FLOAT)
- 参数描述：Delay between failsafe condition triggered and failsafe reaction Comment: Before entering failsafe (RTL, Land, Hold), wait COM_FAIL_ACT_T seconds in Hold mode for the user to realize. During that time the user cannot take over control via the stick override feature (see COM_RC_OVERRIDE). Afterwards the configured failsafe action is triggered and the user may use stick override. A zero value disables the delay and the user cannot take over via stick movements (switching modes is still allowed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 25.0]`
- 默认值：`5.`
- 单位：`s`


574. COM_FLIGHT_UUID (INT32)
- 名称：COM_FLIGHT_UUID (INT32)
- 参数描述：Next flight UUID Comment: This number is incremented automatically after every flight on disarming in order to remember the next flight UUID. The first flight is 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0`
- 单位：``


575. COM_FLTMODE1 (INT32)
- 名称：COM_FLTMODE1 (INT32)
- 参数描述：First flightmode slot (1000-1160) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


576. COM_FLTMODE2 (INT32)
- 名称：COM_FLTMODE2 (INT32)
- 参数描述：Second flightmode slot (1160-1320) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


577. COM_FLTMODE3 (INT32)
- 名称：COM_FLTMODE3 (INT32)
- 参数描述：Third flightmode slot (1320-1480) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


578. COM_FLTMODE4 (INT32)
- 名称：COM_FLTMODE4 (INT32)
- 参数描述：Fourth flightmode slot (1480-1640) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


579. COM_FLTMODE5 (INT32)
- 名称：COM_FLTMODE5 (INT32)
- 参数描述：Fifth flightmode slot (1640-1800) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


580. COM_FLTMODE6 (INT32)
- 名称：COM_FLTMODE6 (INT32)
- 参数描述：Sixth flightmode slot (1800-2000) Comment: If the main switch channel is in this range the selected flight mode will be applied. 参数对照:-1: Unassigned 0: Manual 1: Altitude 2: Position 3: Mission 4: Hold 5: Return 6: Acro 7: Offboard 8: Stabilized 10: Takeoff 11: Land 12: Follow Me 13: Precision Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


581. COM_FLT_PROFILE (INT32)
- 名称：COM_FLT_PROFILE (INT32)
- 参数描述：User Flight Profile Comment: Describes the intended use of the vehicle. Can be used by ground control software or log post processing. This param does not influence the behavior within the firmware. This means for example the control logic is independent of the setting of this param (but depends on other params). 参数对照:0: Default 100: Pro User 200: Flight Tester 300: Developer
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


582. COM_FLT_TIME_MAX (INT32)
- 名称：COM_FLT_TIME_MAX (INT32)
- 参数描述：Maximum allowed flight time Comment: The vehicle aborts the current operation and returns to launch when the time since takeoff is above this value. It is not possible to resume the mission or switch to any auto mode other than RTL or Land. Taking over in any manual mode is still possible. Starting from 90% of the maximum flight time, a warning message will be sent every 1 minute with the remaining time until automatic RTL. Set to -1 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, ?]`
- 默认值：`-1`
- 单位：`s`


583. COM_FORCE_SAFETY (INT32)
- 名称：COM_FORCE_SAFETY (INT32)
- 参数描述：Enable force safety Comment: Force safety when the vehicle disarms
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


584. COM_HLDL_LOSS_T (INT32)
- 名称：COM_HLDL_LOSS_T (INT32)
- 参数描述：High Latency Datalink loss time threshold Comment: After this amount of seconds without datalink the data link lost mode triggers
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[60, 3600]`
- 默认值：`120`
- 单位：`s`


585. COM_HLDL_REG_T (INT32)
- 名称：COM_HLDL_REG_T (INT32)
- 参数描述：High Latency Datalink regain time threshold Comment: After a data link loss: after this number of seconds with a healthy datalink the 'datalink loss' flag is set back to false
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 60]`
- 默认值：`0`
- 单位：`s`


586. COM_HOME_EN (INT32)
- 名称：COM_HOME_EN (INT32)
- 参数描述：Home position enabled Comment: Set home position automatically if possible. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


587. COM_HOME_IN_AIR (INT32)
- 名称：COM_HOME_IN_AIR (INT32)
- 参数描述：Allows setting the home position after takeoff Comment: If set to true, the autopilot is allowed to set its home position after takeoff The true home position is back-computed if a local position is estimate if available. If no local position is available, home is set to the current position.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


588. COM_IMB_PROP_ACT (INT32)
- 名称：COM_IMB_PROP_ACT (INT32)
- 参数描述：Imbalanced propeller failsafe mode Comment: Action the system takes when an imbalanced propeller is detected by the failure detector. See also FD_IMB_PROP_THR to set the failure threshold. 参数对照:-1: Disabled 0: Warning 1: Return 2: Land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(1)`
- 默认值：`0`
- 单位：``


589. COM_KILL_DISARM (FLOAT)
- 名称：COM_KILL_DISARM (FLOAT)
- 参数描述：Timeout value for disarming when kill switch is engaged
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 30.0] (0.1)`
- 默认值：`5.0`
- 单位：`s`


590. COM_LKDOWN_TKO (FLOAT)
- 名称：COM_LKDOWN_TKO (FLOAT)
- 参数描述：Timeout for detecting a failure after takeoff Comment: A non-zero, positive value specifies the timeframe in seconds within failure detector is allowed to disarm the vehicle if attitude exceeds the limits defined in FD_FAIL_P and FD_FAIL_R. The check is not executed for flight modes that do support acrobatic maneuvers, e.g: Acro (MC/FW) and Manual (FW). A zero or negative value means that the check is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 5.0]`
- 默认值：`3.0`
- 单位：`s`


591. COM_LOW_BAT_ACT (INT32)
- 名称：COM_LOW_BAT_ACT (INT32)
- 参数描述：Battery failsafe mode Comment: Action the system takes at critical battery. See also BAT_CRIT_THR and BAT_EMERGEN_THR for definition of battery states. 参数对照:0: Warning 2: Land mode 3: Return at critical level, land at emergency level
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


592. COM_MOT_TEST_EN (INT32)
- 名称：COM_MOT_TEST_EN (INT32)
- 参数描述：Enable Actuator Testing Comment: If set, enables the actuator test interface via MAVLink (ACTUATOR_TEST), that allows spinning the motors and moving the servos for testing purposes.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


593. COM_OBC_LOSS_T (FLOAT)
- 名称：COM_OBC_LOSS_T (FLOAT)
- 参数描述：Time-out to wait when onboard computer connection is lost before warning about loss connection
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 60] (0.01)`
- 默认值：`5.0`
- 单位：`s`


594. COM_OBL_RC_ACT (INT32)
- 名称：COM_OBL_RC_ACT (INT32)
- 参数描述：Set offboard loss failsafe mode Comment: The offboard loss failsafe will only be entered after a timeout, set by COM_OF_LOSS_T in seconds. 参数对照:0: Position mode 1: Altitude mode 2: Manual 3: Return mode 4: Land mode 5: Hold mode 6: Terminate 7: Disarm
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


595. COM_OBS_AVOID (INT32)
- 名称：COM_OBS_AVOID (INT32)
- 参数描述：Flag to enable obstacle avoidance
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


596. COM_OF_LOSS_T (FLOAT)
- 名称：COM_OF_LOSS_T (FLOAT)
- 参数描述：Time-out to wait when offboard connection is lost before triggering offboard lost action Comment: See COM_OBL_RC_ACT to configure action.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 60] (0.01)`
- 默认值：`1.0`
- 单位：`s`


597. COM_PARACHUTE (INT32)
- 名称：COM_PARACHUTE (INT32)
- 参数描述：Expect and require a healthy MAVLink parachute system
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


598. COM_POSCTL_NAVL (INT32)
- 名称：COM_POSCTL_NAVL (INT32)
- 参数描述：Position control navigation loss response Comment: This sets the flight mode that will be used if navigation accuracy is no longer adequate for position control. If Altitude/Manual is selected: assume use of remote control after fallback. Switch to Altitude mode if a height estimate is available, else switch to MANUAL. If Land/Descend is selected: assume no use of remote control after fallback. Switch to Land mode if a height estimate is available, else switch to Descend. 参数对照:0: Altitude/Manual 1: Land/Descend
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


599. COM_POS_FS_DELAY (INT32)
- 名称：COM_POS_FS_DELAY (INT32)
- 参数描述：Loss of position failsafe activation delay Comment: This sets number of seconds that the position checks need to be failed before the failsafe will activate. The default value has been optimised for rotary wing applications. For fixed wing applications, a larger value between 5 and 10 should be used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 100]`
- 默认值：`1`
- 单位：`s`


600. COM_POS_FS_EPH (FLOAT)
- 名称：COM_POS_FS_EPH (FLOAT)
- 参数描述：Horizontal position error threshold Comment: This is the horizontal position error (EPH) threshold that will trigger a failsafe. The default is appropriate for a multicopter. Can be increased for a fixed-wing. If the previous position error was below this threshold, there is an additional factor of 2.5 applied (threshold for invalidation 2.5 times the one for validation). Set to -1 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 400]`
- 默认值：`5.`
- 单位：`m`


601. COM_POS_LOW_EPH (FLOAT)
- 名称：COM_POS_LOW_EPH (FLOAT)
- 参数描述：EPH threshold for RTL Comment: Specify the threshold for triggering a warning for low local position accuracy. Additionally triggers a RTL if currently in Mission or Loiter mode. Local position has to be still declared valid, which is most of all depending on COM_POS_FS_EPH. Use this feature on systems with dead-reckoning capabilites (e.g. fixed-wing vehicles with airspeed sensor) to improve the user notification and failure mitigation when flying in GNSS-denied areas. Set to -1 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1.0`
- 单位：`m`


602. COM_POWER_COUNT (INT32)
- 名称：COM_POWER_COUNT (INT32)
- 参数描述：Required number of redundant power modules Comment: This configures a check to verify the expected number of 5V rail power supplies are present. By default only one is expected. Note: CBRK_SUPPLY_CHK disables all power checks including this one.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`1`
- 单位：``


603. COM_PREARM_MODE (INT32)
- 名称：COM_PREARM_MODE (INT32)
- 参数描述：Condition to enter prearmed mode Comment: Condition to enter the prearmed state, an intermediate state between disarmed and armed in which non-throttling actuators are active. 参数对照:0: Disabled 1: Safety button 2: Always
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


604. COM_QC_ACT (INT32)
- 名称：COM_QC_ACT (INT32)
- 参数描述：Set command after a quadchute  Values:-1: Warning only 0: Return mode 1: Land mode 2: Hold mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


605. COM_RCL_EXCEPT (INT32)
- 名称：COM_RCL_EXCEPT (INT32)
- 参数描述：RC loss exceptions Comment: Specify modes in which RC loss is ignored and the failsafe action not triggered. Bitmask:0: Mission 1: Hold 2: Offboard
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 31]`
- 默认值：`0`
- 单位：``


606. COM_RC_ARM_HYST (INT32)
- 名称：COM_RC_ARM_HYST (INT32)
- 参数描述：RC input arm/disarm command duration Comment: The default value of 1000 requires the stick to be held in the arm or disarm position for 1 second.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[100, 1500]`
- 默认值：`1000`
- 单位：`ms`


607. COM_RC_IN_MODE (INT32)
- 名称：COM_RC_IN_MODE (INT32)
- 参数描述：RC control input mode Comment: A value of 0 enables RC transmitter control (only). A valid RC transmitter calibration is required. A value of 1 allows joystick control only. RC input handling and the associated checks are disabled. A value of 2 allows either RC Transmitter or Joystick input. The first valid input is used, will fallback to other sources if the input stream becomes invalid. A value of 3 allows either input from RC or joystick. The first available source is selected and used until reboot. A value of 4 ignores any stick input. 参数对照:0: RC Transmitter only 1: Joystick only 2: RC and Joystick with fallback 3: RC or Joystick keep first 4: Stick input disabled
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`3`
- 单位：``


608. COM_RC_LOSS_T (FLOAT)
- 名称：COM_RC_LOSS_T (FLOAT)
- 参数描述：Manual control loss timeout Comment: The time in seconds without a new setpoint from RC or Joystick, after which the connection is considered lost. This must be kept short as the vehicle will use the last supplied setpoint until the timeout triggers.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 35] (0.1)`
- 默认值：`0.5`
- 单位：`s`


609. COM_RC_OVERRIDE (INT32)
- 名称：COM_RC_OVERRIDE (INT32)
- 参数描述：Enable RC stick override of auto and/or offboard modes Comment: When RC stick override is enabled, moving the RC sticks more than COM_RC_STICK_OV immediately gives control back to the pilot by switching to Position mode and if position is unavailable Altitude mode. Note: Only has an effect on multicopters, and VTOLs in multicopter mode. Bitmask:0: Enable override during auto modes (except for in critical battery reaction) 1: Enable override during offboard mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`1`
- 单位：``


610. COM_RC_STICK_OV (FLOAT)
- 名称：COM_RC_STICK_OV (FLOAT)
- 参数描述：RC stick override threshold Comment: If COM_RC_OVERRIDE is enabled and the joystick input is moved more than this threshold the autopilot the pilot takes over control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[5, 80] (0.05)`
- 默认值：`30.0`
- 单位：`%`


611. COM_SPOOLUP_TIME (FLOAT)
- 名称：COM_SPOOLUP_TIME (FLOAT)
- 参数描述：Enforced delay between arming and further navigation Comment: The minimal time from arming the motors until moving the vehicle is possible is COM_SPOOLUP_TIME seconds. Goal: - Motors and propellers spool up to idle speed before getting commanded to spin faster - Timeout for ESCs and smart batteries to successfulyy do failure checks e.g. for stuck rotors before the vehicle is off the ground
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 30] (0.1)`
- 默认值：`1.0`
- 单位：`s`


612. COM_TAKEOFF_ACT (INT32)
- 名称：COM_TAKEOFF_ACT (INT32)
- 参数描述：Action after TAKEOFF has been accepted Comment: The mode transition after TAKEOFF has completed successfully. 参数对照:0: Hold 1: Mission (if valid)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


613. COM_VEL_FS_EVH (FLOAT)
- 名称：COM_VEL_FS_EVH (FLOAT)
- 参数描述：Horizontal velocity error threshold Comment: This is the horizontal velocity error (EVH) threshold that will trigger a failsafe. The default is appropriate for a multicopter. Can be increased for a fixed-wing. If the previous velocity error was below this threshold, there is an additional factor of 2.5 applied (threshold for invalidation 2.5 times the one for validation).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`1.`
- 单位：`m/s`


614. COM_WIND_MAX (FLOAT)
- 名称：COM_WIND_MAX (FLOAT)
- 参数描述：Wind speed RTL threshold Comment: Wind speed threshold above which an automatic return to launch is triggered. It is not possible to resume the mission or switch to any auto mode other than RTL or Land if this threshold is exceeded. Taking over in any manual mode is still possible. Set to -1 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, ?] (0.1)`
- 默认值：`-1.`
- 单位：`m/s`


615. COM_WIND_WARN (FLOAT)
- 名称：COM_WIND_WARN (FLOAT)
- 参数描述：Wind speed warning threshold Comment: A warning is triggered if the currently estimated wind speed is above this value. Warning is sent periodically (every 1 minute). Set to -1 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, ?] (0.1)`
- 默认值：`-1.`
- 单位：`m/s`


616. NAV_DLL_ACT (INT32)
- 名称：NAV_DLL_ACT (INT32)
- 参数描述：Set GCS connection loss failsafe mode Comment: The GCS connection loss failsafe will only be entered after a timeout, set by COM_DL_LOSS_T in seconds. Once the timeout occurs the selected action will be executed. 参数对照:0: Disabled 1: Hold mode 2: Return mode 3: Land mode 5: Terminate 6: Disarm
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


617. NAV_RCL_ACT (INT32)
- 名称：NAV_RCL_ACT (INT32)
- 参数描述：Set RC loss failsafe mode Comment: The RC loss failsafe will only be entered after a timeout, set by COM_RC_LOSS_T in seconds. If RC input checks have been disabled by setting the COM_RC_IN_MODE param it will not be triggered. 参数对照:1: Hold mode 2: Return mode 3: Land mode 5: Terminate 6: Disarm
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 6]`
- 默认值：`2`
- 单位：``


618. CYPHAL_BAUD (INT32)
- 名称：CYPHAL_BAUD (INT32)
- 参数描述：UAVCAN/CAN v1 bus bitrate    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20000, 1000000]`
- 默认值：`1000000`
- 单位：`bit/s`


619. CYPHAL_ENABLE (INT32)
- 名称：CYPHAL_ENABLE (INT32)
- 参数描述：Cyphal Comment: 0 - Cyphal disabled. 1 - Enables Cyphal Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


620. CYPHAL_ID (INT32)
- 名称：CYPHAL_ID (INT32)
- 参数描述：Cyphal Node ID Comment: Read the specs at https://uavcan.org to learn more about Node ID. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 125]`
- 默认值：`1`
- 单位：``


621. UCAN1_ACTR_PUB (INT32)
- 名称：UCAN1_ACTR_PUB (INT32)
- 参数描述：actuator_outputs uORB over Cyphal publication port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


622. UCAN1_BMS_BP_SUB (INT32)
- 名称：UCAN1_BMS_BP_SUB (INT32)
- 参数描述：UDRAL battery parameters subscription  port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


623. UCAN1_BMS_BS_SUB (INT32)
- 名称：UCAN1_BMS_BS_SUB (INT32)
- 参数描述：UDRAL battery status subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


624. UCAN1_BMS_ES_SUB (INT32)
- 名称：UCAN1_BMS_ES_SUB (INT32)
- 参数描述：UDRAL battery energy source subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


625. UCAN1_ESC0_SUB (INT32)
- 名称：UCAN1_ESC0_SUB (INT32)
- 参数描述：ESC 0 subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


626. UCAN1_ESC_PUB (INT32)
- 名称：UCAN1_ESC_PUB (INT32)
- 参数描述：Cyphal ESC publication port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


627. UCAN1_GPS0_SUB (INT32)
- 名称：UCAN1_GPS0_SUB (INT32)
- 参数描述：GPS 0 subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


628. UCAN1_GPS1_SUB (INT32)
- 名称：UCAN1_GPS1_SUB (INT32)
- 参数描述：GPS 1 subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


629. UCAN1_GPS_PUB (INT32)
- 名称：UCAN1_GPS_PUB (INT32)
- 参数描述：Cyphal GPS publication port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


630. UCAN1_LG_BMS_SUB (INT32)
- 名称：UCAN1_LG_BMS_SUB (INT32)
- 参数描述：Cyphal legacy battery port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


631. UCAN1_SERVO_PUB (INT32)
- 名称：UCAN1_SERVO_PUB (INT32)
- 参数描述：Cyphal Servo publication port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


632. UCAN1_UORB_GPS (INT32)
- 名称：UCAN1_UORB_GPS (INT32)
- 参数描述：sensor_gps uORB over Cyphal subscription port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


633. UCAN1_UORB_GPS_P (INT32)
- 名称：UCAN1_UORB_GPS_P (INT32)
- 参数描述：sensor_gps uORB over Cyphal publication port ID
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 6143]`
- 默认值：`-1`
- 单位：``


634. DSHOT_3D_DEAD_H (INT32)
- 名称：DSHOT_3D_DEAD_H (INT32)
- 参数描述：DSHOT 3D deadband high Comment: When the actuator_output is between DSHOT_3D_DEAD_L and DSHOT_3D_DEAD_H, motor will not spin. This value is with respect to the mixer_module range (0-1999), not the DSHOT values.
  - 翻译：DSHOT 3D 死区上限 Comment: 当执行器输出位于 DSHOT_3D_DEAD_L 和 DSHOT_3D_DEAD_H 之间时，电机不会旋转。此值是相对于混合器模块范围（0-1999）的，而不是 DSHOT 值。
  - gpt注解：DSHOT_3D_DEAD_H 参数用于定义执行器输出范围内的死区上限。当执行器输出位于 DSHOT_3D_DEAD_L 和 DSHOT_3D_DEAD_H 之间时，电机将不会旋转。需要注意，此值是相对于混合器模块范围（0-1999）的，而不是 DSHOT 协议的值。
- `[Min, Max]`：`[1000, 1999]`
- 默认值：`1000`
- 单位：``


635. DSHOT_3D_DEAD_L (INT32)
- 名称：DSHOT_3D_DEAD_L (INT32)
- 参数描述：DSHOT 3D deadband low Comment: When the actuator_output is between DSHOT_3D_DEAD_L and DSHOT_3D_DEAD_H, motor will not spin. This value is with respect to the mixer_module range (0-1999), not the DSHOT values.
  - 翻译：DSHOT 3D 死区下限 Comment: 当执行器输出位于 DSHOT_3D_DEAD_L 和 DSHOT_3D_DEAD_H 之间时，电机不会旋转。此值是相对于混合器模块范围（0-1999）的，而不是 DSHOT 值。
  - gpt注解：DSHOT_3D_DEAD_L 参数用于定义执行器输出范围内的死区下限。当执行器输出位于 DSHOT_3D_DEAD_L 和 DSHOT_3D_DEAD_H 之间时，电机将不会旋转。需要注意，此值是相对于混合器模块范围（0-1999）的，而不是 DSHOT 协议的值。
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


636. DSHOT_3D_ENABLE (INT32)
- 名称：DSHOT_3D_ENABLE (INT32)
- 参数描述：Allows for 3D mode when using DShot and suitable mixer Comment: WARNING: ESC must be configured for 3D mode, and DSHOT_MIN set to 0. This splits the throttle ranges in two. Direction 1) 48 is the slowest, 1047 is the fastest. Direction 2) 1049 is the slowest, 2047 is the fastest. When mixer outputs 1000 or value inside DSHOT 3D deadband, DShot 0 is sent.
  - 翻译：启用 DShot 3D 模式允许适用于 DShot 和适当混合器的情况 Comment: 警告：ESC 必须配置为 3D 模式，并将 DSHOT_MIN 设置为 0。这将将油门范围分为两个部分。 方向 1) 48 最慢，1047 最快。 方向 2) 1049 最慢，2047 最快。当混合器输出值为 1000 或位于 DSHOT 3D 死区内时，将发送 DShot 0。
  - gpt注解：DSHOT_3D_ENABLE 参数允许在使用 DShot 和适当混合器时启用 3D 模式。需要警告：电调（ESC）必须配置为 3D 模式，并将 DSHOT_MIN 设置为 0。这将分割油门范围为两部分，其中方向 1) 的范围从 48 最慢到 1047 最快，方向 2) 的范围从 1049 最慢到 2047 最快。当混合器输出值为 1000 或位于 DSHOT 3D 死区内时，将发送 DShot 0。
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


637. DSHOT_MIN (FLOAT)
- 名称：DSHOT_MIN (FLOAT)
- 参数描述：Minimum DShot Motor Output Comment: Minimum Output Value for DShot in percent. The value depends on the ESC. Make sure to set this high enough so that the motors are always spinning while armed.
  - 翻译：最小 DShot 电机输出 Comment: DShot 的最小输出值，以百分比表示。该值取决于电调（ESC）。请确保将其设置得足够高，以确保电机在解锁状态下始终旋转。
  - gpt注解：DSHOT_MIN 参数用于定义 DShot 输出的最小值，以百分比表示。实际值取决于所使用的电调（ESC）。请务必将此值设置得足够高，以确保在解锁状态下电机始终保持旋转。
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.055`
- 单位：`%`


638. DSHOT_TEL_CFG (INT32)
- 名称：DSHOT_TEL_CFG (INT32)
- 参数描述：Serial Configuration for DShot Driver Comment: Configure on which serial port to run DShot Driver. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：DShot 驱动串口配置 Comment: 配置在哪个串口上运行 DShot 驱动。参数对照: 0: 禁用 6: 串口 6 101: 遥测串口 1 102: 遥测串口 2 103: 遥测串口 3 104: 遥测/串口 4 201: GPS 串口 1 202: GPS 串口 2 203: GPS 串口 3 300: 遥控器串口 301: WiFi 串口 401: EXT2 需要重启: true
  - gpt注解：DSHOT_TEL_CFG 参数用于配置 DShot 驱动运行的串口。请根据需要选择适当的串口配置。注意，某些配置可能需要重启设备才能生效。
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


639. MOT_POLE_COUNT (INT32)
- 名称：MOT_POLE_COUNT (INT32)
- 参数描述：Number of magnetic poles of the motors Comment: Specify the number of magnetic poles of the motors. It is required to compute the RPM value from the eRPM returned with the ESC telemetry. Either get the number from the motor spec sheet or count the magnets on the bell of the motor (not the stator magnets). Typical motors for 5 inch props have 14 poles.
  - 翻译：电机的磁极数 Comment: 指定电机的磁极数。这是计算从带有电子调速器遥测返回的电机电转数 (eRPM) 所必需的。您可以从电机规格表中获取这个数值，或者数一数电机钟罩上的磁铁数量（而不是定子上的磁铁）。通常用于 5 寸桨叶的电机有 14 个磁极。
  - gpt注解：MOT_POLE_COUNT 参数用于指定电机的磁极数。这个数值对于从电子调速器遥测中计算电机的实际电转数（RPM）非常重要。请根据电机规格或钟罩上的磁铁数量来设置这个参数。
- `[Min, Max]`：``
- 默认值：`14`
- 单位：``


640. EKF2_ABIAS_INIT (FLOAT)
- 名称：EKF2_ABIAS_INIT (FLOAT)
- 参数描述：1-sigma IMU accelerometer switch-on bias    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.5]`
- 默认值：`0.2`
- 单位：`m/s^2`


641. EKF2_ABL_ACCLIM (FLOAT)
- 名称：EKF2_ABL_ACCLIM (FLOAT)
- 参数描述：Maximum IMU accel magnitude that allows IMU bias learning Comment: If the magnitude of the IMU accelerometer vector exceeds this value, the EKF delta velocity state estimation will be inhibited. This reduces the adverse effect of high manoeuvre accelerations and IMU nonlinerity and scale factor errors on the delta velocity bias estimates.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20.0, 200.0]`
- 默认值：`25.0`
- 单位：`m/s^2`


642. EKF2_ABL_GYRLIM (FLOAT)
- 名称：EKF2_ABL_GYRLIM (FLOAT)
- 参数描述：Maximum IMU gyro angular rate magnitude that allows IMU bias learning Comment: If the magnitude of the IMU angular rate vector exceeds this value, the EKF delta velocity state estimation will be inhibited. This reduces the adverse effect of rapid rotation rates and associated errors on the delta velocity bias estimates.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2.0, 20.0]`
- 默认值：`3.0`
- 单位：`rad/s`


643. EKF2_ABL_LIM (FLOAT)
- 名称：EKF2_ABL_LIM (FLOAT)
- 参数描述：Accelerometer bias learning limit Comment: The ekf delta velocity bias states will be limited to within a range equivalent to +- of this value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.8]`
- 默认值：`0.4`
- 单位：`m/s^2`


644. EKF2_ABL_TAU (FLOAT)
- 名称：EKF2_ABL_TAU (FLOAT)
- 参数描述：Time constant used by acceleration and angular rate magnitude checks used to inhibit delta velocity bias learning Comment: The vector magnitude of angular rate and acceleration used to check if learning should be inhibited has a peak hold filter applied to it with an exponential decay. This parameter controls the time constant of the decay.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0]`
- 默认值：`0.5`
- 单位：`s`


645. EKF2_ACC_B_NOISE (FLOAT)
- 名称：EKF2_ACC_B_NOISE (FLOAT)
- 参数描述：Process noise for IMU accelerometer bias prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.01]`
- 默认值：`3.0e-3`
- 单位：`m/s^3`


646. EKF2_ACC_NOISE (FLOAT)
- 名称：EKF2_ACC_NOISE (FLOAT)
- 参数描述：Accelerometer noise for covariance prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1.0]`
- 默认值：`3.5e-1`
- 单位：`m/s^2`


647. EKF2_AID_MASK (INT32)
- 名称：EKF2_AID_MASK (INT32)
- 参数描述：Will be removed after v1.14 release Comment: Set bits in the following positions to enable: 0 : Deprecated, use EKF2_GPS_CTRL instead 1 : Deprecated. use EKF2_OF_CTRL instead 2 : Deprecated, use EKF2_IMU_CTRL instead 3 : Deprecated, use EKF2_EV_CTRL instead 4 : Deprecated, use EKF2_EV_CTRL instead 5 : Deprecated. use EKF2_DRAG_CTRL instead 6 : Deprecated, use EKF2_EV_CTRL instead 7 : Deprecated, use EKF2_GPS_CTRL instead 8 : Deprecated, use EKF2_EV_CTRL instead Bitmask:0: unused 1: unused 2: unused 3: unused 4: unused 5: unused 6: unused 7: unused 8: unused Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 511]`
- 默认值：`0`
- 单位：``


648. EKF2_ANGERR_INIT (FLOAT)
- 名称：EKF2_ANGERR_INIT (FLOAT)
- 参数描述：1-sigma tilt angle uncertainty after gravity vector alignment    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.5]`
- 默认值：`0.1`
- 单位：`rad`


649. EKF2_ARSP_THR (FLOAT)
- 名称：EKF2_ARSP_THR (FLOAT)
- 参数描述：Airspeed fusion threshold Comment: Airspeed data is fused for wind estimation if above this threshold. Set to 0 to disable airspeed fusion. For reliable wind estimation both sideslip (see EKF2_FUSE_BETA) and airspeed fusion should be enabled. Only applies to fixed-wing vehicles (or VTOLs in fixed-wing mode).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：`m/s`


650. EKF2_ASPD_MAX (FLOAT)
- 名称：EKF2_ASPD_MAX (FLOAT)
- 参数描述：Upper limit on airspeed along individual axes used to correct baro for position error effects
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[5.0, 50.0]`
- 默认值：`20.0`
- 单位：`m/s`


651. EKF2_ASP_DELAY (FLOAT)
- 名称：EKF2_ASP_DELAY (FLOAT)
- 参数描述：Airspeed measurement delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`100`
- 单位：`ms`


652. EKF2_AVEL_DELAY (FLOAT)
- 名称：EKF2_AVEL_DELAY (FLOAT)
- 参数描述：Auxiliary Velocity Estimate (e.g from a landing target) delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`5`
- 单位：`ms`


653. EKF2_BARO_CTRL (INT32)
- 名称：EKF2_BARO_CTRL (INT32)
- 参数描述：Barometric sensor height aiding Comment: If this parameter is enabled then the estimator will make use of the barometric height measurements to estimate its height in addition to other height sources (if activated).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


654. EKF2_BARO_DELAY (FLOAT)
- 名称：EKF2_BARO_DELAY (FLOAT)
- 参数描述：Barometer measurement delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`0`
- 单位：`ms`


655. EKF2_BARO_GATE (FLOAT)
- 名称：EKF2_BARO_GATE (FLOAT)
- 参数描述：Gate size for barometric and GPS height fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


656. EKF2_BARO_NOISE (FLOAT)
- 名称：EKF2_BARO_NOISE (FLOAT)
- 参数描述：Measurement noise for barometric altitude
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 15.0]`
- 默认值：`3.5`
- 单位：`m`


657. EKF2_BCOEF_X (FLOAT)
- 名称：EKF2_BCOEF_X (FLOAT)
- 参数描述：X-axis ballistic coefficient used for multi-rotor wind estimation Comment: This parameter controls the prediction of drag produced by bluff body drag along the forward/reverse axis when flying a multi-copter which enables estimation of wind drift when enabled by the EKF2_DRAG_CTRL parameter. The drag produced by this effect scales with speed squared. The predicted drag from the rotors is specified separately by the EKF2_MCOEF parameter. Set this parameter to zero to turn off the bluff body drag model for this axis.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 200.0]`
- 默认值：`100.0`
- 单位：`kg/m^2`


658. EKF2_BCOEF_Y (FLOAT)
- 名称：EKF2_BCOEF_Y (FLOAT)
- 参数描述：Y-axis ballistic coefficient used for multi-rotor wind estimation Comment: This parameter controls the prediction of drag produced by bluff body drag along the right/left axis when flying a multi-copter, which enables estimation of wind drift when enabled by the EKF2_DRAG_CTRL parameter. The drag produced by this effect scales with speed squared. The predicted drag from the rotors is specified separately by the EKF2_MCOEF parameter. Set this parameter to zero to turn off the bluff body drag model for this axis.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 200.0]`
- 默认值：`100.0`
- 单位：`kg/m^2`


659. EKF2_BETA_GATE (FLOAT)
- 名称：EKF2_BETA_GATE (FLOAT)
- 参数描述：Gate size for synthetic sideslip fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


660. EKF2_BETA_NOISE (FLOAT)
- 名称：EKF2_BETA_NOISE (FLOAT)
- 参数描述：Noise for synthetic sideslip fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0]`
- 默认值：`0.3`
- 单位：`m/s`


661. EKF2_DECL_TYPE (INT32)
- 名称：EKF2_DECL_TYPE (INT32)
- 参数描述：Integer bitmask controlling handling of magnetic declination Comment: Set bits in the following positions to enable functions. 0 : Set to true to use the declination from the geo_lookup library when the GPS position becomes available, set to false to always use the EKF2_MAG_DECL value. 1 : Set to true to save the EKF2_MAG_DECL parameter to the value returned by the EKF when the vehicle disarms. 2 : Set to true to always use the declination as an observation when 3-axis magnetometer fusion is being used. Bitmask:0: use geo_lookup declination 1: save EKF2_MAG_DECL on disarm 2: use declination as an observation Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 7]`
- 默认值：`7`
- 单位：``


662. EKF2_DRAG_CTRL (INT32)
- 名称：EKF2_DRAG_CTRL (INT32)
- 参数描述：Multirotor wind estimation selection Comment: Activate wind speed estimation using specific-force measurements and a drag model defined by EKF2_BCOEF_[XY] and EKF2_MCOEF. Only use on vehicles that have their thrust aligned with the Z axis and no thrust in the XY plane.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


663. EKF2_DRAG_NOISE (FLOAT)
- 名称：EKF2_DRAG_NOISE (FLOAT)
- 参数描述：Specific drag force observation noise variance used by the multi-rotor specific drag force model Comment: Increasing this makes the multi-rotor wind estimates adjust more slowly.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 10.0]`
- 默认值：`2.5`
- 单位：`(m/s^2)^2`


664. EKF2_EAS_NOISE (FLOAT)
- 名称：EKF2_EAS_NOISE (FLOAT)
- 参数描述：Measurement noise for airspeed fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 5.0]`
- 默认值：`1.4`
- 单位：`m/s`


665. EKF2_EVA_NOISE (FLOAT)
- 名称：EKF2_EVA_NOISE (FLOAT)
- 参数描述：Measurement noise for vision angle observations used to lower bound or replace the uncertainty included in the message
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, ?]`
- 默认值：`0.1`
- 单位：`rad`


666. EKF2_EVP_GATE (FLOAT)
- 名称：EKF2_EVP_GATE (FLOAT)
- 参数描述：Gate size for vision position fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


667. EKF2_EVP_NOISE (FLOAT)
- 名称：EKF2_EVP_NOISE (FLOAT)
- 参数描述：Measurement noise for vision position observations used to lower bound or replace the uncertainty included in the message
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`0.1`
- 单位：`m`


668. EKF2_EVV_GATE (FLOAT)
- 名称：EKF2_EVV_GATE (FLOAT)
- 参数描述：Gate size for vision velocity estimate fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`3.0`
- 单位：`SD`


669. EKF2_EVV_NOISE (FLOAT)
- 名称：EKF2_EVV_NOISE (FLOAT)
- 参数描述：Measurement noise for vision velocity observations used to lower bound or replace the uncertainty included in the message
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`0.1`
- 单位：`m/s`


670. EKF2_EV_CTRL (INT32)
- 名称：EKF2_EV_CTRL (INT32)
- 参数描述：External vision (EV) sensor aiding Comment: Set bits in the following positions to enable: 0 : Horizontal position fusion 1 : Vertical position fusion 2 : 3D velocity fusion 3 : Yaw Bitmask:0: Horizontal position 1: Vertical position 2: 3D velocity 3: Yaw
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 15]`
- 默认值：`15`
- 单位：``


671. EKF2_EV_DELAY (FLOAT)
- 名称：EKF2_EV_DELAY (FLOAT)
- 参数描述：Vision Position Estimator delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`0`
- 单位：`ms`


672. EKF2_EV_NOISE_MD (INT32)
- 名称：EKF2_EV_NOISE_MD (INT32)
- 参数描述：External vision (EV) noise mode Comment: If set to 0 (default) the measurement noise is taken from the vision message and the EV noise parameters are used as a lower bound. If set to 1 the observation noise is set from the parameters directly, 参数对照:0: EV reported variance (parameter lower bound) 1: EV noise parameters
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


673. EKF2_EV_POS_X (FLOAT)
- 名称：EKF2_EV_POS_X (FLOAT)
- 参数描述：X position of VI sensor focal point in body frame (forward axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


674. EKF2_EV_POS_Y (FLOAT)
- 名称：EKF2_EV_POS_Y (FLOAT)
- 参数描述：Y position of VI sensor focal point in body frame (right axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


675. EKF2_EV_POS_Z (FLOAT)
- 名称：EKF2_EV_POS_Z (FLOAT)
- 参数描述：Z position of VI sensor focal point in body frame (down axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


676. EKF2_EV_QMIN (INT32)
- 名称：EKF2_EV_QMIN (INT32)
- 参数描述：External vision (EV) minimum quality (optional) Comment: External vision will only be started and fused if the quality metric is above this threshold. The quality metric is a completely optional field provided by some VIO systems.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100]`
- 默认值：`0`
- 单位：``


677. EKF2_FUSE_BETA (INT32)
- 名称：EKF2_FUSE_BETA (INT32)
- 参数描述：Enable synthetic sideslip fusion Comment: For reliable wind estimation both sideslip and airspeed fusion (see EKF2_ARSP_THR) should be enabled. Only applies to fixed-wing vehicles (or VTOLs in fixed-wing mode). Note: side slip fusion is currently not supported for tailsitters.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


678. EKF2_GBIAS_INIT (FLOAT)
- 名称：EKF2_GBIAS_INIT (FLOAT)
- 参数描述：1-sigma IMU gyro switch-on bias    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.2]`
- 默认值：`0.1`
- 单位：`rad/s`


679. EKF2_GND_EFF_DZ (FLOAT)
- 名称：EKF2_GND_EFF_DZ (FLOAT)
- 参数描述：Baro deadzone range for height fusion Comment: Sets the value of deadzone applied to negative baro innovations. Deadzone is enabled when EKF2_GND_EFF_DZ > 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0]`
- 默认值：`4.0`
- 单位：`m`


680. EKF2_GND_MAX_HGT (FLOAT)
- 名称：EKF2_GND_MAX_HGT (FLOAT)
- 参数描述：Height above ground level for ground effect zone Comment: Sets the maximum distance to the ground level where negative baro innovations are expected.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 5.0]`
- 默认值：`0.5`
- 单位：`m`


681. EKF2_GPS_CHECK (INT32)
- 名称：EKF2_GPS_CHECK (INT32)
- 参数描述：Integer bitmask controlling GPS checks Comment: Set bits to 1 to enable checks. Checks enabled by the following bit positions 0 : Minimum required sat count set by EKF2_REQ_NSATS 1 : Maximum allowed PDOP set by EKF2_REQ_PDOP 2 : Maximum allowed horizontal position error set by EKF2_REQ_EPH 3 : Maximum allowed vertical position error set by EKF2_REQ_EPV 4 : Maximum allowed speed error set by EKF2_REQ_SACC 5 : Maximum allowed horizontal position rate set by EKF2_REQ_HDRIFT. This check will only run when the vehicle is on ground and stationary. 6 : Maximum allowed vertical position rate set by EKF2_REQ_VDRIFT. This check will only run when the vehicle is on ground and stationary. 7 : Maximum allowed horizontal speed set by EKF2_REQ_HDRIFT. This check will only run when the vehicle is on ground and stationary. 8 : Maximum allowed vertical velocity discrepancy set by EKF2_REQ_VDRIFT Bitmask:0: Min sat count (EKF2_REQ_NSATS) 1: Max PDOP (EKF2_REQ_PDOP) 2: Max horizontal position error (EKF2_REQ_EPH) 3: Max vertical position error (EKF2_REQ_EPV) 4: Max speed error (EKF2_REQ_SACC) 5: Max horizontal position rate (EKF2_REQ_HDRIFT) 6: Max vertical position rate (EKF2_REQ_VDRIFT) 7: Max horizontal speed (EKF2_REQ_HDRIFT) 8: Max vertical velocity discrepancy (EKF2_REQ_VDRIFT)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 511]`
- 默认值：`245`
- 单位：``


682. EKF2_GPS_CTRL (INT32)
- 名称：EKF2_GPS_CTRL (INT32)
- 参数描述：GNSS sensor aiding Comment: Set bits in the following positions to enable: 0 : Longitude and latitude fusion 1 : Altitude fusion 2 : 3D velocity fusion 3 : Dual antenna heading fusion Bitmask:0: Lon/lat 1: Altitude 2: 3D velocity 3: Dual antenna heading
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 15]`
- 默认值：`7`
- 单位：``


683. EKF2_GPS_DELAY (FLOAT)
- 名称：EKF2_GPS_DELAY (FLOAT)
- 参数描述：GPS measurement delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`110`
- 单位：`ms`


684. EKF2_GPS_POS_X (FLOAT)
- 名称：EKF2_GPS_POS_X (FLOAT)
- 参数描述：X position of GPS antenna in body frame (forward axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


685. EKF2_GPS_POS_Y (FLOAT)
- 名称：EKF2_GPS_POS_Y (FLOAT)
- 参数描述：Y position of GPS antenna in body frame (right axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


686. EKF2_GPS_POS_Z (FLOAT)
- 名称：EKF2_GPS_POS_Z (FLOAT)
- 参数描述：Z position of GPS antenna in body frame (down axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


687. EKF2_GPS_P_GATE (FLOAT)
- 名称：EKF2_GPS_P_GATE (FLOAT)
- 参数描述：Gate size for GPS horizontal position fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


688. EKF2_GPS_P_NOISE (FLOAT)
- 名称：EKF2_GPS_P_NOISE (FLOAT)
- 参数描述：Measurement noise for gps position
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 10.0]`
- 默认值：`0.5`
- 单位：`m`


689. EKF2_GPS_V_GATE (FLOAT)
- 名称：EKF2_GPS_V_GATE (FLOAT)
- 参数描述：Gate size for GPS velocity fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


690. EKF2_GPS_V_NOISE (FLOAT)
- 名称：EKF2_GPS_V_NOISE (FLOAT)
- 参数描述：Measurement noise for gps horizontal velocity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 5.0]`
- 默认值：`0.3`
- 单位：`m/s`


691. EKF2_GRAV_NOISE (FLOAT)
- 名称：EKF2_GRAV_NOISE (FLOAT)
- 参数描述：Accelerometer measurement noise for gravity based observations
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10.0]`
- 默认值：`1.0`
- 单位：`m/s^2`


692. EKF2_GSF_TAS (FLOAT)
- 名称：EKF2_GSF_TAS (FLOAT)
- 参数描述：Default value of true airspeed used in EKF-GSF AHRS calculation Comment: If no airspeed measurements are available, the EKF-GSF AHRS calculation will assume this value of true airspeed when compensating for centripetal acceleration during turns. Set to zero to disable centripetal acceleration compensation during fixed wing flight modes.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`15.0`
- 单位：`m/s`


693. EKF2_GYR_B_LIM (FLOAT)
- 名称：EKF2_GYR_B_LIM (FLOAT)
- 参数描述：Gyro bias learning limit Comment: The ekf delta angle bias states will be limited to within a range equivalent to +- of this value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.4]`
- 默认值：`0.15`
- 单位：`rad/s`


694. EKF2_GYR_B_NOISE (FLOAT)
- 名称：EKF2_GYR_B_NOISE (FLOAT)
- 参数描述：Process noise for IMU rate gyro bias prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.01]`
- 默认值：`1.0e-3`
- 单位：`rad/s^2`


695. EKF2_GYR_NOISE (FLOAT)
- 名称：EKF2_GYR_NOISE (FLOAT)
- 参数描述：Rate gyro noise for covariance prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0001, 0.1]`
- 默认值：`1.5e-2`
- 单位：`rad/s`


696. EKF2_HDG_GATE (FLOAT)
- 名称：EKF2_HDG_GATE (FLOAT)
- 参数描述：Gate size for heading fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`2.6`
- 单位：`SD`


697. EKF2_HEAD_NOISE (FLOAT)
- 名称：EKF2_HEAD_NOISE (FLOAT)
- 参数描述：Measurement noise for magnetic heading fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1.0]`
- 默认值：`0.3`
- 单位：`rad`


698. EKF2_HGT_REF (INT32)
- 名称：EKF2_HGT_REF (INT32)
- 参数描述：Determines the reference source of height data used by the EKF Comment: When multiple height sources are enabled at the same time, the height estimate will always converge towards the reference height source selected by this parameter. The range sensor and vision options should only be used when for operation over a flat surface as the local NED origin will move up and down with ground level. 参数对照:0: Barometric pressure 1: GPS 2: Range sensor 3: Vision Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


699. EKF2_IMU_CTRL (INT32)
- 名称：EKF2_IMU_CTRL (INT32)
- 参数描述：IMU control   Bitmask:0: Gyro Bias 1: Accel Bias 2: Gravity vector fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 7]`
- 默认值：`3`
- 单位：``


700. EKF2_IMU_POS_X (FLOAT)
- 名称：EKF2_IMU_POS_X (FLOAT)
- 参数描述：X position of IMU in body frame (forward axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


701. EKF2_IMU_POS_Y (FLOAT)
- 名称：EKF2_IMU_POS_Y (FLOAT)
- 参数描述：Y position of IMU in body frame (right axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


702. EKF2_IMU_POS_Z (FLOAT)
- 名称：EKF2_IMU_POS_Z (FLOAT)
- 参数描述：Z position of IMU in body frame (down axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


703. EKF2_MAG_ACCLIM (FLOAT)
- 名称：EKF2_MAG_ACCLIM (FLOAT)
- 参数描述：Horizontal acceleration threshold used by automatic selection of magnetometer fusion method Comment: This parameter is used when the magnetometer fusion method is set automatically (EKF2_MAG_TYPE = 0). If the filtered horizontal acceleration is greater than this parameter value, then the EKF will use 3-axis magnetometer fusion.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 5.0]`
- 默认值：`0.5`
- 单位：`m/s^2`


704. EKF2_MAG_B_NOISE (FLOAT)
- 名称：EKF2_MAG_B_NOISE (FLOAT)
- 参数描述：Process noise for body magnetic field prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.1]`
- 默认值：`1.0e-4`
- 单位：`gauss/s`


705. EKF2_MAG_CHECK (INT32)
- 名称：EKF2_MAG_CHECK (INT32)
- 参数描述：Magnetic field strength test selection Comment: Bitmask to set which check is used to decide whether the magnetometer data is valid. If GNSS data is received, the magnetic field is compared to a World Magnetic Model (WMM), otherwise an average value is used. This check is useful to reject occasional hard iron disturbance. Set bits to 1 to enable checks. Checks enabled by the following bit positions 0 : Magnetic field strength. Set tolerance using EKF2_MAG_CHK_STR 1 : Magnetic field inclination. Set tolerance using EKF2_MAG_CHK_INC 2 : Wait for GNSS to find the theoretical strength and inclination using the WMM Bitmask:0: Strength (EKF2_MAG_CHK_STR) 1: Inclination (EKF2_MAG_CHK_INC) 2: Wait for WMM
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 7]`
- 默认值：`1`
- 单位：``


706. EKF2_MAG_CHK_INC (FLOAT)
- 名称：EKF2_MAG_CHK_INC (FLOAT)
- 参数描述：Magnetic field inclination check tolerance Comment: Maximum allowed deviation from the expected magnetic field inclination to pass the check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 90.0]`
- 默认值：`20.`
- 单位：`deg`


707. EKF2_MAG_CHK_STR (FLOAT)
- 名称：EKF2_MAG_CHK_STR (FLOAT)
- 参数描述：Magnetic field strength check tolerance Comment: Maximum allowed deviation from the expected magnetic field strength to pass the check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0]`
- 默认值：`0.2`
- 单位：`gauss`


708. EKF2_MAG_DECL (FLOAT)
- 名称：EKF2_MAG_DECL (FLOAT)
- 参数描述：Magnetic declination
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：`deg`


709. EKF2_MAG_DELAY (FLOAT)
- 名称：EKF2_MAG_DELAY (FLOAT)
- 参数描述：Magnetometer measurement delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`0`
- 单位：`ms`


710. EKF2_MAG_E_NOISE (FLOAT)
- 名称：EKF2_MAG_E_NOISE (FLOAT)
- 参数描述：Process noise for earth magnetic field prediction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.1]`
- 默认值：`1.0e-3`
- 单位：`gauss/s`


711. EKF2_MAG_GATE (FLOAT)
- 名称：EKF2_MAG_GATE (FLOAT)
- 参数描述：Gate size for magnetometer XYZ component fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`3.0`
- 单位：`SD`


712. EKF2_MAG_NOISE (FLOAT)
- 名称：EKF2_MAG_NOISE (FLOAT)
- 参数描述：Measurement noise for magnetometer 3-axis fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.001, 1.0]`
- 默认值：`5.0e-2`
- 单位：`gauss`


713. EKF2_MAG_TYPE (INT32)
- 名称：EKF2_MAG_TYPE (INT32)
- 参数描述：Type of magnetometer fusion Comment: Integer controlling the type of magnetometer fusion used - magnetic heading or 3-component vector. The fusion of magnetometer data as a three component vector enables vehicle body fixed hard iron errors to be learned, but requires a stable earth field. If set to 'Automatic' magnetic heading fusion is used when on-ground and 3-axis magnetic field fusion in-flight with fallback to magnetic heading fusion if there is insufficient motion to make yaw or magnetic field states observable. If set to 'Magnetic heading' magnetic heading fusion is used at all times. If set to 'None' the magnetometer will not be used under any circumstance. If no external source of yaw is available, it is possible to use post-takeoff horizontal movement combined with GPS velocity measurements to align the yaw angle with the timer required (depending on the amount of movement and GPS data quality). 参数对照:0: Automatic 1: Magnetic heading 5: None Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


714. EKF2_MAG_YAWLIM (FLOAT)
- 名称：EKF2_MAG_YAWLIM (FLOAT)
- 参数描述：Yaw rate threshold used by automatic selection of magnetometer fusion method Comment: This parameter is used when the magnetometer fusion method is set automatically (EKF2_MAG_TYPE = 0). If the filtered yaw rate is greater than this parameter value, then the EKF will use 3-axis magnetometer fusion.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0]`
- 默认值：`0.20`
- 单位：`rad/s`


715. EKF2_MCOEF (FLOAT)
- 名称：EKF2_MCOEF (FLOAT)
- 参数描述：Propeller momentum drag coefficient used for multi-rotor wind estimation Comment: This parameter controls the prediction of drag produced by the propellers when flying a multi-copter, which enables estimation of wind drift when enabled by the EKF2_DRAG_CTRL parameter. The drag produced by this effect scales with speed not speed squared and is produced because some of the air velocity normal to the propeller axis of rotation is lost when passing through the rotor disc. This  changes the momentum of the flow which creates a drag reaction force. When comparing un-ducted propellers of the same diameter, the effect is roughly proportional to the area of the propeller blades when viewed side on and changes with propeller selection. Momentum drag is significantly higher for ducted rotors. To account for the drag produced by the body which scales with speed squared, see documentation for the EKF2_BCOEF_X and EKF2_BCOEF_Y parameters. Set this parameter to zero to turn off the momentum drag model for both axis.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1.0]`
- 默认值：`0.15`
- 单位：`1/s`


716. EKF2_MIN_RNG (FLOAT)
- 名称：EKF2_MIN_RNG (FLOAT)
- 参数描述：Expected range finder reading when on ground Comment: If the vehicle is on ground, is not moving as determined by the motion test and the range finder is returning invalid or no data, then an assumed range value of EKF2_MIN_RNG will be used by the terrain estimator so that a terrain height estimate is available at the start of flight in situations where the range finder may be inside its minimum measurements distance when on ground.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`0.1`
- 单位：`m`


717. EKF2_MULTI_IMU (INT32)
- 名称：EKF2_MULTI_IMU (INT32)
- 参数描述：Multi-EKF IMUs Comment: Maximum number of IMUs to use for Multi-EKF. Set 0 to disable. Requires SENS_IMU_MODE 0. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`0`
- 单位：``


718. EKF2_MULTI_MAG (INT32)
- 名称：EKF2_MULTI_MAG (INT32)
- 参数描述：Multi-EKF Magnetometers Comment: Maximum number of magnetometers to use for Multi-EKF. Set 0 to disable. Requires SENS_MAG_MODE 0. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`0`
- 单位：``


719. EKF2_NOAID_NOISE (FLOAT)
- 名称：EKF2_NOAID_NOISE (FLOAT)
- 参数描述：Measurement noise for non-aiding position hold
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 50.0]`
- 默认值：`10.0`
- 单位：`m`


720. EKF2_NOAID_TOUT (INT32)
- 名称：EKF2_NOAID_TOUT (INT32)
- 参数描述：Maximum lapsed time from last fusion of measurements that constrain velocity drift before the EKF will report the horizontal nav solution as invalid
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[500000, 10000000]`
- 默认值：`5000000`
- 单位：`µs`


721. EKF2_OF_CTRL (INT32)
- 名称：EKF2_OF_CTRL (INT32)
- 参数描述：Optical flow aiding Comment: Enable optical flow fusion.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


722. EKF2_OF_DELAY (FLOAT)
- 名称：EKF2_OF_DELAY (FLOAT)
- 参数描述：Optical flow measurement delay relative to IMU measurements Comment: Assumes measurement is timestamped at trailing edge of integration period Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`20`
- 单位：`ms`


723. EKF2_OF_GATE (FLOAT)
- 名称：EKF2_OF_GATE (FLOAT)
- 参数描述：Gate size for optical flow fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`3.0`
- 单位：`SD`


724. EKF2_OF_N_MAX (FLOAT)
- 名称：EKF2_OF_N_MAX (FLOAT)
- 参数描述：Measurement noise for the optical flow sensor Comment: (when it's reported quality metric is at the minimum set by EKF2_OF_QMIN). The following condition must be met: EKF2_OF_N_MAXN >= EKF2_OF_N_MIN
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, ?]`
- 默认值：`0.5`
- 单位：`rad/s`


725. EKF2_OF_N_MIN (FLOAT)
- 名称：EKF2_OF_N_MIN (FLOAT)
- 参数描述：Measurement noise for the optical flow sensor when it's reported quality metric is at the maximum
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, ?]`
- 默认值：`0.15`
- 单位：`rad/s`


726. EKF2_OF_POS_X (FLOAT)
- 名称：EKF2_OF_POS_X (FLOAT)
- 参数描述：X position of optical flow focal point in body frame (forward axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


727. EKF2_OF_POS_Y (FLOAT)
- 名称：EKF2_OF_POS_Y (FLOAT)
- 参数描述：Y position of optical flow focal point in body frame (right axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


728. EKF2_OF_POS_Z (FLOAT)
- 名称：EKF2_OF_POS_Z (FLOAT)
- 参数描述：Z position of optical flow focal point in body frame (down axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


729. EKF2_OF_QMIN (INT32)
- 名称：EKF2_OF_QMIN (INT32)
- 参数描述：Optical Flow data will only be used in air if the sensor reports a quality metric >= EKF2_OF_QMIN
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`1`
- 单位：``


730. EKF2_OF_QMIN_GND (INT32)
- 名称：EKF2_OF_QMIN_GND (INT32)
- 参数描述：Optical Flow data will only be used on the ground if the sensor reports a quality metric >= EKF2_OF_QMIN_GND
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


731. EKF2_PCOEF_XN (FLOAT)
- 名称：EKF2_PCOEF_XN (FLOAT)
- 参数描述：Static pressure position error coefficient for the negative X axis Comment: This is the ratio of static pressure error to dynamic pressure generated by a negative wind relative velocity along the X body axis. If the baro height estimate rises during backwards flight, then this will be a negative number.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5]`
- 默认值：`0.0`
- 单位：``


732. EKF2_PCOEF_XP (FLOAT)
- 名称：EKF2_PCOEF_XP (FLOAT)
- 参数描述：Static pressure position error coefficient for the positive X axis Comment: This is the ratio of static pressure error to dynamic pressure generated by a positive wind relative velocity along the X body axis. If the baro height estimate rises during forward flight, then this will be a negative number.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5]`
- 默认值：`0.0`
- 单位：``


733. EKF2_PCOEF_YN (FLOAT)
- 名称：EKF2_PCOEF_YN (FLOAT)
- 参数描述：Pressure position error coefficient for the negative Y axis Comment: This is the ratio of static pressure error to dynamic pressure generated by a wind relative velocity along the negative Y (LH) body axis. If the baro height estimate rises during sideways flight to the left, then this will be a negative number.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5]`
- 默认值：`0.0`
- 单位：``


734. EKF2_PCOEF_YP (FLOAT)
- 名称：EKF2_PCOEF_YP (FLOAT)
- 参数描述：Pressure position error coefficient for the positive Y axis Comment: This is the ratio of static pressure error to dynamic pressure generated by a wind relative velocity along the positive Y (RH) body axis. If the baro height estimate rises during sideways flight to the right, then this will be a negative number.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5]`
- 默认值：`0.0`
- 单位：``


735. EKF2_PCOEF_Z (FLOAT)
- 名称：EKF2_PCOEF_Z (FLOAT)
- 参数描述：Static pressure position error coefficient for the Z axis Comment: This is the ratio of static pressure error to dynamic pressure generated by a wind relative velocity along the Z body axis.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5]`
- 默认值：`0.0`
- 单位：``


736. EKF2_PREDICT_US (INT32)
- 名称：EKF2_PREDICT_US (INT32)
- 参数描述：EKF prediction period Comment: EKF prediction period in microseconds. This should ideally be an integer multiple of the IMU time delta. Actual filter update will be an integer multiple of IMU update.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1000, 20000]`
- 默认值：`10000`
- 单位：`µs`


737. EKF2_REQ_EPH (FLOAT)
- 名称：EKF2_REQ_EPH (FLOAT)
- 参数描述：Required EPH to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 100]`
- 默认值：`3.0`
- 单位：`m`


738. EKF2_REQ_EPV (FLOAT)
- 名称：EKF2_REQ_EPV (FLOAT)
- 参数描述：Required EPV to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 100]`
- 默认值：`5.0`
- 单位：`m`


739. EKF2_REQ_GPS_H (FLOAT)
- 名称：EKF2_REQ_GPS_H (FLOAT)
- 参数描述：Required GPS health time on startup Comment: Minimum continuous period without GPS failure required to mark a healthy GPS status. It can be reduced to speed up initialization, but it's recommended to keep this unchanged for a vehicle. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, ?]`
- 默认值：`10.0`
- 单位：`s`


740. EKF2_REQ_HDRIFT (FLOAT)
- 名称：EKF2_REQ_HDRIFT (FLOAT)
- 参数描述：Maximum horizontal drift speed to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0]`
- 默认值：`0.1`
- 单位：`m/s`


741. EKF2_REQ_NSATS (INT32)
- 名称：EKF2_REQ_NSATS (INT32)
- 参数描述：Required satellite count to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[4, 12]`
- 默认值：`6`
- 单位：``


742. EKF2_REQ_PDOP (FLOAT)
- 名称：EKF2_REQ_PDOP (FLOAT)
- 参数描述：Maximum PDOP to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.5, 5.0]`
- 默认值：`2.5`
- 单位：``


743. EKF2_REQ_SACC (FLOAT)
- 名称：EKF2_REQ_SACC (FLOAT)
- 参数描述：Required speed accuracy to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 5.0]`
- 默认值：`0.5`
- 单位：`m/s`


744. EKF2_REQ_VDRIFT (FLOAT)
- 名称：EKF2_REQ_VDRIFT (FLOAT)
- 参数描述：Maximum vertical drift speed to use GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.5]`
- 默认值：`0.2`
- 单位：`m/s`


745. EKF2_RNG_A_HMAX (FLOAT)
- 名称：EKF2_RNG_A_HMAX (FLOAT)
- 参数描述：Maximum absolute altitude (height above ground level) allowed for conditional range aid mode Comment: If the vehicle absolute altitude exceeds this value then the estimator will not fuse range measurements to estimate its height. This only applies when conditional range aid mode is activated (EKF2_RNG_CTRL = 1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10.0]`
- 默认值：`5.0`
- 单位：`m`


746. EKF2_RNG_A_IGATE (FLOAT)
- 名称：EKF2_RNG_A_IGATE (FLOAT)
- 参数描述：Gate size used for innovation consistency checks for range aid fusion Comment: A lower value means HAGL needs to be more stable in order to use range finder for height estimation in range aid mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 5.0]`
- 默认值：`1.0`
- 单位：`SD`


747. EKF2_RNG_A_VMAX (FLOAT)
- 名称：EKF2_RNG_A_VMAX (FLOAT)
- 参数描述：Maximum horizontal velocity allowed for conditional range aid mode Comment: If the vehicle horizontal speed exceeds this value then the estimator will not fuse range measurements to estimate its height. This only applies when conditional range aid mode is activated (EKF2_RNG_CTRL = 1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 2]`
- 默认值：`1.0`
- 单位：`m/s`


748. EKF2_RNG_CTRL (INT32)
- 名称：EKF2_RNG_CTRL (INT32)
- 参数描述：Range sensor height aiding Comment: WARNING: Range finder measurements are less reliable and can experience unexpected errors. For these reasons, if accurate control of height relative to ground is required, it is recommended to use the MPC_ALT_MODE parameter instead, unless baro errors are severe enough to cause problems with landing and takeoff. To en-/disable range finder for terrain height estimation, use EKF2_TERR_MASK instead. If this parameter is enabled then the estimator will make use of the range finder measurements to estimate its height in addition to other height sources (if activated). Range sensor aiding can be enabled (i.e.: always use) or set in "conditional" mode. Conditional mode: This enables the range finder to be used during low speed (< EKF2_RNG_A_VMAX) and low altitude (< EKF2_RNG_A_HMAX) operation, eg takeoff and landing, where baro interference from rotor wash is excessive and can corrupt EKF state estimates. It is intended to be used where a vertical takeoff and landing is performed, and horizontal flight does not occur until above EKF2_RNG_A_HMAX. 参数对照:0: Disable range fusion 1: Enabled (conditional mode) 2: Enabled
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


749. EKF2_RNG_DELAY (FLOAT)
- 名称：EKF2_RNG_DELAY (FLOAT)
- 参数描述：Range finder measurement delay relative to IMU measurements    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`5`
- 单位：`ms`


750. EKF2_RNG_GATE (FLOAT)
- 名称：EKF2_RNG_GATE (FLOAT)
- 参数描述：Gate size for range finder fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`5.0`
- 单位：`SD`


751. EKF2_RNG_K_GATE (FLOAT)
- 名称：EKF2_RNG_K_GATE (FLOAT)
- 参数描述：Gate size used for range finder kinematic consistency check Comment: To be used, the time derivative of the distance sensor measurements projected on the vertical axis needs to be statistically consistent with the estimated vertical velocity of the drone. Decrease this value to make the filter more robust against range finder faulty data (stuck, reflections, ...). Note: tune the range finder noise parameters (EKF2_RNG_NOISE and EKF2_RNG_SFE) before tuning this gate.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 5.0]`
- 默认值：`1.0`
- 单位：`SD`


752. EKF2_RNG_NOISE (FLOAT)
- 名称：EKF2_RNG_NOISE (FLOAT)
- 参数描述：Measurement noise for range finder fusion
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`0.1`
- 单位：`m`


753. EKF2_RNG_PITCH (FLOAT)
- 名称：EKF2_RNG_PITCH (FLOAT)
- 参数描述：Range sensor pitch offset
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.75, 0.75]`
- 默认值：`0.0`
- 单位：`rad`


754. EKF2_RNG_POS_X (FLOAT)
- 名称：EKF2_RNG_POS_X (FLOAT)
- 参数描述：X position of range finder origin in body frame (forward axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


755. EKF2_RNG_POS_Y (FLOAT)
- 名称：EKF2_RNG_POS_Y (FLOAT)
- 参数描述：Y position of range finder origin in body frame (right axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


756. EKF2_RNG_POS_Z (FLOAT)
- 名称：EKF2_RNG_POS_Z (FLOAT)
- 参数描述：Z position of range finder origin in body frame (down axis with origin relative to vehicle centre of gravity)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


757. EKF2_RNG_QLTY_T (FLOAT)
- 名称：EKF2_RNG_QLTY_T (FLOAT)
- 参数描述：Minimum duration during which the reported range finder signal quality needs to be non-zero in order to be declared valid (s)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 5]`
- 默认值：`1.0`
- 单位：`s`


758. EKF2_RNG_SFE (FLOAT)
- 名称：EKF2_RNG_SFE (FLOAT)
- 参数描述：Range finder range dependent noise scaler Comment: Specifies the increase in range finder noise with range.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.2]`
- 默认值：`0.05`
- 单位：`m/m`


759. EKF2_SEL_ERR_RED (FLOAT)
- 名称：EKF2_SEL_ERR_RED (FLOAT)
- 参数描述：Selector error reduce threshold Comment: EKF2 instances have to be better than the selected by at least this amount before their relative score can be reduced.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.2`
- 单位：``


760. EKF2_SEL_IMU_ACC (FLOAT)
- 名称：EKF2_SEL_IMU_ACC (FLOAT)
- 参数描述：Selector acceleration threshold Comment: EKF2 selector acceleration error threshold for comparing accelerometers. Acceleration vector differences larger than this will result in accumulated velocity error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：`m/s^2`


761. EKF2_SEL_IMU_ANG (FLOAT)
- 名称：EKF2_SEL_IMU_ANG (FLOAT)
- 参数描述：Selector angular threshold Comment: EKF2 selector maximum accumulated angular error threshold for comparing gyros. Accumulated angular error larger than this will result in the sensor being declared faulty.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`15.0`
- 单位：`deg`


762. EKF2_SEL_IMU_RAT (FLOAT)
- 名称：EKF2_SEL_IMU_RAT (FLOAT)
- 参数描述：Selector angular rate threshold Comment: EKF2 selector angular rate error threshold for comparing gyros. Angular rate vector differences larger than this will result in accumulated angular error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`7.0`
- 单位：`deg/s`


763. EKF2_SEL_IMU_VEL (FLOAT)
- 名称：EKF2_SEL_IMU_VEL (FLOAT)
- 参数描述：Selector angular threshold Comment: EKF2 selector maximum accumulated velocity threshold for comparing accelerometers. Accumulated velocity error larger than this will result in the sensor being declared faulty.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2.0`
- 单位：`m/s`


764. EKF2_SYNT_MAG_Z (INT32)
- 名称：EKF2_SYNT_MAG_Z (INT32)
- 参数描述：Enable synthetic magnetometer Z component measurement Comment: Use for vehicles where the measured body Z magnetic field is subject to strong magnetic interference. For magnetic heading fusion the magnetometer Z measurement will be replaced by a synthetic value calculated using the knowledge of the 3D magnetic field vector at the location of the drone. Therefore, this parameter will only have an effect if the global position of the drone is known. For 3D mag fusion the magnetometer Z measurement will simply be ignored instead of fusing the synthetic value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


765. EKF2_TAS_GATE (FLOAT)
- 名称：EKF2_TAS_GATE (FLOAT)
- 参数描述：Gate size for TAS fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`3.0`
- 单位：`SD`


766. EKF2_TAU_POS (FLOAT)
- 名称：EKF2_TAU_POS (FLOAT)
- 参数描述：Time constant of the position output prediction and smoothing filter. Controls how tightly the output track the EKF states
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0]`
- 默认值：`0.25`
- 单位：`s`


767. EKF2_TAU_VEL (FLOAT)
- 名称：EKF2_TAU_VEL (FLOAT)
- 参数描述：Time constant of the velocity output prediction and smoothing filter
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[?, 1.0]`
- 默认值：`0.25`
- 单位：`s`


768. EKF2_TERR_GRAD (FLOAT)
- 名称：EKF2_TERR_GRAD (FLOAT)
- 参数描述：Magnitude of terrain gradient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.5`
- 单位：`m/m`


769. EKF2_TERR_MASK (INT32)
- 名称：EKF2_TERR_MASK (INT32)
- 参数描述：Integer bitmask controlling fusion sources of the terrain estimator Comment: Set bits in the following positions to enable: 0 : Set to true to use range finder data if available 1 : Set to true to use optical flow data if available Bitmask:0: use range finder 1: use optical flow
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`3`
- 单位：``


770. EKF2_TERR_NOISE (FLOAT)
- 名称：EKF2_TERR_NOISE (FLOAT)
- 参数描述：Terrain altitude process noise - accounts for instability in vehicle height estimate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, ?]`
- 默认值：`5.0`
- 单位：`m/s`


771. EKF2_WIND_NSD (FLOAT)
- 名称：EKF2_WIND_NSD (FLOAT)
- 参数描述：Process noise spectral density for wind velocity prediction Comment: When unaided, the wind estimate uncertainty (1-sigma, in m/s) increases by this amount every second.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0]`
- 默认值：`1.0e-2`
- 单位：`m/s^2/sqrt(Hz)`


772. ESC_BL_VER (INT32)
- 名称：ESC_BL_VER (INT32)
- 参数描述：Required esc bootloader version
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


773. ESC_FW_VER (INT32)
- 名称：ESC_FW_VER (INT32)
- 参数描述：Required esc firmware version
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


774. ESC_HW_VER (INT32)
- 名称：ESC_HW_VER (INT32)
- 参数描述：Required esc hardware version
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


775. EV_TSK_RC_LOSS (INT32)
- 名称：EV_TSK_RC_LOSS (INT32)
- 参数描述：RC Loss Alarm Comment: Enable/disable event task for RC Loss. When enabled, an alarm tune will be played via buzzer or ESCs, if supported. The alarm will sound after a disarm, if the vehicle was previously armed and only if the vehicle had RC signal at some point. Particularly useful for locating crashed drones without a GPS sensor. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


776. EV_TSK_STAT_DIS (INT32)
- 名称：EV_TSK_STAT_DIS (INT32)
- 参数描述：Status Display Comment: Enable/disable event task for displaying the vehicle status using arm-mounted LEDs. When enabled and if the vehicle supports it, LEDs will flash indicating various vehicle status changes. Currently PX4 has not implemented any specific status events. - Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


777. FW_MAN_P_MAX (FLOAT)
- 名称：FW_MAN_P_MAX (FLOAT)
- 参数描述：Maximum manual pitch angle Comment: Applies to both directions in all manual modes with attitude stabilization but without altitude control
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 90.0] (0.5)`
- 默认值：`30.0`
- 单位：`deg`


778. FW_MAN_R_MAX (FLOAT)
- 名称：FW_MAN_R_MAX (FLOAT)
- 参数描述：Maximum manual roll angle Comment: Applies to both directions in all manual modes with attitude stabilization
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 90.0] (0.5)`
- 默认值：`45.0`
- 单位：`deg`


779. FW_MAN_YR_MAX (FLOAT)
- 名称：FW_MAN_YR_MAX (FLOAT)
- 参数描述：Maximum manually added yaw rate Comment: This is the maximally added yaw rate setpoint from the yaw stick in any attitude controlled flight mode. It is added to the yaw rate setpoint generated by the controller for turn coordination.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (0.5)`
- 默认值：`30.`
- 单位：`deg/s`


780. FW_PSP_OFF (FLOAT)
- 名称：FW_PSP_OFF (FLOAT)
- 参数描述：Pitch setpoint offset (pitch at level flight) Comment: An airframe specific offset of the pitch setpoint in degrees, the value is added to the pitch setpoint and should correspond to the pitch at typical cruise speed of the airframe.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0] (0.5)`
- 默认值：`0.0`
- 单位：`deg`


781. FW_P_RMAX_NEG (FLOAT)
- 名称：FW_P_RMAX_NEG (FLOAT)
- 参数描述：Maximum negative / down pitch rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 180] (0.5)`
- 默认值：`60.0`
- 单位：`deg/s`


782. FW_P_RMAX_POS (FLOAT)
- 名称：FW_P_RMAX_POS (FLOAT)
- 参数描述：Maximum positive / up pitch rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 180] (0.5)`
- 默认值：`60.0`
- 单位：`deg/s`


783. FW_P_TC (FLOAT)
- 名称：FW_P_TC (FLOAT)
- 参数描述：Attitude pitch time constant Comment: This defines the latency between a pitch step input and the achieved setpoint (inverse to a P gain). Smaller systems may require smaller values.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.2, 1.0] (0.05)`
- 默认值：`0.4`
- 单位：`s`


784. FW_R_RMAX (FLOAT)
- 名称：FW_R_RMAX (FLOAT)
- 参数描述：Maximum roll rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 180] (0.5)`
- 默认值：`70.0`
- 单位：`deg/s`


785. FW_R_TC (FLOAT)
- 名称：FW_R_TC (FLOAT)
- 参数描述：Attitude Roll Time Constant Comment: This defines the latency between a roll step input and the achieved setpoint (inverse to a P gain). Smaller systems may require smaller values.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.2, 1.0] (0.05)`
- 默认值：`0.4`
- 单位：`s`


786. FW_SPOILERS_DESC (FLOAT)
- 名称：FW_SPOILERS_DESC (FLOAT)
- 参数描述：Spoiler descend setting
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.`
- 单位：`norm`


787. FW_SPOILERS_LND (FLOAT)
- 名称：FW_SPOILERS_LND (FLOAT)
- 参数描述：Spoiler landing setting
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.`
- 单位：`norm`


788. FW_WR_FF (FLOAT)
- 名称：FW_WR_FF (FLOAT)
- 参数描述：Wheel steering rate feed forward
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.05)`
- 默认值：`0.2`
- 单位：`%/rad/s`


789. FW_WR_I (FLOAT)
- 名称：FW_WR_I (FLOAT)
- 参数描述：Wheel steering rate integrator gain Comment: This gain defines how much control response will result out of a steady state error. It trims any constant error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.1`
- 单位：`%/rad`


790. FW_WR_IMAX (FLOAT)
- 名称：FW_WR_IMAX (FLOAT)
- 参数描述：Wheel steering rate integrator limit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.05)`
- 默认值：`0.4`
- 单位：``


791. FW_WR_P (FLOAT)
- 名称：FW_WR_P (FLOAT)
- 参数描述：Wheel steering rate proportional gain Comment: This defines how much the wheel steering input will be commanded depending on the current body angular rate error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.5`
- 单位：`%/rad/s`


792. FW_W_EN (INT32)
- 名称：FW_W_EN (INT32)
- 参数描述：Enable wheel steering controller Comment: Only enabled during automatic runway takeoff and landing. In all manual modes the wheel is directly controlled with yaw stick.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


793. FW_W_RMAX (FLOAT)
- 名称：FW_W_RMAX (FLOAT)
- 参数描述：Maximum wheel steering rate Comment: This limits the maximum wheel steering rate the controller will output (in degrees per second).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 90.0] (0.5)`
- 默认值：`30.0`
- 单位：`deg/s`


794. FW_Y_RMAX (FLOAT)
- 名称：FW_Y_RMAX (FLOAT)
- 参数描述：Maximum yaw rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 180] (0.5)`
- 默认值：`50.0`
- 单位：`deg/s`


795. FW_LND_ABORT (INT32)
- 名称：FW_LND_ABORT (INT32)
- 参数描述：Bit mask to set the automatic landing abort conditions Comment: Terrain estimation: bit 0: Abort if terrain is not found bit 1: Abort if terrain times out (after a first successful measurement) The last estimate is always used as ground, whether the last valid measurement or the land waypoint, depending on the selected abort criteria, until an abort condition is entered. If FW_LND_USETER == 0, these bits are ignored. TODO: Extend automatic abort conditions e.g. glide slope tracking error (horizontal and vertical) Bitmask:0: Abort if terrain is not found (only applies to mission landings) 1: Abort if terrain times out (after a first successful measurement)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`3`
- 单位：``


796. FW_LND_AIRSPD (FLOAT)
- 名称：FW_LND_AIRSPD (FLOAT)
- 参数描述：Landing airspeed Comment: The calibrated airspeed setpoint during landing. If set <= 0.0, landing airspeed = FW_AIRSPD_MIN by default.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, ?] (0.1)`
- 默认值：`-1.`
- 单位：`m/s`


797. FW_LND_ANG (FLOAT)
- 名称：FW_LND_ANG (FLOAT)
- 参数描述：Maximum landing slope angle Comment: Typically the desired landing slope angle when landing configuration (flaps, airspeed) is enabled. Set this value within the vehicle's performance limits.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 15.0] (0.5)`
- 默认值：`5.0`
- 单位：`deg`


798. FW_LND_EARLYCFG (INT32)
- 名称：FW_LND_EARLYCFG (INT32)
- 参数描述：Early landing configuration deployment Comment: When disabled, the landing configuration (flaps, landing airspeed, etc.) is only activated on the final approach to landing. When enabled, it is already activated when entering the final loiter-down (loiter-to-alt) waypoint before the landing approach.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


799. FW_LND_FLALT (FLOAT)
- 名称：FW_LND_FLALT (FLOAT)
- 参数描述：Landing flare altitude (relative to landing altitude) Comment: NOTE: max(FW_LND_FLALT, FW_LND_FL_TIME * |z-velocity|) is taken as the flare altitude
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.5)`
- 默认值：`0.5`
- 单位：`m`


800. FW_LND_FL_PMAX (FLOAT)
- 名称：FW_LND_FL_PMAX (FLOAT)
- 参数描述：Flare, maximum pitch Comment: Maximum pitch during flare, a positive sign means nose up Applied once flaring is triggered
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 45.0] (0.5)`
- 默认值：`15.0`
- 单位：`deg`


801. FW_LND_FL_PMIN (FLOAT)
- 名称：FW_LND_FL_PMIN (FLOAT)
- 参数描述：Flare, minimum pitch Comment: Minimum pitch during flare, a positive sign means nose up Applied once flaring is triggered
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-5, 15.0] (0.5)`
- 默认值：`2.5`
- 单位：`deg`


802. FW_LND_FL_SINK (FLOAT)
- 名称：FW_LND_FL_SINK (FLOAT)
- 参数描述：Landing flare sink rate Comment: TECS will attempt to control the aircraft to this sink rate via pitch angle (throttle killed during flare)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2] (0.1)`
- 默认值：`0.25`
- 单位：`m/s`


803. FW_LND_FL_TIME (FLOAT)
- 名称：FW_LND_FL_TIME (FLOAT)
- 参数描述：Landing flare time Comment: Multiplied by the descent rate to calculate a dynamic altitude at which to trigger the flare. NOTE: max(FW_LND_FLALT, FW_LND_FL_TIME * descent rate) is taken as the flare altitude
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 5.0] (0.1)`
- 默认值：`1.0`
- 单位：`s`


804. FW_LND_NUDGE (INT32)
- 名称：FW_LND_NUDGE (INT32)
- 参数描述：Landing touchdown nudging option Comment: Approach angle nudging: shifts the touchdown point laterally while keeping the approach entrance point constant Approach path nudging: shifts the touchdown point laterally along with the entire approach path This is useful for manually adjusting the landing point in real time when map or GNSS errors cause an offset from the desired landing vector. Nuding is done with yaw stick, constrained to FW_LND_TD_OFF (in meters) and the direction is relative to the vehicle heading (stick deflection to the right = land point moves to the right as seen by the vehicle). 参数对照:0: Disable nudging 1: Nudge approach angle 2: Nudge approach path
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`2`
- 单位：``


805. FW_LND_TD_OFF (FLOAT)
- 名称：FW_LND_TD_OFF (FLOAT)
- 参数描述：Maximum lateral position offset for the touchdown point
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (1)`
- 默认值：`3.0`
- 单位：`m`


806. FW_LND_TD_TIME (FLOAT)
- 名称：FW_LND_TD_TIME (FLOAT)
- 参数描述：Landing touchdown time (since flare start) Comment: This is the time after the start of flaring that we expect the vehicle to touch the runway. At this time, a 0.5s clamp down ramp will engage, constraining the pitch setpoint to RWTO_PSP. If enabled, ensure that RWTO_PSP is configured appropriately for full gear contact on ground roll. Set to -1.0 to disable touchdown clamping. E.g. it may not be desirable to clamp on belly landings. The touchdown time will be constrained to be greater than or equal to the flare time (FW_LND_FL_TIME).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 5.0] (0.1)`
- 默认值：`-1.0`
- 单位：`s`


807. FW_LND_THRTC_SC (FLOAT)
- 名称：FW_LND_THRTC_SC (FLOAT)
- 参数描述：Altitude time constant factor for landing Comment: Set this parameter to less than 1.0 to make TECS react faster to altitude errors during landing than during normal flight. During landing, the TECS altitude time constant (FW_T_ALT_TC) is multiplied by this value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.2, 1.0] (0.1)`
- 默认值：`1.0`
- 单位：``


808. FW_LND_USETER (INT32)
- 名称：FW_LND_USETER (INT32)
- 参数描述：Use terrain estimation during landing. This is critical for detecting when to flare, and should be enabled if possible Comment: NOTE: terrain estimate is currently solely derived from a distance sensor. If enabled and no measurement is found within a given timeout, the landing waypoint altitude will be used OR the landing will be aborted, depending on the criteria set in FW_LND_ABORT. If disabled, FW_LND_ABORT terrain based criteria are ignored. 参数对照:0: Disable the terrain estimate 1: Use the terrain estimate to trigger the flare (only) 2: Calculate landing glide slope relative to the terrain estimate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`1`
- 单位：``


809. FW_WING_HEIGHT (FLOAT)
- 名称：FW_WING_HEIGHT (FLOAT)
- 参数描述：Height (AGL) of the wings when the aircraft is on the ground Comment: This is used to constrain a minimum altitude below which we keep wings level to avoid wing tip strike. It's safer to give a slight margin here (> 0m)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (1)`
- 默认值：`0.5`
- 单位：`m`


810. FW_WING_SPAN (FLOAT)
- 名称：FW_WING_SPAN (FLOAT)
- 参数描述：The aircraft's wing span (length from tip to tip) Comment: This is used for limiting the roll setpoint near the ground. (if multiple wings, take the longest span)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, ?] (0.1)`
- 默认值：`3.0`
- 单位：`m`


811. FW_LAUN_AC_T (FLOAT)
- 名称：FW_LAUN_AC_T (FLOAT)
- 参数描述：Trigger time Comment: Launch is detected when acceleration in body forward direction is above FW_LAUN_AC_THLD for FW_LAUN_AC_T seconds.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 5.0] (0.05)`
- 默认值：`0.05`
- 单位：`s`


812. FW_LAUN_AC_THLD (FLOAT)
- 名称：FW_LAUN_AC_THLD (FLOAT)
- 参数描述：Trigger acceleration threshold Comment: Launch is detected when acceleration in body forward direction is above FW_LAUN_AC_THLD for FW_LAUN_AC_T seconds.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (0.5)`
- 默认值：`30.0`
- 单位：`m/s^2`


813. FW_LAUN_DETCN_ON (INT32)
- 名称：FW_LAUN_DETCN_ON (INT32)
- 参数描述：Fixed-wing launch detection Comment: Enables automatic launch detection based on measured acceleration. Use for hand- or catapult-launched vehicles. Not compatible with runway takeoff.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


814. FW_LAUN_MOT_DEL (FLOAT)
- 名称：FW_LAUN_MOT_DEL (FLOAT)
- 参数描述：Motor delay Comment: Start the motor(s) this amount of seconds after launch is detected.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (0.5)`
- 默认值：`0.0`
- 单位：`s`


815. NPFG_DAMPING (FLOAT)
- 名称：NPFG_DAMPING (FLOAT)
- 参数描述：NPFG damping ratio Comment: Damping ratio of the NPFG control law.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.10, 1.00] (0.01)`
- 默认值：`0.7`
- 单位：``


816. NPFG_EN_MIN_GSP (INT32)
- 名称：NPFG_EN_MIN_GSP (INT32)
- 参数描述：Enable minimum forward ground speed maintaining excess wind handling logic
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


817. NPFG_GSP_MAX_TK (FLOAT)
- 名称：NPFG_GSP_MAX_TK (FLOAT)
- 参数描述：Maximum, minimum forward ground speed for track keeping in excess wind Comment: The maximum value of the minimum forward ground speed that may be commanded by the track keeping excess wind handling logic. Commanded in full at the normalized track error fraction of the track error boundary and reduced to zero on track.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (0.5)`
- 默认值：`5.0`
- 单位：`m/s`


818. NPFG_LB_PERIOD (INT32)
- 名称：NPFG_LB_PERIOD (INT32)
- 参数描述：Enable automatic lower bound on the NPFG period Comment: Avoids limit cycling from a too aggressively tuned period/damping combination. If set to false, also disables the upper bound NPFG_PERIOD_UB.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


819. NPFG_PERIOD (FLOAT)
- 名称：NPFG_PERIOD (FLOAT)
- 参数描述：NPFG period Comment: Period of the NPFG control law.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 100.0] (0.1)`
- 默认值：`10.0`
- 单位：`s`


820. NPFG_PERIOD_SF (FLOAT)
- 名称：NPFG_PERIOD_SF (FLOAT)
- 参数描述：Period safety factor Comment: Multiplied by period for conservative minimum period bounding (when period lower bounding is enabled). 1.0 bounds at marginal stability.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10.0] (0.1)`
- 默认值：`1.5`
- 单位：``


821. NPFG_ROLL_TC (FLOAT)
- 名称：NPFG_ROLL_TC (FLOAT)
- 参数描述：Roll time constant Comment: Time constant of roll controller command / response, modeled as first order delay. Used to determine lower period bound. Setting zero disables automatic period bounding.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.00, 2.00] (0.05)`
- 默认值：`0.5`
- 单位：`s`


822. NPFG_SW_DST_MLT (FLOAT)
- 名称：NPFG_SW_DST_MLT (FLOAT)
- 参数描述：NPFG switch distance multiplier Comment: Multiplied by the track error boundary to determine when the aircraft switches to the next waypoint and/or path segment. Should be less than 1.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.0] (0.01)`
- 默认值：`0.32`
- 单位：``


823. NPFG_TRACK_KEEP (INT32)
- 名称：NPFG_TRACK_KEEP (INT32)
- 参数描述：Enable track keeping excess wind handling logic
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


824. NPFG_UB_PERIOD (INT32)
- 名称：NPFG_UB_PERIOD (INT32)
- 参数描述：Enable automatic upper bound on the NPFG period Comment: Adapts period to maintain track keeping in variable winds and path curvature.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


825. NPFG_WIND_REG (INT32)
- 名称：NPFG_WIND_REG (INT32)
- 参数描述：Enable wind excess regulation Comment: Disabling this parameter further disables all other airspeed incrementation options.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


826. FW_PN_R_SLEW_MAX (FLOAT)
- 名称：FW_PN_R_SLEW_MAX (FLOAT)
- 参数描述：Path navigation roll slew rate limit Comment: The maximum change in roll angle setpoint per second.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (1)`
- 默认值：`90.0`
- 单位：`deg/s`


827. FW_POS_STK_CONF (INT32)
- 名称：FW_POS_STK_CONF (INT32)
- 参数描述：RC stick configuration fixed-wing Comment: Set RC/joystick configuration for fixed-wing manual position and altitude controlled flight. Bitmask:0: Alternative stick configuration (height rate on throttle stick, airspeed on pitch stick) 1: Enable airspeed setpoint via sticks in altitude and position flight mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`2`
- 单位：``


828. FW_R_LIM (FLOAT)
- 名称：FW_R_LIM (FLOAT)
- 参数描述：Maximum roll angle Comment: The maximum roll angle setpoint for setpoint for a height-rate or altitude controlled mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[35.0, 65.0] (0.5)`
- 默认值：`50.0`
- 单位：`deg`


829. FW_TKO_PITCH_MIN (FLOAT)
- 名称：FW_TKO_PITCH_MIN (FLOAT)
- 参数描述：Minimum pitch during takeoff
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-5.0, 30.0] (0.5)`
- 默认值：`10.0`
- 单位：`deg`


830. FW_ACRO_X_MAX (FLOAT)
- 名称：FW_ACRO_X_MAX (FLOAT)
- 参数描述：Acro body roll max rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, 720]`
- 默认值：`90`
- 单位：`deg`


831. FW_ACRO_YAW_EN (INT32)
- 名称：FW_ACRO_YAW_EN (INT32)
- 参数描述：Enable yaw rate controller in Acro Comment: If this parameter is set to 1, the yaw rate controller is enabled in Fixed-wing Acro mode. Otherwise the pilot commands directly the yaw actuator. It is disabled by default because an active yaw rate controller will fight against the natural turn coordination of the plane.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


832. FW_ACRO_Y_MAX (FLOAT)
- 名称：FW_ACRO_Y_MAX (FLOAT)
- 参数描述：Acro body pitch max rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, 720]`
- 默认值：`90`
- 单位：`deg`


833. FW_ACRO_Z_MAX (FLOAT)
- 名称：FW_ACRO_Z_MAX (FLOAT)
- 参数描述：Acro body yaw max rate setpoint
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, 720]`
- 默认值：`45`
- 单位：`deg`


834. FW_ARSP_MODE (INT32)
- 名称：FW_ARSP_MODE (INT32)
- 参数描述：Airspeed mode Comment: On vehicles without airspeed sensor this parameter can be used to enable flying without an airspeed reading 参数对照:0: Use airspeed in controller 1: Do not use airspeed in controller
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


835. FW_ARSP_SCALE_EN (INT32)
- 名称：FW_ARSP_SCALE_EN (INT32)
- 参数描述：Enable airspeed scaling Comment: This enables a logic that automatically adjusts the output of the rate controller to take into account the real torque produced by an aerodynamic control surface given the current deviation from the trim airspeed (FW_AIRSPD_TRIM). Enable when using aerodynamic control surfaces (e.g.: plane) Disable when using rotor wings (e.g.: autogyro)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


836. FW_BAT_SCALE_EN (INT32)
- 名称：FW_BAT_SCALE_EN (INT32)
- 参数描述：Enable throttle scale by battery level Comment: This compensates for voltage drop of the battery over time by attempting to normalize performance across the operating range of the battery.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


837. FW_DTRIM_P_VMAX (FLOAT)
- 名称：FW_DTRIM_P_VMAX (FLOAT)
- 参数描述：Pitch trim increment at maximum airspeed Comment: This increment is added to TRIM_PITCH when airspeed is FW_AIRSPD_MAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


838. FW_DTRIM_P_VMIN (FLOAT)
- 名称：FW_DTRIM_P_VMIN (FLOAT)
- 参数描述：Pitch trim increment at minimum airspeed Comment: This increment is added to TRIM_PITCH when airspeed is FW_AIRSPD_MIN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


839. FW_DTRIM_R_VMAX (FLOAT)
- 名称：FW_DTRIM_R_VMAX (FLOAT)
- 参数描述：Roll trim increment at maximum airspeed Comment: This increment is added to TRIM_ROLL when airspeed is FW_AIRSPD_MAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


840. FW_DTRIM_R_VMIN (FLOAT)
- 名称：FW_DTRIM_R_VMIN (FLOAT)
- 参数描述：Roll trim increment at minimum airspeed Comment: This increment is added to TRIM_ROLL when airspeed is FW_AIRSPD_MIN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


841. FW_DTRIM_Y_VMAX (FLOAT)
- 名称：FW_DTRIM_Y_VMAX (FLOAT)
- 参数描述：Yaw trim increment at maximum airspeed Comment: This increment is added to TRIM_YAW when airspeed is FW_AIRSPD_MAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


842. FW_DTRIM_Y_VMIN (FLOAT)
- 名称：FW_DTRIM_Y_VMIN (FLOAT)
- 参数描述：Yaw trim increment at minimum airspeed Comment: This increment is added to TRIM_YAW when airspeed is FW_AIRSPD_MIN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-0.5, 0.5] (0.01)`
- 默认值：`0.0`
- 单位：``


843. FW_FLAPS_LND_SCL (FLOAT)
- 名称：FW_FLAPS_LND_SCL (FLOAT)
- 参数描述：Flaps setting during landing Comment: Sets a fraction of full flaps during landing. Also applies to flaperons if enabled in the mixer/allocation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`1.0`
- 单位：`norm`


844. FW_FLAPS_TO_SCL (FLOAT)
- 名称：FW_FLAPS_TO_SCL (FLOAT)
- 参数描述：Flaps setting during take-off Comment: Sets a fraction of full flaps during take-off. Also applies to flaperons if enabled in the mixer/allocation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.0`
- 单位：`norm`


845. FW_MAN_P_SC (FLOAT)
- 名称：FW_MAN_P_SC (FLOAT)
- 参数描述：Manual pitch scale Comment: Scale factor applied to the desired pitch actuator command in full manual mode. This parameter allows to adjust the throws of the control surfaces.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`1.0`
- 单位：`norm`


846. FW_MAN_R_SC (FLOAT)
- 名称：FW_MAN_R_SC (FLOAT)
- 参数描述：Manual roll scale Comment: Scale factor applied to the desired roll actuator command in full manual mode. This parameter allows to adjust the throws of the control surfaces.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`1.0`
- 单位：`norm`


847. FW_MAN_Y_SC (FLOAT)
- 名称：FW_MAN_Y_SC (FLOAT)
- 参数描述：Manual yaw scale Comment: Scale factor applied to the desired yaw actuator command in full manual mode. This parameter allows to adjust the throws of the control surfaces.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`1.0`
- 单位：`norm`


848. FW_PR_D (FLOAT)
- 名称：FW_PR_D (FLOAT)
- 参数描述：Pitch rate derivative gain Comment: Pitch rate differential gain.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.`
- 单位：`%/rad/s`


849. FW_PR_FF (FLOAT)
- 名称：FW_PR_FF (FLOAT)
- 参数描述：Pitch rate feed forward Comment: Direct feed forward from rate setpoint to control surface output
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (0.05)`
- 默认值：`0.5`
- 单位：`%/rad/s`


850. FW_PR_I (FLOAT)
- 名称：FW_PR_I (FLOAT)
- 参数描述：Pitch rate integrator gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.1`
- 单位：`%/rad`


851. FW_PR_IMAX (FLOAT)
- 名称：FW_PR_IMAX (FLOAT)
- 参数描述：Pitch rate integrator limit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.05)`
- 默认值：`0.4`
- 单位：``


852. FW_PR_P (FLOAT)
- 名称：FW_PR_P (FLOAT)
- 参数描述：Pitch rate proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.08`
- 单位：`%/rad/s`


853. FW_RLL_TO_YAW_FF (FLOAT)
- 名称：FW_RLL_TO_YAW_FF (FLOAT)
- 参数描述：Roll control to yaw control feedforward gain Comment: This gain can be used to counteract the "adverse yaw" effect for fixed wings. When the plane enters a roll it will tend to yaw the nose out of the turn. This gain enables the use of a yaw actuator to counteract this effect.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.0`
- 单位：``


854. FW_RR_D (FLOAT)
- 名称：FW_RR_D (FLOAT)
- 参数描述：Roll rate derivative gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.0`
- 单位：`%/rad/s`


855. FW_RR_FF (FLOAT)
- 名称：FW_RR_FF (FLOAT)
- 参数描述：Roll rate feed forward Comment: Direct feed forward from rate setpoint to control surface output.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (0.05)`
- 默认值：`0.5`
- 单位：`%/rad/s`


856. FW_RR_I (FLOAT)
- 名称：FW_RR_I (FLOAT)
- 参数描述：Roll rate integrator gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.01)`
- 默认值：`0.1`
- 单位：`%/rad`


857. FW_RR_IMAX (FLOAT)
- 名称：FW_RR_IMAX (FLOAT)
- 参数描述：Roll integrator limit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.05)`
- 默认值：`0.2`
- 单位：``


858. FW_RR_P (FLOAT)
- 名称：FW_RR_P (FLOAT)
- 参数描述：Roll rate proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.05`
- 单位：`%/rad/s`


859. FW_SPOILERS_MAN (INT32)
- 名称：FW_SPOILERS_MAN (INT32)
- 参数描述：Spoiler input in manual flight Comment: Chose source for manual setting of spoilers in manual flight modes. 参数对照:0: Disabled 1: Flaps channel 2: Aux1
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


860. FW_YR_D (FLOAT)
- 名称：FW_YR_D (FLOAT)
- 参数描述：Yaw rate derivative gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.0`
- 单位：`%/rad/s`


861. FW_YR_FF (FLOAT)
- 名称：FW_YR_FF (FLOAT)
- 参数描述：Yaw rate feed forward Comment: Direct feed forward from rate setpoint to control surface output
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0] (0.05)`
- 默认值：`0.3`
- 单位：`%/rad/s`


862. FW_YR_I (FLOAT)
- 名称：FW_YR_I (FLOAT)
- 参数描述：Yaw rate integrator gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.5)`
- 默认值：`0.1`
- 单位：`%/rad`


863. FW_YR_IMAX (FLOAT)
- 名称：FW_YR_IMAX (FLOAT)
- 参数描述：Yaw rate integrator limit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.05)`
- 默认值：`0.2`
- 单位：``


864. FW_YR_P (FLOAT)
- 名称：FW_YR_P (FLOAT)
- 参数描述：Yaw rate proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.005)`
- 默认值：`0.05`
- 单位：`%/rad/s`


865. FW_AIRSPD_MAX (FLOAT)
- 名称：FW_AIRSPD_MAX (FLOAT)
- 参数描述：Maximum Airspeed (CAS) Comment: The maximal airspeed (calibrated airspeed) the user is able to command.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, ?] (0.5)`
- 默认值：`20.0`
- 单位：`m/s`


866. FW_AIRSPD_MIN (FLOAT)
- 名称：FW_AIRSPD_MIN (FLOAT)
- 参数描述：Minimum Airspeed (CAS) Comment: The minimal airspeed (calibrated airspeed) the user is able to command. Further, if the airspeed falls below this value, the TECS controller will try to increase airspeed more aggressively. Should be set (with some margin) above the vehicle stall speed. This value corresponds to the desired minimum speed with the default load factor (level flight, default weight), and is automatically adapated to the current load factor (calculated from roll setpoint and WEIGHT_GROSS/WEIGHT_BASE).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, ?] (0.5)`
- 默认值：`10.0`
- 单位：`m/s`


867. FW_AIRSPD_STALL (FLOAT)
- 名称：FW_AIRSPD_STALL (FLOAT)
- 参数描述：Stall Airspeed (CAS) Comment: The stall airspeed (calibrated airspeed) of the vehicle. It is used for airspeed sensor failure detection and for the control surface scaling airspeed limits.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, ?] (0.5)`
- 默认值：`7.0`
- 单位：`m/s`


868. FW_AIRSPD_TRIM (FLOAT)
- 名称：FW_AIRSPD_TRIM (FLOAT)
- 参数描述：Trim (Cruise) Airspeed Comment: The trim CAS (calibrated airspeed) of the vehicle. If an airspeed controller is active, this is the default airspeed setpoint that the controller will try to achieve.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, ?] (0.5)`
- 默认值：`15.0`
- 单位：`m/s`


869. FW_GND_SPD_MIN (FLOAT)
- 名称：FW_GND_SPD_MIN (FLOAT)
- 参数描述：Minimum groundspeed Comment: The controller will increase the commanded airspeed to maintain this minimum groundspeed to the next waypoint.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 40] (0.5)`
- 默认值：`5.0`
- 单位：`m/s`


870. FW_P_LIM_MAX (FLOAT)
- 名称：FW_P_LIM_MAX (FLOAT)
- 参数描述：Maximum pitch angle Comment: The maximum pitch angle setpoint setpoint for a height-rate or altitude controlled mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 60.0] (0.5)`
- 默认值：`30.0`
- 单位：`deg`


871. FW_P_LIM_MIN (FLOAT)
- 名称：FW_P_LIM_MIN (FLOAT)
- 参数描述：Minimum pitch angle Comment: The minimum pitch angle setpoint for a height-rate or altitude controlled mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-60.0, 0.0] (0.5)`
- 默认值：`-30.0`
- 单位：`deg`


872. FW_THR_ASPD_MAX (FLOAT)
- 名称：FW_THR_ASPD_MAX (FLOAT)
- 参数描述：Throttle at max airspeed Comment: Required throttle for level flight at maximum airspeed FW_AIRSPD_MAX (sea level, standard atmosphere) Set to 0 to disable mapping of airspeed to trim throttle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.`
- 单位：``


873. FW_THR_ASPD_MIN (FLOAT)
- 名称：FW_THR_ASPD_MIN (FLOAT)
- 参数描述：Throttle at min airspeed Comment: Required throttle for level flight at minimum airspeed FW_AIRSPD_MIN (sea level, standard atmosphere) Set to 0 to disable mapping of airspeed to trim throttle below FW_AIRSPD_TRIM.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.`
- 单位：``


874. FW_THR_IDLE (FLOAT)
- 名称：FW_THR_IDLE (FLOAT)
- 参数描述：Idle throttle Comment: This is the minimum throttle while on the ground For aircraft with internal combustion engines, this parameter should be set above the desired idle rpm. For electric motors, idle should typically be set to zero. Note that in automatic modes, "landed" conditions will engage idle throttle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.4] (0.01)`
- 默认值：`0.0`
- 单位：`norm`


875. FW_THR_MAX (FLOAT)
- 名称：FW_THR_MAX (FLOAT)
- 参数描述：Throttle limit max Comment: Maximum throttle limit in altitude controlled modes. Should be set accordingly to achieve FW_T_CLMB_MAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`1.0`
- 单位：`norm`


876. FW_THR_MIN (FLOAT)
- 名称：FW_THR_MIN (FLOAT)
- 参数描述：Throttle limit min Comment: Minimum throttle limit in altitude controlled modes. Usually set to 0 but can be increased to prevent the motor from stopping when descending, which can increase achievable descent rates. For aircraft with internal combustion engine this parameter should be set for desired idle rpm.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.0`
- 单位：`norm`


877. FW_THR_SLEW_MAX (FLOAT)
- 名称：FW_THR_SLEW_MAX (FLOAT)
- 参数描述：Throttle max slew rate Comment: Maximum slew rate for the commanded throttle
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.0`
- 单位：``


878. FW_THR_TRIM (FLOAT)
- 名称：FW_THR_TRIM (FLOAT)
- 参数描述：Trim throttle Comment: This is the throttle setting required to achieve FW_AIRSPD_TRIM during level flight.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.6`
- 单位：`norm`


879. FW_TKO_AIRSPD (FLOAT)
- 名称：FW_TKO_AIRSPD (FLOAT)
- 参数描述：Takeoff Airspeed Comment: The calibrated airspeed setpoint TECS will stabilize to during the takeoff climbout. If set <= 0.0, FW_AIRSPD_MIN will be set by default.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, ?] (0.1)`
- 默认值：`-1.0`
- 单位：`m/s`


880. FW_T_ALT_TC (FLOAT)
- 名称：FW_T_ALT_TC (FLOAT)
- 参数描述：Altitude error time constant
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2.0, ?] (0.5)`
- 默认值：`5.0`
- 单位：``


881. FW_T_CLMB_MAX (FLOAT)
- 名称：FW_T_CLMB_MAX (FLOAT)
- 参数描述：Maximum climb rate Comment: This is the maximum climb rate that the aircraft can achieve with the throttle set to THR_MAX and the airspeed set to the trim value. For electric aircraft make sure this number can be achieved towards the end of flight when the battery voltage has reduced.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 15.0] (0.5)`
- 默认值：`5.0`
- 单位：`m/s`


882. FW_T_CLMB_R_SP (FLOAT)
- 名称：FW_T_CLMB_R_SP (FLOAT)
- 参数描述：Default target climbrate Comment: The default rate at which the vehicle will climb in autonomous modes to achieve altitude setpoints. In manual modes this defines the maximum rate at which the altitude setpoint can be increased.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 15] (0.01)`
- 默认值：`3.0`
- 单位：`m/s`


883. FW_T_HRATE_FF (FLOAT)
- 名称：FW_T_HRATE_FF (FLOAT)
- 参数描述：Height rate feed forward
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.05)`
- 默认值：`0.3`
- 单位：``


884. FW_T_I_GAIN_PIT (FLOAT)
- 名称：FW_T_I_GAIN_PIT (FLOAT)
- 参数描述：Integrator gain pitch Comment: This is the integrator gain on the pitch part of the control loop. Increasing this gain increases the speed at which speed and height offsets are trimmed out, but reduces damping and increases overshoot. Set this value to zero to completely disable all integrator action.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.05)`
- 默认值：`0.1`
- 单位：``


885. FW_T_I_GAIN_THR (FLOAT)
- 名称：FW_T_I_GAIN_THR (FLOAT)
- 参数描述：Integrator gain throttle Comment: This is the integrator gain on the throttle part of the control loop. Increasing this gain increases the speed at which speed and height offsets are trimmed out, but reduces damping and increases overshoot. Set this value to zero to completely disable all integrator action.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.05)`
- 默认值：`0.05`
- 单位：``


886. FW_T_PTCH_DAMP (FLOAT)
- 名称：FW_T_PTCH_DAMP (FLOAT)
- 参数描述：Pitch damping factor Comment: This is the damping gain for the pitch demand loop. Increase to add damping to correct for oscillations in height. The default value of 0.0 will work well provided the pitch to servo controller has been tuned properly.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.1)`
- 默认值：`0.1`
- 单位：``


887. FW_T_RLL2THR (FLOAT)
- 名称：FW_T_RLL2THR (FLOAT)
- 参数描述：Roll -> Throttle feedforward Comment: Increasing this gain turn increases the amount of throttle that will be used to compensate for the additional drag created by turning. Ideally this should be set to  approximately 10 x the extra sink rate in m/s created by a 45 degree bank turn. Increase this gain if the aircraft initially loses energy in turns and reduce if the aircraft initially gains energy in turns. Efficient high aspect-ratio aircraft (eg powered sailplanes) can use a lower value, whereas inefficient low aspect-ratio models (eg delta wings) can use a higher value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 20.0] (0.5)`
- 默认值：`15.0`
- 单位：``


888. FW_T_SEB_R_FF (FLOAT)
- 名称：FW_T_SEB_R_FF (FLOAT)
- 参数描述：Specific total energy balance rate feedforward gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 3] (0.01)`
- 默认值：`1.0`
- 单位：``


889. FW_T_SINK_MAX (FLOAT)
- 名称：FW_T_SINK_MAX (FLOAT)
- 参数描述：Maximum descent rate Comment: This sets the maximum descent rate that the controller will use. If this value is too large, the aircraft can over-speed on descent. This should be set to a value that can be achieved without exceeding the lower pitch angle limit and without over-speeding the aircraft.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 15.0] (0.5)`
- 默认值：`5.0`
- 单位：`m/s`


890. FW_T_SINK_MIN (FLOAT)
- 名称：FW_T_SINK_MIN (FLOAT)
- 参数描述：Minimum descent rate Comment: This is the sink rate of the aircraft with the throttle set to THR_MIN and flown at the same airspeed as used to measure FW_T_CLMB_MAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 5.0] (0.5)`
- 默认值：`2.0`
- 单位：`m/s`


891. FW_T_SINK_R_SP (FLOAT)
- 名称：FW_T_SINK_R_SP (FLOAT)
- 参数描述：Default target sinkrate Comment: The default rate at which the vehicle will sink in autonomous modes to achieve altitude setpoints. In manual modes this defines the maximum rate at which the altitude setpoint can be decreased.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 15] (0.01)`
- 默认值：`2.0`
- 单位：`m/s`


892. FW_T_SPDWEIGHT (FLOAT)
- 名称：FW_T_SPDWEIGHT (FLOAT)
- 参数描述：Speed <--> Altitude priority Comment: This parameter adjusts the amount of weighting that the pitch control applies to speed vs height errors. Setting it to 0.0 will cause the pitch control to control height and ignore speed errors. This will normally improve height accuracy but give larger airspeed errors. Setting it to 2.0 will cause the pitch control loop to control speed and ignore height errors. This will normally reduce airspeed errors, but give larger height errors. The default value of 1.0 allows the pitch control to simultaneously control height and speed. Set to 2 for gliders.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (1.0)`
- 默认值：`1.0`
- 单位：``


893. FW_T_SPD_DEV_STD (FLOAT)
- 名称：FW_T_SPD_DEV_STD (FLOAT)
- 参数描述：Airspeed rate measurement standard deviation for airspeed filter Comment: This is the measurement standard deviation for the airspeed rate used in the airspeed filter in TECS.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 10.0] (0.1)`
- 默认值：`0.2`
- 单位：`m/s^2`


894. FW_T_SPD_PRC_STD (FLOAT)
- 名称：FW_T_SPD_PRC_STD (FLOAT)
- 参数描述：Process noise standard deviation for the airspeed rate in the airspeed filter Comment: This is the process noise standard deviation in the airspeed filter filter defining the noise in the airspeed rate for the constant airspeed rate model. This is used to define how much the airspeed and the airspeed rate are filtered. The smaller the value the more the measurements are smoothed with the drawback for delays.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 10.0] (0.1)`
- 默认值：`0.2`
- 单位：`m/s^2`


895. FW_T_SPD_STD (FLOAT)
- 名称：FW_T_SPD_STD (FLOAT)
- 参数描述：Airspeed measurement standard deviation for airspeed filter Comment: This is the measurement standard deviation for the airspeed used in the airspeed filter in TECS.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 10.0] (0.1)`
- 默认值：`0.2`
- 单位：`m/s`


896. FW_T_STE_R_TC (FLOAT)
- 名称：FW_T_STE_R_TC (FLOAT)
- 参数描述：Specific total energy rate first order filter time constant Comment: This filter is applied to the specific total energy rate used for throttle damping.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2] (0.01)`
- 默认值：`0.4`
- 单位：``


897. FW_T_TAS_TC (FLOAT)
- 名称：FW_T_TAS_TC (FLOAT)
- 参数描述：True airspeed error time constant
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2.0, ?] (0.5)`
- 默认值：`5.0`
- 单位：``


898. FW_T_THR_DAMP (FLOAT)
- 名称：FW_T_THR_DAMP (FLOAT)
- 参数描述：Throttle damping factor Comment: This is the damping gain for the throttle demand loop. Increase to add damping to correct for oscillations in speed and height.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.1)`
- 默认值：`0.1`
- 单位：``


899. FW_T_VERT_ACC (FLOAT)
- 名称：FW_T_VERT_ACC (FLOAT)
- 参数描述：Maximum vertical acceleration Comment: This is the maximum vertical acceleration (in m/s/s) either up or down that the controller will use to correct speed or height errors. The default value of 7 m/s/s (equivalent to +- 0.7 g) allows for reasonably aggressive pitch changes if required to recover from under-speed conditions.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10.0] (0.5)`
- 默认值：`7.0`
- 单位：`m/s^2`


900. FW_WIND_ARSP_SC (FLOAT)
- 名称：FW_WIND_ARSP_SC (FLOAT)
- 参数描述：Wind-based airspeed scaling factor Comment: Multiplying this factor with the current absolute wind estimate gives the airspeed offset added to the minimum airspeed setpoint limit. This helps to make the system more robust against disturbances (turbulence) in high wind. Only applies to AUTO flight mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (0.01)`
- 默认值：`0.`
- 单位：``


901. FD_ACT_EN (INT32)
- 名称：FD_ACT_EN (INT32)
- 参数描述：Enable Actuator Failure check Comment: If enabled, failure detector will verify that for motors, a minimum amount of ESC current per throttle level is being consumed. Otherwise this indicates an motor failure. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


902. FD_ACT_MOT_C2T (FLOAT)
- 名称：FD_ACT_MOT_C2T (FLOAT)
- 参数描述：Motor Failure Current/Throttle Threshold Comment: Motor failure triggers only below this current value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 50.0] (1)`
- 默认值：`2.0`
- 单位：`A/%`


903. FD_ACT_MOT_THR (FLOAT)
- 名称：FD_ACT_MOT_THR (FLOAT)
- 参数描述：Motor Failure Throttle Threshold Comment: Motor failure triggers only above this throttle value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.2`
- 单位：`norm`


904. FD_ACT_MOT_TOUT (INT32)
- 名称：FD_ACT_MOT_TOUT (INT32)
- 参数描述：Motor Failure Time Threshold Comment: Motor failure triggers only if the throttle threshold and the current to throttle threshold are violated for this time.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, 10000] (100)`
- 默认值：`100`
- 单位：`ms`


905. FD_ESCS_EN (INT32)
- 名称：FD_ESCS_EN (INT32)
- 参数描述：Enable checks on ESCs that report their arming state Comment: If enabled, failure detector will verify that all the ESCs have successfully armed when the vehicle has transitioned to the armed state. Timeout for receiving an acknowledgement from the ESCs is 0.3s, if no feedback is received the failure detector will auto disarm the vehicle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


906. FD_EXT_ATS_EN (INT32)
- 名称：FD_EXT_ATS_EN (INT32)
- 参数描述：Enable PWM input on for engaging failsafe from an external automatic trigger system (ATS) Comment: Enabled on either AUX5 or MAIN5 depending on board. External ATS is required by ASTM F3322-18. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


907. FD_EXT_ATS_TRIG (INT32)
- 名称：FD_EXT_ATS_TRIG (INT32)
- 参数描述：The PWM threshold from external automatic trigger system for engaging failsafe Comment: External ATS is required by ASTM F3322-18.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1900`
- 单位：`µs`


908. FD_FAIL_P (INT32)
- 名称：FD_FAIL_P (INT32)
- 参数描述：FailureDetector Max Pitch Comment: Maximum pitch angle before FailureDetector triggers the attitude_failure flag. The flag triggers flight termination (if @CBRK_FLIGHTTERM = 0), which sets outputs to their failsafe values. On takeoff the flag triggers lockdown (irrespective of @CBRK_FLIGHTTERM), which disarms motors but does not set outputs to failsafe values. Setting this parameter to 0 disables the check
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 180]`
- 默认值：`60`
- 单位：`deg`


909. FD_FAIL_P_TTRI (FLOAT)
- 名称：FD_FAIL_P_TTRI (FLOAT)
- 参数描述：Pitch failure trigger time Comment: Seconds (decimal) that pitch has to exceed FD_FAIL_P before being considered as a failure.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.02, 5]`
- 默认值：`0.3`
- 单位：`s`


910. FD_FAIL_R (INT32)
- 名称：FD_FAIL_R (INT32)
- 参数描述：FailureDetector Max Roll Comment: Maximum roll angle before FailureDetector triggers the attitude_failure flag. The flag triggers flight termination (if @CBRK_FLIGHTTERM = 0), which sets outputs to their failsafe values. On takeoff the flag triggers lockdown (irrespective of @CBRK_FLIGHTTERM), which disarms motors but does not set outputs to failsafe values. Setting this parameter to 0 disables the check
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 180]`
- 默认值：`60`
- 单位：`deg`


911. FD_FAIL_R_TTRI (FLOAT)
- 名称：FD_FAIL_R_TTRI (FLOAT)
- 参数描述：Roll failure trigger time Comment: Seconds (decimal) that roll has to exceed FD_FAIL_R before being considered as a failure.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.02, 5]`
- 默认值：`0.3`
- 单位：`s`


912. FD_IMB_PROP_THR (INT32)
- 名称：FD_IMB_PROP_THR (INT32)
- 参数描述：Imbalanced propeller check threshold Comment: Value at which the imbalanced propeller metric (based on horizontal and vertical acceleration variance) triggers a failure Setting this value to 0 disables the feature.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000] (1)`
- 默认值：`30`
- 单位：``


913. MC_ORBIT_RAD_MAX (FLOAT)
- 名称：MC_ORBIT_RAD_MAX (FLOAT)
- 参数描述：Maximum radius of orbit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10000.0] (0.5)`
- 默认值：`1000.0`
- 单位：`m`


914. FLW_TGT_ALT_M (INT32)
- 名称：FLW_TGT_ALT_M (INT32)
- 参数描述：Altitude control mode Comment: Maintain altitude or track target's altitude. When maintaining the altitude, the drone can crash into terrain when the target moves uphill. When tracking the target's altitude, the follow altitude FLW_TGT_HT should be high enough to prevent terrain collisions due to GPS inaccuracies of the target. 参数对照:0: 2D Tracking: Maintain constant altitude relative to home and track XY position only 1: 2D + Terrain: Maintain constant altitude relative to terrain below and track XY position 2: 3D Tracking: Track target's altitude (be aware that GPS altitude bias usually makes this useless)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


915. FLW_TGT_DST (FLOAT)
- 名称：FLW_TGT_DST (FLOAT)
- 参数描述：Distance to follow target from Comment: The distance in meters to follow the target at
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, ?]`
- 默认值：`8.0`
- 单位：`m`


916. FLW_TGT_FA (FLOAT)
- 名称：FLW_TGT_FA (FLOAT)
- 参数描述：Follow Angle setting in degrees Comment: Angle to follow the target from. 0.0 Equals straight in front of the target's course (direction of motion) and the angle increases in clockwise direction, meaning Right-side would be 90.0 degrees while Left-side is -90.0 degrees Note: When the user force sets the angle out of the min/max range, it will be wrapped (e.g. 480 -> 120) in the range to gracefully handle the out of range.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-180.0, 180.0]`
- 默认值：`180.0`
- 单位：``


917. FLW_TGT_HT (FLOAT)
- 名称：FLW_TGT_HT (FLOAT)
- 参数描述：Follow target height Comment: Following height above the target
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[8.0, ?]`
- 默认值：`8.0`
- 单位：`m`


918. FLW_TGT_MAX_VEL (FLOAT)
- 名称：FLW_TGT_MAX_VEL (FLOAT)
- 参数描述：Maximum tangential velocity setting for generating the follow orbit trajectory Comment: This is the maximum tangential velocity the drone will circle around the target whenever an orbit angle setpoint changes. Higher value means more aggressive follow behavior.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 20.0]`
- 默认值：`5.0`
- 单位：``


919. FLW_TGT_RS (FLOAT)
- 名称：FLW_TGT_RS (FLOAT)
- 参数描述：Responsiveness to target movement in Target Estimator Comment: lower values increase the responsiveness to changing position, but also ignore less noise
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0]`
- 默认值：`0.1`
- 单位：``


920. GPS_1_CONFIG (INT32)
- 名称：GPS_1_CONFIG (INT32)
- 参数描述：Serial Configuration for Main GPS Comment: Configure on which serial port to run Main GPS. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`201`
- 单位：``


921. GPS_1_GNSS (INT32)
- 名称：GPS_1_GNSS (INT32)
- 参数描述：GNSS Systems for Primary GPS (integer bitmask) Comment: This integer bitmask controls the set of GNSS systems used by the receiver. Check your receiver's documentation on how many systems are supported to be used in parallel. Currently this functionality is just implemented for u-blox receivers. When no bits are set, the receiver's default configuration should be used. Set bits true to enable: 0 : Use GPS (with QZSS) 1 : Use SBAS (multiple GPS augmentation systems) 2 : Use Galileo 3 : Use BeiDou 4 : Use GLONASS Bitmask:0: GPS (with QZSS) 1: SBAS 2: Galileo 3: BeiDou 4: GLONASS Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 31]`
- 默认值：`0`
- 单位：``


922. GPS_1_PROTOCOL (INT32)
- 名称：GPS_1_PROTOCOL (INT32)
- 参数描述：Protocol for Main GPS Comment: Select the GPS protocol over serial. Auto-detection will probe all protocols, and thus is a bit slower. 参数对照:0: Auto detect 1: u-blox 2: MTK 3: Ashtech / Trimble 4: Emlid Reach 5: Femtomes 6: NMEA (generic) 7: Septentrio (SBF) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 7]`
- 默认值：`1`
- 单位：``


923. GPS_2_CONFIG (INT32)
- 名称：GPS_2_CONFIG (INT32)
- 参数描述：Serial Configuration for Secondary GPS Comment: Configure on which serial port to run Secondary GPS. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


924. GPS_2_GNSS (INT32)
- 名称：GPS_2_GNSS (INT32)
- 参数描述：GNSS Systems for Secondary GPS (integer bitmask) Comment: This integer bitmask controls the set of GNSS systems used by the receiver. Check your receiver's documentation on how many systems are supported to be used in parallel. Currently this functionality is just implemented for u-blox receivers. When no bits are set, the receiver's default configuration should be used. Set bits true to enable: 0 : Use GPS (with QZSS) 1 : Use SBAS (multiple GPS augmentation systems) 2 : Use Galileo 3 : Use BeiDou 4 : Use GLONASS Bitmask:0: GPS (with QZSS) 1: SBAS 2: Galileo 3: BeiDou 4: GLONASS Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 31]`
- 默认值：`0`
- 单位：``


925. GPS_2_PROTOCOL (INT32)
- 名称：GPS_2_PROTOCOL (INT32)
- 参数描述：Protocol for Secondary GPS Comment: Select the GPS protocol over serial. Auto-detection will probe all protocols, and thus is a bit slower. 参数对照:0: Auto detect 1: u-blox 2: MTK 3: Ashtech / Trimble 4: Emlid Reach 5: Femtomes 6: NMEA (generic) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`1`
- 单位：``


926. GPS_DUMP_COMM (INT32)
- 名称：GPS_DUMP_COMM (INT32)
- 参数描述：Log GPS communication data Comment: If this is set to 1, all GPS communication data will be published via uORB, and written to the log file as gps_dump message. If this is set to 2, the main GPS is configured to output RTCM data, which is then logged as gps_dump and can be used for PPK. 参数对照:0: Disable 1: Full communication 2: RTCM output (PPK)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


927. GPS_PITCH_OFFSET (FLOAT)
- 名称：GPS_PITCH_OFFSET (FLOAT)
- 参数描述：Pitch offset for dual antenna GPS Comment: Vertical offsets can be compensated for by adjusting the Pitch offset (Septentrio). Note that this can be interpreted as the "roll" angle in case the antennas are aligned along the perpendicular axis. This occurs in situations where the two antenna ARPs may not be exactly at the same height in the vehicle reference frame. Since pitch is defined as the right-handed rotation about the vehicle Y axis, a situation where the main antenna is mounted lower than the aux antenna (assuming the default antenna setup) will result in a positive pitch. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90, 90]`
- 默认值：`0.`
- 单位：`deg`


928. GPS_SAT_INFO (INT32)
- 名称：GPS_SAT_INFO (INT32)
- 参数描述：Enable sat info (if available) Comment: Enable publication of satellite info (ORB_ID(satellite_info)) if possible. Not available on MTK. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


929. GPS_UBX_BAUD2 (INT32)
- 名称：GPS_UBX_BAUD2 (INT32)
- 参数描述：u-blox F9P UART2 Baudrate Comment: Select a baudrate for the F9P's UART2 port. In GPS_UBX_MODE 1, 2, and 3, the F9P's UART2 port is configured to send/receive RTCM corrections. Set this to 57600 if you want to attach a telemetry radio on UART2. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`230400`
- 单位：`B/s`


930. GPS_UBX_CFG_INTF (INT32)
- 名称：GPS_UBX_CFG_INTF (INT32)
- 参数描述：u-blox protocol configuration for interfaces   Bitmask:0: Enable I2C input protocol UBX 1: Enable I2C input protocol NMEA 2: Enable I2C input protocol RTCM3X 3: Enable I2C output protocol UBX 4: Enable I2C output protocol NMEA 5: Enable I2C output protocol RTCM3X Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 32]`
- 默认值：`0`
- 单位：``


931. GPS_UBX_DYNMODEL (INT32)
- 名称：GPS_UBX_DYNMODEL (INT32)
- 参数描述：u-blox GPS dynamic platform model Comment: u-blox receivers support different dynamic platform models to adjust the navigation engine to the expected application environment. 参数对照:2: stationary 4: automotive 6: airborne with <1g acceleration 7: airborne with <2g acceleration 8: airborne with <4g acceleration Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 9]`
- 默认值：`7`
- 单位：``


932. GPS_UBX_MODE (INT32)
- 名称：GPS_UBX_MODE (INT32)
- 参数描述：u-blox GPS Mode Comment: Select the u-blox configuration setup. Most setups will use the default, including RTK and dual GPS without heading. If rover has RTCM corrections from a static base (or other static correction source) coming in on UART2, then select Mode 5. The Heading mode requires 2 F9P devices to be attached. The main GPS will act as rover and output heading information, whereas the secondary will act as moving base. Modes 1 and 2 require each F9P UART1 to be connected to the Autopilot. In addition, UART2 on the F9P units are connected to each other. Modes 3 and 4 only require UART1 on each F9P connected to the Autopilot or Can Node. UART RX DMA is required. RTK is still possible with this setup. 参数对照:0: Default 1: Heading (Rover With Moving Base UART1 Connected To Autopilot, UART2 Connected To Moving Base) 2: Moving Base (UART1 Connected To Autopilot, UART2 Connected To Rover) 3: Heading (Rover With Moving Base UART1 Connected to Autopilot Or Can Node At 921600) 4: Moving Base (Moving Base UART1 Connected to Autopilot Or Can Node At 921600) 5: Rover with Static Base on UART2 (similar to Default, except coming in on UART2) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


933. GPS_YAW_OFFSET (FLOAT)
- 名称：GPS_YAW_OFFSET (FLOAT)
- 参数描述：Heading/Yaw offset for dual antenna GPS Comment: Heading offset angle for dual antenna GPS setups that support heading estimation. Set this to 0 if the antennas are parallel to the forward-facing direction of the vehicle and the rover (or Unicore primary) antenna is in front. The offset angle increases clockwise. Set this to 90 if the rover (or Unicore primary) antenna is placed on the right side of the vehicle and the moving base antenna is on the left side. (Note: the Unicore primary antenna is the one connected on the right as seen from the top). Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360]`
- 默认值：`0.`
- 单位：`deg`


934. PPS_CAP_ENABLE (INT32)
- 名称：PPS_CAP_ENABLE (INT32)
- 参数描述：PPS Capture Enable Comment: Enables the PPS capture module. This switches mode of FMU channel 7 to be the PPS input channel. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


935. GF_ACTION (INT32)
- 名称：GF_ACTION (INT32)
- 参数描述：Geofence violation action Comment: Note: Setting this value to 4 enables flight termination, which will kill the vehicle on violation of the fence. 参数对照:0: None 1: Warning 2: Hold mode 3: Return mode 4: Terminate 5: Land mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 5]`
- 默认值：`2`
- 单位：``


936. GF_ALTMODE (INT32)
- 名称：GF_ALTMODE (INT32)
- 参数描述：Geofence altitude mode Comment: Select which altitude (AMSL) source should be used for geofence calculations. 参数对照:0: Autopilot estimator global position altitude (GPS) 1: Raw barometer altitude (assuming standard atmospheric pressure)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


937. GF_COUNT (INT32)
- 名称：GF_COUNT (INT32)
- 参数描述：Geofence counter limit Comment: Set how many subsequent position measurements outside of the fence are needed before geofence violation is triggered
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 10] (1)`
- 默认值：`-1`
- 单位：``


938. GF_MAX_HOR_DIST (FLOAT)
- 名称：GF_MAX_HOR_DIST (FLOAT)
- 参数描述：Max horizontal distance in meters Comment: Maximum horizontal distance in meters the vehicle can be from home before triggering a geofence action. Disabled if 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10000] (1)`
- 默认值：`0`
- 单位：`m`


939. GF_MAX_VER_DIST (FLOAT)
- 名称：GF_MAX_VER_DIST (FLOAT)
- 参数描述：Max vertical distance in meters Comment: Maximum vertical distance in meters the vehicle can be from home before triggering a geofence action. Disabled if 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10000] (1)`
- 默认值：`0`
- 单位：`m`


940. GF_PREDICT (INT32)
- 名称：GF_PREDICT (INT32)
- 参数描述：[EXPERIMENTAL] Use Pre-emptive geofence triggering Comment: WARNING: This experimental feature may cause flyaways. Use at your own risk. Predict the motion of the vehicle and trigger the breach if it is determined that the current trajectory would result in a breach happening before the vehicle can make evasive maneuvers. The vehicle is then re-routed to a safe hold position (stop for multirotor, loiter for fixed wing).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


941. GF_SOURCE (INT32)
- 名称：GF_SOURCE (INT32)
- 参数描述：Geofence source Comment: Select which position source should be used. Selecting GPS instead of global position makes sure that there is no dependence on the position estimator 0 = global position, 1 = GPS 参数对照:0: GPOS 1: GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


942. CA_AIRFRAME (INT32)
- 名称：CA_AIRFRAME (INT32)
- 参数描述：Airframe selection Comment: Defines which mixer implementation to use. Some are generic, while others are specifically fit to a certain vehicle with a fixed set of actuators. 'Custom' should only be used if noting else can be used. 参数对照:0: Multirotor 1: Fixed-wing 2: Standard VTOL 3: Tiltrotor VTOL 4: Tailsitter VTOL 5: Rover (Ackermann) 6: Rover (Differential) 7: Motors (6DOF) 8: Multirotor with Tilt 9: Custom 10: Helicopter (tail ESC) 11: Helicopter (tail Servo) 12: Helicopter (Coaxial)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


943. CA_FAILURE_MODE (INT32)
- 名称：CA_FAILURE_MODE (INT32)
- 参数描述：Motor failure handling mode Comment: This is used to specify how to handle motor failures reported by failure detector. 参数对照:0: Ignore 1: Remove first failed motor from effectiveness
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


944. CA_HELI_PITCH_C0 (FLOAT)
- 名称：CA_HELI_PITCH_C0 (FLOAT)
- 参数描述：Collective pitch curve at position 0 Comment: Defines the collective pitch at the interval position 0 for a given thrust setpoint. Use negative values if the swash plate needs to move down to provide upwards thrust.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`-0.05`
- 单位：``


945. CA_HELI_PITCH_C1 (FLOAT)
- 名称：CA_HELI_PITCH_C1 (FLOAT)
- 参数描述：Collective pitch curve at position 1 Comment: Defines the collective pitch at the interval position 1 for a given thrust setpoint. Use negative values if the swash plate needs to move down to provide upwards thrust.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`0.0725`
- 单位：``


946. CA_HELI_PITCH_C2 (FLOAT)
- 名称：CA_HELI_PITCH_C2 (FLOAT)
- 参数描述：Collective pitch curve at position 2 Comment: Defines the collective pitch at the interval position 2 for a given thrust setpoint. Use negative values if the swash plate needs to move down to provide upwards thrust.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`0.2`
- 单位：``


947. CA_HELI_PITCH_C3 (FLOAT)
- 名称：CA_HELI_PITCH_C3 (FLOAT)
- 参数描述：Collective pitch curve at position 3 Comment: Defines the collective pitch at the interval position 3 for a given thrust setpoint. Use negative values if the swash plate needs to move down to provide upwards thrust.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`0.325`
- 单位：``


948. CA_HELI_PITCH_C4 (FLOAT)
- 名称：CA_HELI_PITCH_C4 (FLOAT)
- 参数描述：Collective pitch curve at position 4 Comment: Defines the collective pitch at the interval position 4 for a given thrust setpoint. Use negative values if the swash plate needs to move down to provide upwards thrust.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`0.45`
- 单位：``


949. CA_HELI_THR_C0 (FLOAT)
- 名称：CA_HELI_THR_C0 (FLOAT)
- 参数描述：Throttle curve at position 0 Comment: Defines the output throttle at the interval position 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.1)`
- 默认值：`1`
- 单位：``


950. CA_HELI_THR_C1 (FLOAT)
- 名称：CA_HELI_THR_C1 (FLOAT)
- 参数描述：Throttle curve at position 1 Comment: Defines the output throttle at the interval position 1.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.1)`
- 默认值：`1`
- 单位：``


951. CA_HELI_THR_C2 (FLOAT)
- 名称：CA_HELI_THR_C2 (FLOAT)
- 参数描述：Throttle curve at position 2 Comment: Defines the output throttle at the interval position 2.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.1)`
- 默认值：`1`
- 单位：``


952. CA_HELI_THR_C3 (FLOAT)
- 名称：CA_HELI_THR_C3 (FLOAT)
- 参数描述：Throttle curve at position 3 Comment: Defines the output throttle at the interval position 3.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.1)`
- 默认值：`1`
- 单位：``


953. CA_HELI_THR_C4 (FLOAT)
- 名称：CA_HELI_THR_C4 (FLOAT)
- 参数描述：Throttle curve at position 4 Comment: Defines the output throttle at the interval position 4.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.1)`
- 默认值：`1`
- 单位：``


954. CA_HELI_YAW_CCW (INT32)
- 名称：CA_HELI_YAW_CCW (INT32)
- 参数描述：Main rotor turns counter-clockwise Comment: Default configuration is for a clockwise turning main rotor and positive thrust of the tail rotor is expected to rotate the vehicle clockwise. Set this parameter to true if the tail rotor provides thrust in counter-clockwise direction which is mostly the case when the main rotor turns counter-clockwise.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


955. CA_HELI_YAW_CP_O (FLOAT)
- 名称：CA_HELI_YAW_CP_O (FLOAT)
- 参数描述：Offset for yaw compensation based on collective pitch Comment: This allows to specify which collective pitch command results in the least amount of rotor drag. This is used to increase the accuracy of the yaw drag torque compensation based on collective pitch by aligning the lowest rotor drag with zero compensation. For symmetric profile blades this is the command that results in exactly 0° collective blade angle. For lift profile blades this is typically a command resulting in slightly negative collective blade angle. tail_output += CA_HELI_YAW_CP_S * abs(collective_pitch - CA_HELI_YAW_CP_O)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-2, 2] (0.1)`
- 默认值：`0.0`
- 单位：``


956. CA_HELI_YAW_CP_S (FLOAT)
- 名称：CA_HELI_YAW_CP_S (FLOAT)
- 参数描述：Scale for yaw compensation based on collective pitch Comment: This allows to add a proportional factor of the collective pitch command to the yaw command. A negative value is needed when positive thrust of the tail rotor rotates the vehicle opposite to the main rotor turn direction. tail_output += CA_HELI_YAW_CP_S * abs(collective_pitch - CA_HELI_YAW_CP_O)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-2, 2] (0.1)`
- 默认值：`0.0`
- 单位：``


957. CA_HELI_YAW_TH_S (FLOAT)
- 名称：CA_HELI_YAW_TH_S (FLOAT)
- 参数描述：Scale for yaw compensation based on throttle Comment: This allows to add a proportional factor of the throttle command to the yaw command. A negative value is needed when positive thrust of the tail rotor rotates the vehicle opposite to the main rotor turn direction. tail_output += CA_HELI_YAW_TH_S * throttle
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-2, 2] (0.1)`
- 默认值：`0.0`
- 单位：``


958. CA_METHOD (INT32)
- 名称：CA_METHOD (INT32)
- 参数描述：Control allocation method Comment: Selects the algorithm and desaturation method. If set to Automtic, the selection is based on the airframe (CA_AIRFRAME). 参数对照:0: Pseudo-inverse with output clipping 1: Pseudo-inverse with sequential desaturation technique 2: Automatic
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


959. CA_R0_SLEW (FLOAT)
- 名称：CA_R0_SLEW (FLOAT)
- 参数描述：Motor 0 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


960. CA_R10_SLEW (FLOAT)
- 名称：CA_R10_SLEW (FLOAT)
- 参数描述：Motor 10 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


961. CA_R11_SLEW (FLOAT)
- 名称：CA_R11_SLEW (FLOAT)
- 参数描述：Motor 11 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


962. CA_R1_SLEW (FLOAT)
- 名称：CA_R1_SLEW (FLOAT)
- 参数描述：Motor 1 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


963. CA_R2_SLEW (FLOAT)
- 名称：CA_R2_SLEW (FLOAT)
- 参数描述：Motor 2 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


964. CA_R3_SLEW (FLOAT)
- 名称：CA_R3_SLEW (FLOAT)
- 参数描述：Motor 3 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


965. CA_R4_SLEW (FLOAT)
- 名称：CA_R4_SLEW (FLOAT)
- 参数描述：Motor 4 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


966. CA_R5_SLEW (FLOAT)
- 名称：CA_R5_SLEW (FLOAT)
- 参数描述：Motor 5 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


967. CA_R6_SLEW (FLOAT)
- 名称：CA_R6_SLEW (FLOAT)
- 参数描述：Motor 6 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


968. CA_R7_SLEW (FLOAT)
- 名称：CA_R7_SLEW (FLOAT)
- 参数描述：Motor 7 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


969. CA_R8_SLEW (FLOAT)
- 名称：CA_R8_SLEW (FLOAT)
- 参数描述：Motor 8 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


970. CA_R9_SLEW (FLOAT)
- 名称：CA_R9_SLEW (FLOAT)
- 参数描述：Motor 9 slew rate limit Comment: Minimum time allowed for the motor input signal to pass through the full output range. A value x means that the motor signal can only go from 0 to 1 in minimum x seconds (in case of reversible motors, the range is -1 to 1). Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.01)`
- 默认值：`0.0`
- 单位：``


971. CA_ROTOR0_AX (FLOAT)
- 名称：CA_ROTOR0_AX (FLOAT)
- 参数描述：Axis of rotor 0 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


972. CA_ROTOR0_AY (FLOAT)
- 名称：CA_ROTOR0_AY (FLOAT)
- 参数描述：Axis of rotor 0 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


973. CA_ROTOR0_AZ (FLOAT)
- 名称：CA_ROTOR0_AZ (FLOAT)
- 参数描述：Axis of rotor 0 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


974. CA_ROTOR0_CT (FLOAT)
- 名称：CA_ROTOR0_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 0 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


975. CA_ROTOR0_KM (FLOAT)
- 名称：CA_ROTOR0_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 0 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


976. CA_ROTOR0_PX (FLOAT)
- 名称：CA_ROTOR0_PX (FLOAT)
- 参数描述：Position of rotor 0 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


977. CA_ROTOR0_PY (FLOAT)
- 名称：CA_ROTOR0_PY (FLOAT)
- 参数描述：Position of rotor 0 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


978. CA_ROTOR0_PZ (FLOAT)
- 名称：CA_ROTOR0_PZ (FLOAT)
- 参数描述：Position of rotor 0 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


979. CA_ROTOR0_TILT (INT32)
- 名称：CA_ROTOR0_TILT (INT32)
- 参数描述：Rotor 0 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


980. CA_ROTOR10_AX (FLOAT)
- 名称：CA_ROTOR10_AX (FLOAT)
- 参数描述：Axis of rotor 10 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


981. CA_ROTOR10_AY (FLOAT)
- 名称：CA_ROTOR10_AY (FLOAT)
- 参数描述：Axis of rotor 10 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


982. CA_ROTOR10_AZ (FLOAT)
- 名称：CA_ROTOR10_AZ (FLOAT)
- 参数描述：Axis of rotor 10 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


983. CA_ROTOR10_CT (FLOAT)
- 名称：CA_ROTOR10_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 10 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


984. CA_ROTOR10_KM (FLOAT)
- 名称：CA_ROTOR10_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 10 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


985. CA_ROTOR10_PX (FLOAT)
- 名称：CA_ROTOR10_PX (FLOAT)
- 参数描述：Position of rotor 10 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


986. CA_ROTOR10_PY (FLOAT)
- 名称：CA_ROTOR10_PY (FLOAT)
- 参数描述：Position of rotor 10 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


987. CA_ROTOR10_PZ (FLOAT)
- 名称：CA_ROTOR10_PZ (FLOAT)
- 参数描述：Position of rotor 10 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


988. CA_ROTOR10_TILT (INT32)
- 名称：CA_ROTOR10_TILT (INT32)
- 参数描述：Rotor 10 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


989. CA_ROTOR11_AX (FLOAT)
- 名称：CA_ROTOR11_AX (FLOAT)
- 参数描述：Axis of rotor 11 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


990. CA_ROTOR11_AY (FLOAT)
- 名称：CA_ROTOR11_AY (FLOAT)
- 参数描述：Axis of rotor 11 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


991. CA_ROTOR11_AZ (FLOAT)
- 名称：CA_ROTOR11_AZ (FLOAT)
- 参数描述：Axis of rotor 11 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


992. CA_ROTOR11_CT (FLOAT)
- 名称：CA_ROTOR11_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 11 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


993. CA_ROTOR11_KM (FLOAT)
- 名称：CA_ROTOR11_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 11 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


994. CA_ROTOR11_PX (FLOAT)
- 名称：CA_ROTOR11_PX (FLOAT)
- 参数描述：Position of rotor 11 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


995. CA_ROTOR11_PY (FLOAT)
- 名称：CA_ROTOR11_PY (FLOAT)
- 参数描述：Position of rotor 11 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


996. CA_ROTOR11_PZ (FLOAT)
- 名称：CA_ROTOR11_PZ (FLOAT)
- 参数描述：Position of rotor 11 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


997. CA_ROTOR11_TILT (INT32)
- 名称：CA_ROTOR11_TILT (INT32)
- 参数描述：Rotor 11 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


998. CA_ROTOR1_AX (FLOAT)
- 名称：CA_ROTOR1_AX (FLOAT)
- 参数描述：Axis of rotor 1 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


999. CA_ROTOR1_AY (FLOAT)
- 名称：CA_ROTOR1_AY (FLOAT)
- 参数描述：Axis of rotor 1 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1000. CA_ROTOR1_AZ (FLOAT)
- 名称：CA_ROTOR1_AZ (FLOAT)
- 参数描述：Axis of rotor 1 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


