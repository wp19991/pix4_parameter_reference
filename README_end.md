# pix4_parameter_reference
> 使用gpt翻译pix4的参数，并且加上gpt的解释

> https://docs.px4.io/main/zh/advanced_config/parameter_reference.html

2001. SYS_CAL_BARO (INT32)
- 名称：SYS_CAL_BARO (INT32)
- 参数描述：Enable auto start of barometer thermal calibration at the next power up Comment: 0 : Set to 0 to do nothing 1 : Set to 1 to start a calibration at next boot This parameter is reset to zero when the temperature calibration starts. default (0, no calibration)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


2002. SYS_CAL_GYRO (INT32)
- 名称：SYS_CAL_GYRO (INT32)
- 参数描述：Enable auto start of rate gyro thermal calibration at the next power up Comment: 0 : Set to 0 to do nothing 1 : Set to 1 to start a calibration at next boot This parameter is reset to zero when the temperature calibration starts. default (0, no calibration)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


2003. SYS_CAL_TDEL (INT32)
- 名称：SYS_CAL_TDEL (INT32)
- 参数描述：Required temperature rise during thermal calibration Comment: A temperature increase greater than this value is required during calibration. Calibration will complete for each sensor when the temperature increase above the starting temperature exceeds the value set by SYS_CAL_TDEL. If the temperature rise is insufficient, the calibration will continue indefinitely and the board will need to be repowered to exit.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, ?]`
- 默认值：`24`
- 单位：`celcius`


2004. SYS_CAL_TMAX (INT32)
- 名称：SYS_CAL_TMAX (INT32)
- 参数描述：Maximum starting temperature for thermal calibration Comment: Temperature calibration will not start if the temperature of any sensor is higher than the value set by SYS_CAL_TMAX.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`10`
- 单位：`celcius`


2005. SYS_CAL_TMIN (INT32)
- 名称：SYS_CAL_TMIN (INT32)
- 参数描述：Minimum starting temperature for thermal calibration Comment: Temperature calibration for each sensor will ignore data if the temperature is lower than the value set by SYS_CAL_TMIN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5`
- 单位：`celcius`


2006. SYS_DM_BACKEND (INT32)
- 名称：SYS_DM_BACKEND (INT32)
- 参数描述：Dataman storage backend  Values:-1: Disabled 0: default (SD card) 1: RAM (not persistent) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2007. SYS_FAC_CAL_MODE (INT32)
- 名称：SYS_FAC_CAL_MODE (INT32)
- 参数描述：Enable factory calibration mode Comment: If enabled, future sensor calibrations will be stored to /fs/mtd_caldata. Note: this is only supported on boards with a separate calibration storage /fs/mtd_caldata. 参数对照:0: Disabled 1: All sensors 2: All sensors except mag
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2008. SYS_FAILURE_EN (INT32)
- 名称：SYS_FAILURE_EN (INT32)
- 参数描述：Enable failure injection Comment: If enabled allows MAVLink INJECT_FAILURE commands. WARNING: the failures can easily cause crashes and are to be used with caution!
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2009. SYS_HAS_BARO (INT32)
- 名称：SYS_HAS_BARO (INT32)
- 参数描述：Control if the vehicle has a barometer Comment: Disable this if the board has no barometer, such as some of the Omnibus F4 SD variants. If disabled, the preflight checks will not check for the presence of a barometer. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2010. SYS_HAS_GPS (INT32)
- 名称：SYS_HAS_GPS (INT32)
- 参数描述：Control if the vehicle has a GPS Comment: Disable this if the system has no GPS. If disabled, the sensors hub will not process sensor_gps, and GPS will not be available for the rest of the system. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2011. SYS_HAS_MAG (INT32)
- 名称：SYS_HAS_MAG (INT32)
- 参数描述：Control if the vehicle has a magnetometer Comment: Set this to 0 if the board has no magnetometer. If set to 0, the preflight checks will not check for the presence of a magnetometer, otherwise N sensors are required. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


2012. SYS_HAS_NUM_DIST (INT32)
- 名称：SYS_HAS_NUM_DIST (INT32)
- 参数描述：Number of distance sensors to check being available Comment: The preflight check will fail if fewer than this number of distance sensors with valid data is present. Disable the check with 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`0`
- 单位：``


2013. SYS_HITL (INT32)
- 名称：SYS_HITL (INT32)
- 参数描述：Enable HITL/SIH mode on next boot Comment: While enabled the system will boot in Hardware-In-The-Loop (HITL) or Simulation-In-Hardware (SIH) mode and not enable all sensors and checks. When disabled the same vehicle can be flown normally. Set to 'external HITL', if the system should perform as if it were a real vehicle (the only difference to a real system is then only the parameter value, which can be used for log analysis). 参数对照:-1: external HITL 0: HITL and SIH disabled 1: HITL enabled 2: SIH enabled Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2014. SYS_MC_EST_GROUP (INT32)
- 名称：SYS_MC_EST_GROUP (INT32)
- 参数描述：Set multicopter estimator group Comment: Set the group of estimators used for multicopters and VTOLs 参数对照:1: local_position_estimator, attitude_estimator_q (unsupported) 2: ekf2 (recommended) 3: Q attitude estimator (no position) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


2015. SYS_RGB_MAXBRT (FLOAT)
- 名称：SYS_RGB_MAXBRT (FLOAT)
- 参数描述：RGB Led brightness limit Comment: Set to 0 to disable, 1 for maximum brightness
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.`
- 单位：`%`


2016. SYS_STCK_EN (INT32)
- 名称：SYS_STCK_EN (INT32)
- 参数描述：Enable stack checking
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2017. SYS_USE_IO (INT32)
- 名称：SYS_USE_IO (INT32)
- 参数描述：Set usage of IO board Comment: Can be used to use a configure the use of the IO board. 参数对照:0: IO PWM disabled (RC only) 1: IO enabled (RC & PWM) Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2018. TEL_BST_EN (INT32)
- 名称：TEL_BST_EN (INT32)
- 参数描述：Blacksheep telemetry Enable Comment: If true, the FMU will try to connect to Blacksheep telemetry on start up Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2019. TEL_FRSKY_CONFIG (INT32)
- 名称：TEL_FRSKY_CONFIG (INT32)
- 参数描述：Serial Configuration for FrSky Telemetry Comment: Configure on which serial port to run FrSky Telemetry. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2020. TEL_HOTT_CONFIG (INT32)
- 名称：TEL_HOTT_CONFIG (INT32)
- 参数描述：Serial Configuration for HoTT Telemetry Comment: Configure on which serial port to run HoTT Telemetry. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2021. TEST_1 (INT32)
- 名称：TEST_1 (INT32)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


2022. TEST_2 (INT32)
- 名称：TEST_2 (INT32)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4`
- 单位：``


2023. TEST_3 (FLOAT)
- 名称：TEST_3 (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5.0`
- 单位：``


2024. TEST_D (FLOAT)
- 名称：TEST_D (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.01`
- 单位：``


2025. TEST_DEV (FLOAT)
- 名称：TEST_DEV (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2.0`
- 单位：``


2026. TEST_D_LP (FLOAT)
- 名称：TEST_D_LP (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`10.0`
- 单位：``


2027. TEST_HP (FLOAT)
- 名称：TEST_HP (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`10.0`
- 单位：``


2028. TEST_I (FLOAT)
- 名称：TEST_I (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.1`
- 单位：``


2029. TEST_I_MAX (FLOAT)
- 名称：TEST_I_MAX (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2030. TEST_LP (FLOAT)
- 名称：TEST_LP (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`10.0`
- 单位：``


2031. TEST_MAX (FLOAT)
- 名称：TEST_MAX (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2032. TEST_MEAN (FLOAT)
- 名称：TEST_MEAN (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2033. TEST_MIN (FLOAT)
- 名称：TEST_MIN (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1.0`
- 单位：``


2034. TEST_P (FLOAT)
- 名称：TEST_P (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.2`
- 单位：``


2035. TEST_PARAMS (INT32)
- 名称：TEST_PARAMS (INT32)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`12345678`
- 单位：``


2036. TEST_RC2_X (INT32)
- 名称：TEST_RC2_X (INT32)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`16`
- 单位：``


2037. TEST_RC_X (INT32)
- 名称：TEST_RC_X (INT32)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`8`
- 单位：``


2038. TEST_TRIM (FLOAT)
- 名称：TEST_TRIM (FLOAT)
- 参数描述：
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.5`
- 单位：``


2039. TC_A0_ID (INT32)
- 名称：TC_A0_ID (INT32)
- 参数描述：ID of Accelerometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2040. TC_A0_TMAX (FLOAT)
- 名称：TC_A0_TMAX (FLOAT)
- 参数描述：Accelerometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2041. TC_A0_TMIN (FLOAT)
- 名称：TC_A0_TMIN (FLOAT)
- 参数描述：Accelerometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2042. TC_A0_TREF (FLOAT)
- 名称：TC_A0_TREF (FLOAT)
- 参数描述：Accelerometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2043. TC_A0_X0_0 (FLOAT)
- 名称：TC_A0_X0_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2044. TC_A0_X0_1 (FLOAT)
- 名称：TC_A0_X0_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2045. TC_A0_X0_2 (FLOAT)
- 名称：TC_A0_X0_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2046. TC_A0_X1_0 (FLOAT)
- 名称：TC_A0_X1_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2047. TC_A0_X1_1 (FLOAT)
- 名称：TC_A0_X1_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2048. TC_A0_X1_2 (FLOAT)
- 名称：TC_A0_X1_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2049. TC_A0_X2_0 (FLOAT)
- 名称：TC_A0_X2_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2050. TC_A0_X2_1 (FLOAT)
- 名称：TC_A0_X2_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2051. TC_A0_X2_2 (FLOAT)
- 名称：TC_A0_X2_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2052. TC_A0_X3_0 (FLOAT)
- 名称：TC_A0_X3_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2053. TC_A0_X3_1 (FLOAT)
- 名称：TC_A0_X3_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2054. TC_A0_X3_2 (FLOAT)
- 名称：TC_A0_X3_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2055. TC_A1_ID (INT32)
- 名称：TC_A1_ID (INT32)
- 参数描述：ID of Accelerometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2056. TC_A1_TMAX (FLOAT)
- 名称：TC_A1_TMAX (FLOAT)
- 参数描述：Accelerometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2057. TC_A1_TMIN (FLOAT)
- 名称：TC_A1_TMIN (FLOAT)
- 参数描述：Accelerometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2058. TC_A1_TREF (FLOAT)
- 名称：TC_A1_TREF (FLOAT)
- 参数描述：Accelerometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2059. TC_A1_X0_0 (FLOAT)
- 名称：TC_A1_X0_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2060. TC_A1_X0_1 (FLOAT)
- 名称：TC_A1_X0_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2061. TC_A1_X0_2 (FLOAT)
- 名称：TC_A1_X0_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2062. TC_A1_X1_0 (FLOAT)
- 名称：TC_A1_X1_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2063. TC_A1_X1_1 (FLOAT)
- 名称：TC_A1_X1_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2064. TC_A1_X1_2 (FLOAT)
- 名称：TC_A1_X1_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2065. TC_A1_X2_0 (FLOAT)
- 名称：TC_A1_X2_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2066. TC_A1_X2_1 (FLOAT)
- 名称：TC_A1_X2_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2067. TC_A1_X2_2 (FLOAT)
- 名称：TC_A1_X2_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2068. TC_A1_X3_0 (FLOAT)
- 名称：TC_A1_X3_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2069. TC_A1_X3_1 (FLOAT)
- 名称：TC_A1_X3_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2070. TC_A1_X3_2 (FLOAT)
- 名称：TC_A1_X3_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2071. TC_A2_ID (INT32)
- 名称：TC_A2_ID (INT32)
- 参数描述：ID of Accelerometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2072. TC_A2_TMAX (FLOAT)
- 名称：TC_A2_TMAX (FLOAT)
- 参数描述：Accelerometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2073. TC_A2_TMIN (FLOAT)
- 名称：TC_A2_TMIN (FLOAT)
- 参数描述：Accelerometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2074. TC_A2_TREF (FLOAT)
- 名称：TC_A2_TREF (FLOAT)
- 参数描述：Accelerometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2075. TC_A2_X0_0 (FLOAT)
- 名称：TC_A2_X0_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2076. TC_A2_X0_1 (FLOAT)
- 名称：TC_A2_X0_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2077. TC_A2_X0_2 (FLOAT)
- 名称：TC_A2_X0_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2078. TC_A2_X1_0 (FLOAT)
- 名称：TC_A2_X1_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2079. TC_A2_X1_1 (FLOAT)
- 名称：TC_A2_X1_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2080. TC_A2_X1_2 (FLOAT)
- 名称：TC_A2_X1_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2081. TC_A2_X2_0 (FLOAT)
- 名称：TC_A2_X2_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2082. TC_A2_X2_1 (FLOAT)
- 名称：TC_A2_X2_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2083. TC_A2_X2_2 (FLOAT)
- 名称：TC_A2_X2_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2084. TC_A2_X3_0 (FLOAT)
- 名称：TC_A2_X3_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2085. TC_A2_X3_1 (FLOAT)
- 名称：TC_A2_X3_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2086. TC_A2_X3_2 (FLOAT)
- 名称：TC_A2_X3_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2087. TC_A3_ID (INT32)
- 名称：TC_A3_ID (INT32)
- 参数描述：ID of Accelerometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2088. TC_A3_TMAX (FLOAT)
- 名称：TC_A3_TMAX (FLOAT)
- 参数描述：Accelerometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2089. TC_A3_TMIN (FLOAT)
- 名称：TC_A3_TMIN (FLOAT)
- 参数描述：Accelerometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2090. TC_A3_TREF (FLOAT)
- 名称：TC_A3_TREF (FLOAT)
- 参数描述：Accelerometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2091. TC_A3_X0_0 (FLOAT)
- 名称：TC_A3_X0_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2092. TC_A3_X0_1 (FLOAT)
- 名称：TC_A3_X0_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2093. TC_A3_X0_2 (FLOAT)
- 名称：TC_A3_X0_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2094. TC_A3_X1_0 (FLOAT)
- 名称：TC_A3_X1_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2095. TC_A3_X1_1 (FLOAT)
- 名称：TC_A3_X1_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2096. TC_A3_X1_2 (FLOAT)
- 名称：TC_A3_X1_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2097. TC_A3_X2_0 (FLOAT)
- 名称：TC_A3_X2_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2098. TC_A3_X2_1 (FLOAT)
- 名称：TC_A3_X2_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2099. TC_A3_X2_2 (FLOAT)
- 名称：TC_A3_X2_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2100. TC_A3_X3_0 (FLOAT)
- 名称：TC_A3_X3_0 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2101. TC_A3_X3_1 (FLOAT)
- 名称：TC_A3_X3_1 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2102. TC_A3_X3_2 (FLOAT)
- 名称：TC_A3_X3_2 (FLOAT)
- 参数描述：Accelerometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2103. TC_A_ENABLE (INT32)
- 名称：TC_A_ENABLE (INT32)
- 参数描述：Thermal compensation for accelerometer sensors    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2104. TC_B0_ID (INT32)
- 名称：TC_B0_ID (INT32)
- 参数描述：ID of Barometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2105. TC_B0_TMAX (FLOAT)
- 名称：TC_B0_TMAX (FLOAT)
- 参数描述：Barometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`75.0`
- 单位：``


2106. TC_B0_TMIN (FLOAT)
- 名称：TC_B0_TMIN (FLOAT)
- 参数描述：Barometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5.0`
- 单位：``


2107. TC_B0_TREF (FLOAT)
- 名称：TC_B0_TREF (FLOAT)
- 参数描述：Barometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`40.0`
- 单位：``


2108. TC_B0_X0 (FLOAT)
- 名称：TC_B0_X0 (FLOAT)
- 参数描述：Barometer offset temperature ^0 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2109. TC_B0_X1 (FLOAT)
- 名称：TC_B0_X1 (FLOAT)
- 参数描述：Barometer offset temperature ^1 polynomial coefficients
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2110. TC_B0_X2 (FLOAT)
- 名称：TC_B0_X2 (FLOAT)
- 参数描述：Barometer offset temperature ^2 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2111. TC_B0_X3 (FLOAT)
- 名称：TC_B0_X3 (FLOAT)
- 参数描述：Barometer offset temperature ^3 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2112. TC_B0_X4 (FLOAT)
- 名称：TC_B0_X4 (FLOAT)
- 参数描述：Barometer offset temperature ^4 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2113. TC_B0_X5 (FLOAT)
- 名称：TC_B0_X5 (FLOAT)
- 参数描述：Barometer offset temperature ^5 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2114. TC_B1_ID (INT32)
- 名称：TC_B1_ID (INT32)
- 参数描述：ID of Barometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2115. TC_B1_TMAX (FLOAT)
- 名称：TC_B1_TMAX (FLOAT)
- 参数描述：Barometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`75.0`
- 单位：``


2116. TC_B1_TMIN (FLOAT)
- 名称：TC_B1_TMIN (FLOAT)
- 参数描述：Barometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5.0`
- 单位：``


2117. TC_B1_TREF (FLOAT)
- 名称：TC_B1_TREF (FLOAT)
- 参数描述：Barometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`40.0`
- 单位：``


2118. TC_B1_X0 (FLOAT)
- 名称：TC_B1_X0 (FLOAT)
- 参数描述：Barometer offset temperature ^0 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2119. TC_B1_X1 (FLOAT)
- 名称：TC_B1_X1 (FLOAT)
- 参数描述：Barometer offset temperature ^1 polynomial coefficients
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2120. TC_B1_X2 (FLOAT)
- 名称：TC_B1_X2 (FLOAT)
- 参数描述：Barometer offset temperature ^2 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2121. TC_B1_X3 (FLOAT)
- 名称：TC_B1_X3 (FLOAT)
- 参数描述：Barometer offset temperature ^3 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2122. TC_B1_X4 (FLOAT)
- 名称：TC_B1_X4 (FLOAT)
- 参数描述：Barometer offset temperature ^4 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2123. TC_B1_X5 (FLOAT)
- 名称：TC_B1_X5 (FLOAT)
- 参数描述：Barometer offset temperature ^5 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2124. TC_B2_ID (INT32)
- 名称：TC_B2_ID (INT32)
- 参数描述：ID of Barometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2125. TC_B2_TMAX (FLOAT)
- 名称：TC_B2_TMAX (FLOAT)
- 参数描述：Barometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`75.0`
- 单位：``


2126. TC_B2_TMIN (FLOAT)
- 名称：TC_B2_TMIN (FLOAT)
- 参数描述：Barometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5.0`
- 单位：``


2127. TC_B2_TREF (FLOAT)
- 名称：TC_B2_TREF (FLOAT)
- 参数描述：Barometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`40.0`
- 单位：``


2128. TC_B2_X0 (FLOAT)
- 名称：TC_B2_X0 (FLOAT)
- 参数描述：Barometer offset temperature ^0 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2129. TC_B2_X1 (FLOAT)
- 名称：TC_B2_X1 (FLOAT)
- 参数描述：Barometer offset temperature ^1 polynomial coefficients
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2130. TC_B2_X2 (FLOAT)
- 名称：TC_B2_X2 (FLOAT)
- 参数描述：Barometer offset temperature ^2 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2131. TC_B2_X3 (FLOAT)
- 名称：TC_B2_X3 (FLOAT)
- 参数描述：Barometer offset temperature ^3 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2132. TC_B2_X4 (FLOAT)
- 名称：TC_B2_X4 (FLOAT)
- 参数描述：Barometer offset temperature ^4 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2133. TC_B2_X5 (FLOAT)
- 名称：TC_B2_X5 (FLOAT)
- 参数描述：Barometer offset temperature ^5 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2134. TC_B3_ID (INT32)
- 名称：TC_B3_ID (INT32)
- 参数描述：ID of Barometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2135. TC_B3_TMAX (FLOAT)
- 名称：TC_B3_TMAX (FLOAT)
- 参数描述：Barometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`75.0`
- 单位：``


2136. TC_B3_TMIN (FLOAT)
- 名称：TC_B3_TMIN (FLOAT)
- 参数描述：Barometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5.0`
- 单位：``


2137. TC_B3_TREF (FLOAT)
- 名称：TC_B3_TREF (FLOAT)
- 参数描述：Barometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`40.0`
- 单位：``


2138. TC_B3_X0 (FLOAT)
- 名称：TC_B3_X0 (FLOAT)
- 参数描述：Barometer offset temperature ^0 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2139. TC_B3_X1 (FLOAT)
- 名称：TC_B3_X1 (FLOAT)
- 参数描述：Barometer offset temperature ^1 polynomial coefficients
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2140. TC_B3_X2 (FLOAT)
- 名称：TC_B3_X2 (FLOAT)
- 参数描述：Barometer offset temperature ^2 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2141. TC_B3_X3 (FLOAT)
- 名称：TC_B3_X3 (FLOAT)
- 参数描述：Barometer offset temperature ^3 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2142. TC_B3_X4 (FLOAT)
- 名称：TC_B3_X4 (FLOAT)
- 参数描述：Barometer offset temperature ^4 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2143. TC_B3_X5 (FLOAT)
- 名称：TC_B3_X5 (FLOAT)
- 参数描述：Barometer offset temperature ^5 polynomial coefficient
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2144. TC_B_ENABLE (INT32)
- 名称：TC_B_ENABLE (INT32)
- 参数描述：Thermal compensation for barometric pressure sensors    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2145. TC_G0_ID (INT32)
- 名称：TC_G0_ID (INT32)
- 参数描述：ID of Gyro that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2146. TC_G0_TMAX (FLOAT)
- 名称：TC_G0_TMAX (FLOAT)
- 参数描述：Gyro calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2147. TC_G0_TMIN (FLOAT)
- 名称：TC_G0_TMIN (FLOAT)
- 参数描述：Gyro calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2148. TC_G0_TREF (FLOAT)
- 名称：TC_G0_TREF (FLOAT)
- 参数描述：Gyro calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2149. TC_G0_X0_0 (FLOAT)
- 名称：TC_G0_X0_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2150. TC_G0_X0_1 (FLOAT)
- 名称：TC_G0_X0_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2151. TC_G0_X0_2 (FLOAT)
- 名称：TC_G0_X0_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2152. TC_G0_X1_0 (FLOAT)
- 名称：TC_G0_X1_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2153. TC_G0_X1_1 (FLOAT)
- 名称：TC_G0_X1_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2154. TC_G0_X1_2 (FLOAT)
- 名称：TC_G0_X1_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2155. TC_G0_X2_0 (FLOAT)
- 名称：TC_G0_X2_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2156. TC_G0_X2_1 (FLOAT)
- 名称：TC_G0_X2_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2157. TC_G0_X2_2 (FLOAT)
- 名称：TC_G0_X2_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2158. TC_G0_X3_0 (FLOAT)
- 名称：TC_G0_X3_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2159. TC_G0_X3_1 (FLOAT)
- 名称：TC_G0_X3_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2160. TC_G0_X3_2 (FLOAT)
- 名称：TC_G0_X3_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2161. TC_G1_ID (INT32)
- 名称：TC_G1_ID (INT32)
- 参数描述：ID of Gyro that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2162. TC_G1_TMAX (FLOAT)
- 名称：TC_G1_TMAX (FLOAT)
- 参数描述：Gyro calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2163. TC_G1_TMIN (FLOAT)
- 名称：TC_G1_TMIN (FLOAT)
- 参数描述：Gyro calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2164. TC_G1_TREF (FLOAT)
- 名称：TC_G1_TREF (FLOAT)
- 参数描述：Gyro calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2165. TC_G1_X0_0 (FLOAT)
- 名称：TC_G1_X0_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2166. TC_G1_X0_1 (FLOAT)
- 名称：TC_G1_X0_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2167. TC_G1_X0_2 (FLOAT)
- 名称：TC_G1_X0_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2168. TC_G1_X1_0 (FLOAT)
- 名称：TC_G1_X1_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2169. TC_G1_X1_1 (FLOAT)
- 名称：TC_G1_X1_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2170. TC_G1_X1_2 (FLOAT)
- 名称：TC_G1_X1_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2171. TC_G1_X2_0 (FLOAT)
- 名称：TC_G1_X2_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2172. TC_G1_X2_1 (FLOAT)
- 名称：TC_G1_X2_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2173. TC_G1_X2_2 (FLOAT)
- 名称：TC_G1_X2_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2174. TC_G1_X3_0 (FLOAT)
- 名称：TC_G1_X3_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2175. TC_G1_X3_1 (FLOAT)
- 名称：TC_G1_X3_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2176. TC_G1_X3_2 (FLOAT)
- 名称：TC_G1_X3_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2177. TC_G2_ID (INT32)
- 名称：TC_G2_ID (INT32)
- 参数描述：ID of Gyro that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2178. TC_G2_TMAX (FLOAT)
- 名称：TC_G2_TMAX (FLOAT)
- 参数描述：Gyro calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2179. TC_G2_TMIN (FLOAT)
- 名称：TC_G2_TMIN (FLOAT)
- 参数描述：Gyro calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2180. TC_G2_TREF (FLOAT)
- 名称：TC_G2_TREF (FLOAT)
- 参数描述：Gyro calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2181. TC_G2_X0_0 (FLOAT)
- 名称：TC_G2_X0_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2182. TC_G2_X0_1 (FLOAT)
- 名称：TC_G2_X0_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2183. TC_G2_X0_2 (FLOAT)
- 名称：TC_G2_X0_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2184. TC_G2_X1_0 (FLOAT)
- 名称：TC_G2_X1_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2185. TC_G2_X1_1 (FLOAT)
- 名称：TC_G2_X1_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2186. TC_G2_X1_2 (FLOAT)
- 名称：TC_G2_X1_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2187. TC_G2_X2_0 (FLOAT)
- 名称：TC_G2_X2_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2188. TC_G2_X2_1 (FLOAT)
- 名称：TC_G2_X2_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2189. TC_G2_X2_2 (FLOAT)
- 名称：TC_G2_X2_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2190. TC_G2_X3_0 (FLOAT)
- 名称：TC_G2_X3_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2191. TC_G2_X3_1 (FLOAT)
- 名称：TC_G2_X3_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2192. TC_G2_X3_2 (FLOAT)
- 名称：TC_G2_X3_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2193. TC_G3_ID (INT32)
- 名称：TC_G3_ID (INT32)
- 参数描述：ID of Gyro that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2194. TC_G3_TMAX (FLOAT)
- 名称：TC_G3_TMAX (FLOAT)
- 参数描述：Gyro calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2195. TC_G3_TMIN (FLOAT)
- 名称：TC_G3_TMIN (FLOAT)
- 参数描述：Gyro calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2196. TC_G3_TREF (FLOAT)
- 名称：TC_G3_TREF (FLOAT)
- 参数描述：Gyro calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2197. TC_G3_X0_0 (FLOAT)
- 名称：TC_G3_X0_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2198. TC_G3_X0_1 (FLOAT)
- 名称：TC_G3_X0_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2199. TC_G3_X0_2 (FLOAT)
- 名称：TC_G3_X0_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2200. TC_G3_X1_0 (FLOAT)
- 名称：TC_G3_X1_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2201. TC_G3_X1_1 (FLOAT)
- 名称：TC_G3_X1_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2202. TC_G3_X1_2 (FLOAT)
- 名称：TC_G3_X1_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2203. TC_G3_X2_0 (FLOAT)
- 名称：TC_G3_X2_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2204. TC_G3_X2_1 (FLOAT)
- 名称：TC_G3_X2_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2205. TC_G3_X2_2 (FLOAT)
- 名称：TC_G3_X2_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2206. TC_G3_X3_0 (FLOAT)
- 名称：TC_G3_X3_0 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2207. TC_G3_X3_1 (FLOAT)
- 名称：TC_G3_X3_1 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2208. TC_G3_X3_2 (FLOAT)
- 名称：TC_G3_X3_2 (FLOAT)
- 参数描述：Gyro rate offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2209. TC_G_ENABLE (INT32)
- 名称：TC_G_ENABLE (INT32)
- 参数描述：Thermal compensation for rate gyro sensors    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2210. TC_M0_ID (INT32)
- 名称：TC_M0_ID (INT32)
- 参数描述：ID of Magnetometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2211. TC_M0_TMAX (FLOAT)
- 名称：TC_M0_TMAX (FLOAT)
- 参数描述：Magnetometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2212. TC_M0_TMIN (FLOAT)
- 名称：TC_M0_TMIN (FLOAT)
- 参数描述：Magnetometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2213. TC_M0_TREF (FLOAT)
- 名称：TC_M0_TREF (FLOAT)
- 参数描述：Magnetometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2214. TC_M0_X0_0 (FLOAT)
- 名称：TC_M0_X0_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2215. TC_M0_X0_1 (FLOAT)
- 名称：TC_M0_X0_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2216. TC_M0_X0_2 (FLOAT)
- 名称：TC_M0_X0_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2217. TC_M0_X1_0 (FLOAT)
- 名称：TC_M0_X1_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2218. TC_M0_X1_1 (FLOAT)
- 名称：TC_M0_X1_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2219. TC_M0_X1_2 (FLOAT)
- 名称：TC_M0_X1_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2220. TC_M0_X2_0 (FLOAT)
- 名称：TC_M0_X2_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2221. TC_M0_X2_1 (FLOAT)
- 名称：TC_M0_X2_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2222. TC_M0_X2_2 (FLOAT)
- 名称：TC_M0_X2_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2223. TC_M0_X3_0 (FLOAT)
- 名称：TC_M0_X3_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2224. TC_M0_X3_1 (FLOAT)
- 名称：TC_M0_X3_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2225. TC_M0_X3_2 (FLOAT)
- 名称：TC_M0_X3_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2226. TC_M1_ID (INT32)
- 名称：TC_M1_ID (INT32)
- 参数描述：ID of Magnetometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2227. TC_M1_TMAX (FLOAT)
- 名称：TC_M1_TMAX (FLOAT)
- 参数描述：Magnetometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2228. TC_M1_TMIN (FLOAT)
- 名称：TC_M1_TMIN (FLOAT)
- 参数描述：Magnetometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2229. TC_M1_TREF (FLOAT)
- 名称：TC_M1_TREF (FLOAT)
- 参数描述：Magnetometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2230. TC_M1_X0_0 (FLOAT)
- 名称：TC_M1_X0_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2231. TC_M1_X0_1 (FLOAT)
- 名称：TC_M1_X0_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2232. TC_M1_X0_2 (FLOAT)
- 名称：TC_M1_X0_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2233. TC_M1_X1_0 (FLOAT)
- 名称：TC_M1_X1_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2234. TC_M1_X1_1 (FLOAT)
- 名称：TC_M1_X1_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2235. TC_M1_X1_2 (FLOAT)
- 名称：TC_M1_X1_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2236. TC_M1_X2_0 (FLOAT)
- 名称：TC_M1_X2_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2237. TC_M1_X2_1 (FLOAT)
- 名称：TC_M1_X2_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2238. TC_M1_X2_2 (FLOAT)
- 名称：TC_M1_X2_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2239. TC_M1_X3_0 (FLOAT)
- 名称：TC_M1_X3_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2240. TC_M1_X3_1 (FLOAT)
- 名称：TC_M1_X3_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2241. TC_M1_X3_2 (FLOAT)
- 名称：TC_M1_X3_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2242. TC_M2_ID (INT32)
- 名称：TC_M2_ID (INT32)
- 参数描述：ID of Magnetometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2243. TC_M2_TMAX (FLOAT)
- 名称：TC_M2_TMAX (FLOAT)
- 参数描述：Magnetometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2244. TC_M2_TMIN (FLOAT)
- 名称：TC_M2_TMIN (FLOAT)
- 参数描述：Magnetometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2245. TC_M2_TREF (FLOAT)
- 名称：TC_M2_TREF (FLOAT)
- 参数描述：Magnetometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2246. TC_M2_X0_0 (FLOAT)
- 名称：TC_M2_X0_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2247. TC_M2_X0_1 (FLOAT)
- 名称：TC_M2_X0_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2248. TC_M2_X0_2 (FLOAT)
- 名称：TC_M2_X0_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2249. TC_M2_X1_0 (FLOAT)
- 名称：TC_M2_X1_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2250. TC_M2_X1_1 (FLOAT)
- 名称：TC_M2_X1_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2251. TC_M2_X1_2 (FLOAT)
- 名称：TC_M2_X1_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2252. TC_M2_X2_0 (FLOAT)
- 名称：TC_M2_X2_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2253. TC_M2_X2_1 (FLOAT)
- 名称：TC_M2_X2_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2254. TC_M2_X2_2 (FLOAT)
- 名称：TC_M2_X2_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2255. TC_M2_X3_0 (FLOAT)
- 名称：TC_M2_X3_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2256. TC_M2_X3_1 (FLOAT)
- 名称：TC_M2_X3_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2257. TC_M2_X3_2 (FLOAT)
- 名称：TC_M2_X3_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2258. TC_M3_ID (INT32)
- 名称：TC_M3_ID (INT32)
- 参数描述：ID of Magnetometer that the calibration is for
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2259. TC_M3_TMAX (FLOAT)
- 名称：TC_M3_TMAX (FLOAT)
- 参数描述：Magnetometer calibration maximum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`100.0`
- 单位：``


2260. TC_M3_TMIN (FLOAT)
- 名称：TC_M3_TMIN (FLOAT)
- 参数描述：Magnetometer calibration minimum temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2261. TC_M3_TREF (FLOAT)
- 名称：TC_M3_TREF (FLOAT)
- 参数描述：Magnetometer calibration reference temperature
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`25.0`
- 单位：``


2262. TC_M3_X0_0 (FLOAT)
- 名称：TC_M3_X0_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2263. TC_M3_X0_1 (FLOAT)
- 名称：TC_M3_X0_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2264. TC_M3_X0_2 (FLOAT)
- 名称：TC_M3_X0_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^0 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2265. TC_M3_X1_0 (FLOAT)
- 名称：TC_M3_X1_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2266. TC_M3_X1_1 (FLOAT)
- 名称：TC_M3_X1_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2267. TC_M3_X1_2 (FLOAT)
- 名称：TC_M3_X1_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^1 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2268. TC_M3_X2_0 (FLOAT)
- 名称：TC_M3_X2_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2269. TC_M3_X2_1 (FLOAT)
- 名称：TC_M3_X2_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2270. TC_M3_X2_2 (FLOAT)
- 名称：TC_M3_X2_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^2 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2271. TC_M3_X3_0 (FLOAT)
- 名称：TC_M3_X3_0 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - X axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2272. TC_M3_X3_1 (FLOAT)
- 名称：TC_M3_X3_1 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Y axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2273. TC_M3_X3_2 (FLOAT)
- 名称：TC_M3_X3_2 (FLOAT)
- 参数描述：Magnetometer offset temperature ^3 polynomial coefficient - Z axis
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2274. TC_M_ENABLE (INT32)
- 名称：TC_M_ENABLE (INT32)
- 参数描述：Thermal compensation for magnetometer sensors    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2275. MXS_EXT_CFG (INT32)
- 名称：MXS_EXT_CFG (INT32)
- 参数描述：Sagetech External Configuration Mode Comment: Disables auto-configuration mode enabling MXS config through external software. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2276. MXS_OP_MODE (INT32)
- 名称：MXS_OP_MODE (INT32)
- 参数描述：Sagetech MXS mode configuration Comment: This parameter defines the operating mode of the MXS 参数对照:0: Off 1: On 2: Standby 3: Alt Reboot required: false
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0`
- 单位：``


2277. MXS_SER_CFG (INT32)
- 名称：MXS_SER_CFG (INT32)
- 参数描述：Serial Configuration for Sagetech MXS Serial Port Comment: Configure on which serial port to run Sagetech MXS Serial Port. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2278. MXS_TARG_PORT (INT32)
- 名称：MXS_TARG_PORT (INT32)
- 参数描述：Sagetech MXS Participant Configuration Comment: The MXS communication port to receive Target data from 参数对照:0: Auto 1: COM0 2: COM1 Reboot required: false
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`1`
- 单位：``


2279. CANNODE_BITRATE (INT32)
- 名称：CANNODE_BITRATE (INT32)
- 参数描述：UAVCAN CAN bus bitrate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20000, 1000000]`
- 默认值：`1000000`
- 单位：``


2280. CANNODE_PUB_MBD (INT32)
- 名称：CANNODE_PUB_MBD (INT32)
- 参数描述：Enable MovingBaselineData publication    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2281. CANNODE_SUB_MBD (INT32)
- 名称：CANNODE_SUB_MBD (INT32)
- 参数描述：Enable MovingBaselineData subscription    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[?, 1]`
- 默认值：`Disabled (0)`
- 单位：``


2282. CANNODE_SUB_RTCM (INT32)
- 名称：CANNODE_SUB_RTCM (INT32)
- 参数描述：Enable RTCM subscription    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2283. CANNODE_TERM (INT32)
- 名称：CANNODE_TERM (INT32)
- 参数描述：CAN built-in bus termination
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[?, 1]`
- 默认值：`Disabled (0)`
- 单位：``


2284. SIM_GZ_EN (INT32)
- 名称：SIM_GZ_EN (INT32)
- 参数描述：Simulator Gazebo bridge enable    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2285. UAVCAN_BITRATE (INT32)
- 名称：UAVCAN_BITRATE (INT32)
- 参数描述：UAVCAN CAN bus bitrate    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20000, 1000000]`
- 默认值：`1000000`
- 单位：`bit/s`


2286. UAVCAN_ENABLE (INT32)
- 名称：UAVCAN_ENABLE (INT32)
- 参数描述：UAVCAN mode Comment: 0 - UAVCAN disabled. 1 - Enables support for UAVCAN sensors without dynamic node ID allocation and firmware update. 2 - Enables support for UAVCAN sensors with dynamic node ID allocation and firmware update. 3 - Enables support for UAVCAN sensors and actuators with dynamic node ID allocation and firmware update. Also sets the motor control outputs to UAVCAN. 参数对照:0: Disabled 1: Sensors Manual Config 2: Sensors Automatic Config 3: Sensors and Actuators (ESCs) Automatic Config Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0`
- 单位：``


2287. UAVCAN_LGT_ANTCL (INT32)
- 名称：UAVCAN_LGT_ANTCL (INT32)
- 参数描述：UAVCAN ANTI_COLLISION light operating mode Comment: This parameter defines the minimum condition under which the system will command the ANTI_COLLISION lights on 0 - Always off 1 - When autopilot is armed 2 - When autopilot is prearmed 3 - Always on 参数对照:0: Always off 1: When autopilot is armed 2: When autopilot is prearmed 3: Always on Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`2`
- 单位：``


2288. UAVCAN_LGT_LAND (INT32)
- 名称：UAVCAN_LGT_LAND (INT32)
- 参数描述：UAVCAN LIGHT_ID_LANDING light operating mode Comment: This parameter defines the minimum condition under which the system will command the LIGHT_ID_LANDING lights on 0 - Always off 1 - When autopilot is armed 2 - When autopilot is prearmed 3 - Always on 参数对照:0: Always off 1: When autopilot is armed 2: When autopilot is prearmed 3: Always on Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0`
- 单位：``


2289. UAVCAN_LGT_NAV (INT32)
- 名称：UAVCAN_LGT_NAV (INT32)
- 参数描述：UAVCAN RIGHT_OF_WAY light operating mode Comment: This parameter defines the minimum condition under which the system will command the RIGHT_OF_WAY lights on 0 - Always off 1 - When autopilot is armed 2 - When autopilot is prearmed 3 - Always on 参数对照:0: Always off 1: When autopilot is armed 2: When autopilot is prearmed 3: Always on Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`3`
- 单位：``


2290. UAVCAN_LGT_STROB (INT32)
- 名称：UAVCAN_LGT_STROB (INT32)
- 参数描述：UAVCAN STROBE light operating mode Comment: This parameter defines the minimum condition under which the system will command the STROBE lights on 0 - Always off 1 - When autopilot is armed 2 - When autopilot is prearmed 3 - Always on 参数对照:0: Always off 1: When autopilot is armed 2: When autopilot is prearmed 3: Always on Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`1`
- 单位：``


2291. UAVCAN_NODE_ID (INT32)
- 名称：UAVCAN_NODE_ID (INT32)
- 参数描述：UAVCAN Node ID Comment: Read the specs at http://uavcan.org to learn more about Node ID. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 125]`
- 默认值：`1`
- 单位：``


2292. UAVCAN_PUB_ARM (INT32)
- 名称：UAVCAN_PUB_ARM (INT32)
- 参数描述：publish Arming Status stream Comment: Enable UAVCAN Arming Status stream publication uavcan::equipment::safety::ArmingStatus Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2293. UAVCAN_PUB_MBD (INT32)
- 名称：UAVCAN_PUB_MBD (INT32)
- 参数描述：publish moving baseline data RTCM stream Comment: Enable UAVCAN RTCM stream publication ardupilot::gnss::MovingBaselineData Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2294. UAVCAN_PUB_RTCM (INT32)
- 名称：UAVCAN_PUB_RTCM (INT32)
- 参数描述：publish RTCM stream Comment: Enable UAVCAN RTCM stream publication uavcan::equipment::gnss::RTCMStream Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2295. UAVCAN_RNG_MAX (FLOAT)
- 名称：UAVCAN_RNG_MAX (FLOAT)
- 参数描述：UAVCAN rangefinder maximum range Comment: This parameter defines the maximum valid range for a rangefinder connected via UAVCAN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`200.0`
- 单位：`m`


2296. UAVCAN_RNG_MIN (FLOAT)
- 名称：UAVCAN_RNG_MIN (FLOAT)
- 参数描述：UAVCAN rangefinder minimum range Comment: This parameter defines the minimum valid range for a rangefinder connected via UAVCAN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.3`
- 单位：`m`


2297. UAVCAN_SUB_ASPD (INT32)
- 名称：UAVCAN_SUB_ASPD (INT32)
- 参数描述：subscription airspeed Comment: Enable UAVCAN airspeed subscriptions. uavcan::equipment::air_data::IndicatedAirspeed uavcan::equipment::air_data::TrueAirspeed uavcan::equipment::air_data::StaticTemperature Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2298. UAVCAN_SUB_BARO (INT32)
- 名称：UAVCAN_SUB_BARO (INT32)
- 参数描述：subscription barometer Comment: Enable UAVCAN barometer subscription. uavcan::equipment::air_data::StaticPressure uavcan::equipment::air_data::StaticTemperature Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2299. UAVCAN_SUB_BAT (INT32)
- 名称：UAVCAN_SUB_BAT (INT32)
- 参数描述：subscription battery Comment: Enable UAVCAN battery subscription. uavcan::equipment::power::BatteryInfo ardupilot::equipment::power::BatteryInfoAux 0 - Disable 1 - Use raw data. Recommended for Smart battery 2 - Filter the data with internal battery library 参数对照:0: Disable 1: Raw data 2: Filter data Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


2300. UAVCAN_SUB_BTN (INT32)
- 名称：UAVCAN_SUB_BTN (INT32)
- 参数描述：subscription button Comment: Enable UAVCAN button subscription. ardupilot::indication::Button Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2301. UAVCAN_SUB_DPRES (INT32)
- 名称：UAVCAN_SUB_DPRES (INT32)
- 参数描述：subscription differential pressure Comment: Enable UAVCAN differential pressure subscription. uavcan::equipment::air_data::RawAirData Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2302. UAVCAN_SUB_FLOW (INT32)
- 名称：UAVCAN_SUB_FLOW (INT32)
- 参数描述：subscription flow Comment: Enable UAVCAN optical flow subscription. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2303. UAVCAN_SUB_GPS (INT32)
- 名称：UAVCAN_SUB_GPS (INT32)
- 参数描述：subscription GPS Comment: Enable UAVCAN GPS subscriptions. uavcan::equipment::gnss::Fix uavcan::equipment::gnss::Fix2 uavcan::equipment::gnss::Auxiliary Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2304. UAVCAN_SUB_HYGRO (INT32)
- 名称：UAVCAN_SUB_HYGRO (INT32)
- 参数描述：subscription hygrometer Comment: Enable UAVCAN hygrometer subscriptions. dronecan::sensors::hygrometer::Hygrometer Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2305. UAVCAN_SUB_ICE (INT32)
- 名称：UAVCAN_SUB_ICE (INT32)
- 参数描述：subscription ICE Comment: Enable UAVCAN internal combustion engine (ICE) subscription. uavcan::equipment::ice::reciprocating::Status Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2306. UAVCAN_SUB_IMU (INT32)
- 名称：UAVCAN_SUB_IMU (INT32)
- 参数描述：subscription IMU Comment: Enable UAVCAN IMU subscription. uavcan::equipment::ahrs::RawIMU Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2307. UAVCAN_SUB_MAG (INT32)
- 名称：UAVCAN_SUB_MAG (INT32)
- 参数描述：subscription magnetometer Comment: Enable UAVCAN mag subscription. uavcan::equipment::ahrs::MagneticFieldStrength uavcan::equipment::ahrs::MagneticFieldStrength2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2308. UAVCAN_SUB_RNG (INT32)
- 名称：UAVCAN_SUB_RNG (INT32)
- 参数描述：subscription range finder Comment: Enable UAVCAN range finder subscription. uavcan::equipment::range_sensor::Measurement Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


2309. UUV_DIRCT_PITCH (FLOAT)
- 名称：UUV_DIRCT_PITCH (FLOAT)
- 参数描述：Direct pitch input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2310. UUV_DIRCT_ROLL (FLOAT)
- 名称：UUV_DIRCT_ROLL (FLOAT)
- 参数描述：Direct roll input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2311. UUV_DIRCT_THRUST (FLOAT)
- 名称：UUV_DIRCT_THRUST (FLOAT)
- 参数描述：Direct thrust input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2312. UUV_DIRCT_YAW (FLOAT)
- 名称：UUV_DIRCT_YAW (FLOAT)
- 参数描述：Direct yaw input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


2313. UUV_INPUT_MODE (INT32)
- 名称：UUV_INPUT_MODE (INT32)
- 参数描述：Select Input Mode  Values:0: use Attitude Setpoints 1: Direct Feedthrough
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2314. UUV_PITCH_D (FLOAT)
- 名称：UUV_PITCH_D (FLOAT)
- 参数描述：Pitch differential gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2.0`
- 单位：``


2315. UUV_PITCH_P (FLOAT)
- 名称：UUV_PITCH_P (FLOAT)
- 参数描述：Pitch proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4.0`
- 单位：``


2316. UUV_ROLL_D (FLOAT)
- 名称：UUV_ROLL_D (FLOAT)
- 参数描述：Roll differential gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.5`
- 单位：``


2317. UUV_ROLL_P (FLOAT)
- 名称：UUV_ROLL_P (FLOAT)
- 参数描述：Roll proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4.0`
- 单位：``


2318. UUV_YAW_D (FLOAT)
- 名称：UUV_YAW_D (FLOAT)
- 参数描述：Yaw differential gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2.0`
- 单位：``


2319. UUV_YAW_P (FLOAT)
- 名称：UUV_YAW_P (FLOAT)
- 参数描述：Yawh proportional gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4.0`
- 单位：``


2320. UUV_GAIN_X_D (FLOAT)
- 名称：UUV_GAIN_X_D (FLOAT)
- 参数描述：Gain of D controller X
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.2`
- 单位：``


2321. UUV_GAIN_X_P (FLOAT)
- 名称：UUV_GAIN_X_P (FLOAT)
- 参数描述：Gain of P controller X
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2322. UUV_GAIN_Y_D (FLOAT)
- 名称：UUV_GAIN_Y_D (FLOAT)
- 参数描述：Gain of D controller Y
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.2`
- 单位：``


2323. UUV_GAIN_Y_P (FLOAT)
- 名称：UUV_GAIN_Y_P (FLOAT)
- 参数描述：Gain of P controller Y
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2324. UUV_GAIN_Z_D (FLOAT)
- 名称：UUV_GAIN_Z_D (FLOAT)
- 参数描述：Gain of D controller Z
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.2`
- 单位：``


2325. UUV_GAIN_Z_P (FLOAT)
- 名称：UUV_GAIN_Z_P (FLOAT)
- 参数描述：Gain of P controller Z
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.0`
- 单位：``


2326. UUV_STAB_MODE (INT32)
- 名称：UUV_STAB_MODE (INT32)
- 参数描述：Stabilization mode(1) or Position Control(0)  Values:0: Position Control 1: Stabilization Mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


2327. UWB_INIT_OFF_X (FLOAT)
- 名称：UWB_INIT_OFF_X (FLOAT)
- 参数描述：UWB sensor X offset in body frame Comment: UWB sensor positioning in relation to Drone in NED. X offset. A Positive offset results in a Position o
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`0.0`
- 单位：`m`


2328. UWB_INIT_OFF_Y (FLOAT)
- 名称：UWB_INIT_OFF_Y (FLOAT)
- 参数描述：UWB sensor Y offset in body frame Comment: UWB sensor positioning in relation to Drone in NED. Y offset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`0.0`
- 单位：`m`


2329. UWB_INIT_OFF_Z (FLOAT)
- 名称：UWB_INIT_OFF_Z (FLOAT)
- 参数描述：UWB sensor Z offset in body frame Comment: UWB sensor positioning in relation to Drone in NED. Z offset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.01)`
- 默认值：`0.0`
- 单位：`m`


2330. UWB_PORT_CFG (INT32)
- 名称：UWB_PORT_CFG (INT32)
- 参数描述：Serial Configuration for Ultrawideband position sensor driver Comment: Configure on which serial port to run Ultrawideband position sensor driver. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2331. UWB_SENS_ROT (INT32)
- 名称：UWB_SENS_ROT (INT32)
- 参数描述：UWB sensor orientation Comment: The orientation of the sensor relative to the forward direction of the body frame. Look up table in src/lib/conversion/rotation.h Default position is the antannaes downward facing, UWB board parallel with body frame. 参数对照:0: ROTATION_NONE 1: ROTATION_YAW_45 2: ROTATION_YAW_90 3: ROTATION_YAW_135 4: ROTATION_YAW_180 5: ROTATION_YAW_225 6: ROTATION_YAW_270 7: ROTATION_YAW_315 8: ROTATION_ROLL_180 9: ROTATION_ROLL_180_YAW_45 10: ROTATION_ROLL_180_YAW_90 11: ROTATION_ROLL_180_YAW_135 12: ROTATION_PITCH_180 13: ROTATION_ROLL_180_YAW_225 14: ROTATION_ROLL_180_YAW_270 15: ROTATION_ROLL_180_YAW_315 16: ROTATION_ROLL_90 17: ROTATION_ROLL_90_YAW_45 18: ROTATION_ROLL_90_YAW_90 19: ROTATION_ROLL_90_YAW_135 20: ROTATION_ROLL_270 21: ROTATION_ROLL_270_YAW_45 22: ROTATION_ROLL_270_YAW_90 23: ROTATION_ROLL_270_YAW_135 24: ROTATION_PITCH_90 25: ROTATION_PITCH_270 26: ROTATION_PITCH_180_YAW_90 27: ROTATION_PITCH_180_YAW_270 28: ROTATION_ROLL_90_PITCH_90 29: ROTATION_ROLL_180_PITCH_90 30: ROTATION_ROLL_270_PITCH_90 31: ROTATION_ROLL_90_PITCH_180 32: ROTATION_ROLL_270_PITCH_180 33: ROTATION_ROLL_90_PITCH_270 34: ROTATION_ROLL_180_PITCH_270 35: ROTATION_ROLL_270_PITCH_270 36: ROTATION_ROLL_90_PITCH_180_YAW_90 37: ROTATION_ROLL_90_YAW_270 38: ROTATION_ROLL_90_PITCH_68_YAW_293 39: ROTATION_PITCH_315 40: ROTATION_ROLL_90_PITCH_315
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2332. UXRCE_DDS_AG_IP (INT32)
- 名称：UXRCE_DDS_AG_IP (INT32)
- 参数描述：uXRCE-DDS Agent IP address Comment: If ethernet is enabled and is the selected configuration for uXRCE-DDS, the selected Agent IP address will be set and used. Decimal dot notation is not supported. IP address must be provided in int32 format. For example, 192.168.1.2 is mapped to -1062731518; 127.0.0.1 is mapped to 2130706433. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2130706433`
- 单位：``


2333. UXRCE_DDS_CFG (INT32)
- 名称：UXRCE_DDS_CFG (INT32)
- 参数描述：Serial Configuration for UXRCE-DDS Client Comment: Configure on which serial port to run UXRCE-DDS Client. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 1000: Ethernet Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2334. UXRCE_DDS_DOM_ID (INT32)
- 名称：UXRCE_DDS_DOM_ID (INT32)
- 参数描述：uXRCE-DDS domain ID Comment: uXRCE-DDS domain ID Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2335. UXRCE_DDS_KEY (INT32)
- 名称：UXRCE_DDS_KEY (INT32)
- 参数描述：uXRCE-DDS session key Comment: uXRCE-DDS key, must be different from zero. In a single agent - multi client configuration, each client must have a unique session key. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


2336. UXRCE_DDS_PRT (INT32)
- 名称：UXRCE_DDS_PRT (INT32)
- 参数描述：uXRCE-DDS UDP port Comment: If ethernet is enabled and is the selected configuration for uXRCE-DDS, the selected UDP port will be set and used. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`8888`
- 单位：``


2337. UXRCE_DDS_PTCFG (INT32)
- 名称：UXRCE_DDS_PTCFG (INT32)
- 参数描述：uXRCE-DDS participant configuration Comment: Set the participant configuration on the Agent's system. 0: Use the default configuration. 1: Restrict messages to localhost (use in combination with ROS_LOCALHOST_ONLY=1). 2: Use a custom participant with the profile name "px4_participant". 参数对照:0: Default 1: Localhost-only 2: Custom participant Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


2338. UXRCE_DDS_SYNCT (INT32)
- 名称：UXRCE_DDS_SYNCT (INT32)
- 参数描述：Enable uXRCE-DDS timestamp synchronization Comment: When enabled, uxrce_dds_client will synchronize the timestamps of the incoming and outgoing messages measuring the offset between the Agent OS time and the PX4 time. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2339. VT_ARSP_BLEND (FLOAT)
- 名称：VT_ARSP_BLEND (FLOAT)
- 参数描述：Transition blending airspeed Comment: Airspeed at which we can start blending both fw and mc controls. Set to 0 to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.00, 30.00] (1)`
- 默认值：`8.0`
- 单位：`m/s`


2340. VT_ARSP_TRANS (FLOAT)
- 名称：VT_ARSP_TRANS (FLOAT)
- 参数描述：Transition airspeed Comment: Airspeed at which we can switch to fw mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.00, 30.00] (1)`
- 默认值：`10.0`
- 单位：`m/s`


2341. VT_BT_TILT_DUR (FLOAT)
- 名称：VT_BT_TILT_DUR (FLOAT)
- 参数描述：Duration motor tilt up in backtransition Comment: Time in seconds it takes to tilt form VT_TILT_FW to VT_TILT_MC.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10] (0.1)`
- 默认值：`1.`
- 单位：`s`


2342. VT_B_DEC_I (FLOAT)
- 名称：VT_B_DEC_I (FLOAT)
- 参数描述：Backtransition deceleration setpoint to pitch I gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.3] (0.05)`
- 默认值：`0.1`
- 单位：`rad s/m`


2343. VT_B_DEC_MSS (FLOAT)
- 名称：VT_B_DEC_MSS (FLOAT)
- 参数描述：Approximate deceleration during back transition Comment: Used to calculate back transition distance in an auto mode. For standard vtol and tiltrotors a controller is used to track this value during the transition.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 10] (0.1)`
- 默认值：`2.0`
- 单位：`m/s^2`


2344. VT_B_TRANS_DUR (FLOAT)
- 名称：VT_B_TRANS_DUR (FLOAT)
- 参数描述：Maximum duration of a back transition Comment: Transition is also declared over if the groundspeed drops below MPC_XY_CRUISE.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 20.00] (1)`
- 默认值：`10.0`
- 单位：`s`


2345. VT_B_TRANS_RAMP (FLOAT)
- 名称：VT_B_TRANS_RAMP (FLOAT)
- 参数描述：Back transition MC motor ramp up time Comment: This sets the duration during which the MC motors ramp up to the commanded thrust during the back transition stage.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 20.0] (0.1)`
- 默认值：`3.0`
- 单位：`s`


2346. VT_ELEV_MC_LOCK (INT32)
- 名称：VT_ELEV_MC_LOCK (INT32)
- 参数描述：Lock control surfaces in hover Comment: If set to 1 the control surfaces are locked at the disarmed value in multicopter mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


2347. VT_FWD_THRUST_EN (INT32)
- 名称：VT_FWD_THRUST_EN (INT32)
- 参数描述：Use fixed-wing actuation in hover to accelerate forward Comment: This feature can be used to avoid the plane having to pitch nose down in order to move forward. Prevents large, negative lift from pitching nose down into wind. Fixed-wing forward actuators refers to puller/pusher (standard VTOL), or forward-tilt (tiltrotor VTOL). Only active if demanded down pitch is below VT_PITCH_MIN. Use VT_FWD_THRUST_SC to tune it. Only active (if enabled) in Altitude, Position and Auto modes, not in Stabilized. 参数对照:0: Disabled 1: Enabled (except LANDING) 2: Enabled if distance to ground above MPC_LAND_ALT1 3: Enabled if distance to ground above MPC_LAND_ALT2 4: Enabled constantly 5: Enabled if distance to ground above MPC_LAND_ALT1 (except LANDING) 6: Enabled if distance to ground above MPC_LAND_ALT2 (except LANDING)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2348. VT_FWD_THRUST_SC (FLOAT)
- 名称：VT_FWD_THRUST_SC (FLOAT)
- 参数描述：Fixed-wing actuation thrust scale for hover forward flight Comment: Scale applied to the demanded down-pitch to get the fixed-wing forward actuation in hover mode. Enabled via VT_FWD_THRUST_EN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.01)`
- 默认值：`0.7`
- 单位：``


2349. VT_FW_DIFTHR_EN (INT32)
- 名称：VT_FW_DIFTHR_EN (INT32)
- 参数描述：Differential thrust in forwards flight Comment: Enable differential thrust seperately for roll, pitch, yaw in forward (fixed-wing) mode. The effectiveness of differential thrust around the corresponding axis can be tuned by setting VT_FW_DIFTHR_S_R / VT_FW_DIFTHR_S_P / VT_FW_DIFTHR_S_Y. Bitmask:0: Yaw 1: Roll 2: Pitch
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 7]`
- 默认值：`0`
- 单位：``


2350. VT_FW_DIFTHR_S_P (FLOAT)
- 名称：VT_FW_DIFTHR_S_P (FLOAT)
- 参数描述：Pitch differential thrust factor in forward flight Comment: Differential thrust in forward flight is enabled via VT_FW_DIFTHR_EN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.1)`
- 默认值：`1.`
- 单位：``


2351. VT_FW_DIFTHR_S_R (FLOAT)
- 名称：VT_FW_DIFTHR_S_R (FLOAT)
- 参数描述：Roll differential thrust factor in forward flight Comment: Differential thrust in forward flight is enabled via VT_FW_DIFTHR_EN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.1)`
- 默认值：`1.`
- 单位：``


2352. VT_FW_DIFTHR_S_Y (FLOAT)
- 名称：VT_FW_DIFTHR_S_Y (FLOAT)
- 参数描述：Yaw differential thrust factor in forward flight Comment: Differential thrust in forward flight is enabled via VT_FW_DIFTHR_EN.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0] (0.1)`
- 默认值：`0.1`
- 单位：``


2353. VT_FW_MIN_ALT (FLOAT)
- 名称：VT_FW_MIN_ALT (FLOAT)
- 参数描述：Quad-chute altitude Comment: Minimum altitude for fixed-wing flight. When the vehicle is in fixed-wing mode and the altitude drops below this altitude (relative altitude above local origin), it will instantly switch back to MC mode and execute behavior defined in COM_QC_ACT.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 200.0] (1)`
- 默认值：`0.0`
- 单位：`m`


2354. VT_FW_QC_HMAX (INT32)
- 名称：VT_FW_QC_HMAX (INT32)
- 参数描述：Quad-chute maximum height Comment: Maximum height above the ground (if available, otherwise above Home if available, otherwise above the local origin) where triggering a quad-chute is possible. At high altitudes there is a big risk to deplete the battery and therefore crash if quad-chuting there.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (1)`
- 默认值：`0`
- 单位：`m`


2355. VT_FW_QC_P (INT32)
- 名称：VT_FW_QC_P (INT32)
- 参数描述：Quad-chute max pitch threshold Comment: Absolute pitch threshold for quad-chute triggering in FW mode. Above this the vehicle will transition back to MC mode and execute behavior defined in COM_QC_ACT. Set to 0 do disable this threshold.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 180]`
- 默认值：`0`
- 单位：`deg`


2356. VT_FW_QC_R (INT32)
- 名称：VT_FW_QC_R (INT32)
- 参数描述：Quad-chute max roll threshold Comment: Absolute roll threshold for quad-chute triggering in FW mode. Above this the vehicle will transition back to MC mode and execute behavior defined in COM_QC_ACT. Set to 0 do disable this threshold.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 180]`
- 默认值：`0`
- 单位：`deg`


2357. VT_F_TRANS_DUR (FLOAT)
- 名称：VT_F_TRANS_DUR (FLOAT)
- 参数描述：Duration of a front transition Comment: Time in seconds used for a transition
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 20.00] (1)`
- 默认值：`5.0`
- 单位：`s`


2358. VT_F_TRANS_THR (FLOAT)
- 名称：VT_F_TRANS_THR (FLOAT)
- 参数描述：Target throttle value for the transition to fixed-wing flight
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`1.0`
- 单位：``


2359. VT_F_TR_OL_TM (FLOAT)
- 名称：VT_F_TR_OL_TM (FLOAT)
- 参数描述：Airspeed-less front transition time (open loop) Comment: The duration of the front transition when there is no airspeed feedback available.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 30.0] (0.5)`
- 默认值：`6.0`
- 单位：`s`


2360. VT_LND_PITCH_MIN (FLOAT)
- 名称：VT_LND_PITCH_MIN (FLOAT)
- 参数描述：Minimum pitch angle during hover landing Comment: Overrides VT_PITCH_MIN when the vehicle is in LAND mode (hovering). During landing it can be beneficial to reduce the pitch angle to reduce the generated lift in head wind.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-10.0, 45.0] (0.1)`
- 默认值：`-5.0`
- 单位：`deg`


2361. VT_PITCH_MIN (FLOAT)
- 名称：VT_PITCH_MIN (FLOAT)
- 参数描述：Minimum pitch angle during hover Comment: Any pitch setpoint below this value is translated to a forward force by the fixed-wing forward actuation if VT_FW_TRHUST_EN is set to 1.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-10.0, 45.0] (0.1)`
- 默认值：`-5.0`
- 单位：`deg`


2362. VT_PSHER_SLEW (FLOAT)
- 名称：VT_PSHER_SLEW (FLOAT)
- 参数描述：Pusher throttle ramp up slew rate Comment: Defines the slew rate of the puller/pusher throttle during transitions. Zero will deactivate the slew rate limiting and thus produce an instant throttle rise to the transition throttle VT_F_TRANS_THR.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (0.01)`
- 默认值：`0.33`
- 单位：`1/s`


2363. VT_QC_ALT_LOSS (FLOAT)
- 名称：VT_QC_ALT_LOSS (FLOAT)
- 参数描述：Quad-chute uncommanded descent threshold Comment: Altitude error threshold for quad-chute triggering during fixed-wing flight. The check is only active if altitude is controlled and the vehicle is below the current altitude reference. The altitude error is relative to the highest altitude the vehicle has achieved since it has flown below the current altitude reference. Set to 0 do disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 200.0] (1)`
- 默认值：`0.0`
- 单位：`m`


2364. VT_QC_T_ALT_LOSS (FLOAT)
- 名称：VT_QC_T_ALT_LOSS (FLOAT)
- 参数描述：Quad-chute transition altitude loss threshold Comment: Altitude loss threshold for quad-chute triggering during VTOL transition to fixed-wing flight in altitude-controlled flight modes. Active until 5s after completing transition to fixed-wing. If the current altitude is more than this value below the altitude at the beginning of the transition, it will instantly switch back to MC mode and execute behavior defined in COM_QC_ACT. Set to 0 do disable this threshold.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 50] (1)`
- 默认值：`20.0`
- 单位：`m`


2365. VT_SPOILER_MC_LD (FLOAT)
- 名称：VT_SPOILER_MC_LD (FLOAT)
- 参数描述：Spoiler setting while landing (hover)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.1)`
- 默认值：`0.`
- 单位：`norm`


2366. VT_TILT_FW (FLOAT)
- 名称：VT_TILT_FW (FLOAT)
- 参数描述：Normalized tilt in FW
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`1.0`
- 单位：``


2367. VT_TILT_MC (FLOAT)
- 名称：VT_TILT_MC (FLOAT)
- 参数描述：Normalized tilt in Hover
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.0`
- 单位：``


2368. VT_TILT_TRANS (FLOAT)
- 名称：VT_TILT_TRANS (FLOAT)
- 参数描述：Normalized tilt in transition to FW
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.01)`
- 默认值：`0.4`
- 单位：``


2369. VT_TRANS_MIN_TM (FLOAT)
- 名称：VT_TRANS_MIN_TM (FLOAT)
- 参数描述：Front transition minimum time Comment: Minimum time in seconds for front transition.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 20.0] (0.1)`
- 默认值：`2.0`
- 单位：`s`


2370. VT_TRANS_P2_DUR (FLOAT)
- 名称：VT_TRANS_P2_DUR (FLOAT)
- 参数描述：Duration of front transition phase 2 Comment: Time in seconds it takes to tilt form VT_TILT_TRANS to VT_TILT_FW.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 5.0] (0.01)`
- 默认值：`0.5`
- 单位：`s`


2371. VT_TRANS_TIMEOUT (FLOAT)
- 名称：VT_TRANS_TIMEOUT (FLOAT)
- 参数描述：Front transition timeout Comment: Time in seconds after which transition will be cancelled. Disabled if set to 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 30.00] (1)`
- 默认值：`15.0`
- 单位：`s`


2372. VT_TYPE (INT32)
- 名称：VT_TYPE (INT32)
- 参数描述：VTOL Type (Tailsitter=0, Tiltrotor=1, Standard=2)  Values:0: Tailsitter 1: Tiltrotor 2: Standard Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


2373. WV_GAIN (FLOAT)
- 名称：WV_GAIN (FLOAT)
- 参数描述：Weather-vane roll angle to yawrate Comment: The desired gain to convert roll sp into yaw rate sp.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 3.0] (0.01)`
- 默认值：`1.0`
- 单位：`Hz`


2374. VTO_LOITER_ALT (FLOAT)
- 名称：VTO_LOITER_ALT (FLOAT)
- 参数描述：VTOL Takeoff relative loiter altitude Comment: Altitude relative to home at which vehicle will loiter after front transition.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20, 300] (1)`
- 默认值：`80`
- 单位：`m`


2375. ZENOH_ENABLE (INT32)
- 名称：ZENOH_ENABLE (INT32)
- 参数描述：Zenoh Enable Comment: Zenoh Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


2376. UUV_SKIP_CTRL (INT32)
- 名称：UUV_SKIP_CTRL (INT32)
- 参数描述：Skip the controller  Values:0: use the module's controller 1: skip the controller and feedthrough the setpoints
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


