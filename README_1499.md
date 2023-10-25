# pix4_parameter_reference
> 使用gpt翻译pix4的参数，并且加上gpt的解释

> https://docs.px4.io/main/zh/advanced_config/parameter_reference.html

1. ctl_bw (INT32)
- 名称：ctl_bw (INT32)
- 参数描述：Speed controller bandwidth Comment: Speed controller bandwidth, in Hz. Higher values result in faster speed and current rise times, but may result in overshoot and higher current consumption. For fixed-wing aircraft, this value should be less than 50 Hz; for multirotors, values up to 100 Hz may provide improvements in responsiveness.
  - 翻译：速度控制器带宽 说明：速度控制器带宽，单位为赫兹（Hz）。较高的数值会导致更快的速度和电流上升时间，但可能会导致超调和更高的电流消耗。对于固定翼飞行器，此数值应低于50赫兹；对于多旋翼飞行器，数值高达100赫兹可能提高响应性能。
  - gpt注解：速度控制器带宽是一个用于调整飞行器响应特性的参数。较高的带宽数值会使飞行器更加敏捷，但潜在风险包括振荡和更高的电流消耗。对于不同类型的飞行器，推荐的带宽范围不同，应根据飞行器类型进行调整。
- `[Min, Max]`：`[10, 250]`
- 默认值：`75`
- 单位：`Hz`


2. ctl_dir (INT32)
- 名称：ctl_dir (INT32)
- 参数描述：Reverse direction Comment: Motor spin direction as detected during initial enumeration. Use 0 or 1 to reverse direction.
  - 翻译：反向方向 说明：电机旋转方向，在初始枚举期间检测到的方向。使用 0 或 1 来反转方向。
  - gpt注解：此参数用于控制电机旋转方向。根据初始枚举时检测到的方向，可以选择 0 或 1 来实现反向旋转。
- `[Min, Max]`：`[0, 1]`
- 默认值：`1`
- 单位：``


3. ctl_get (FLOAT)
- 名称：ctl_get (FLOAT)
- 参数描述：Speed (RPM) controller gain Comment: Speed (RPM) controller gain. Determines controller aggressiveness; units are amp-seconds per radian. Systems with higher rotational inertia (large props) will need gain increased; systems with low rotational inertia (small props) may need gain decreased. Higher values result in faster response, but may result in oscillation and excessive overshoot. Lower values result in a slower, smoother response.
  - 翻译：速度（RPM）控制器增益 说明：速度（RPM）控制器增益。决定控制器的侵略性；单位为安培秒每弧度。具有较大转动惯量（大螺旋桨）的系统需要增加增益；具有低转动惯量（小螺旋桨）的系统可能需要降低增益。较高的值会导致更快的响应，但可能会引起振荡和过度超调。较低的值会导致较慢、更平稳的响应。
  - gpt注解：速度控制器增益是一个用于调整速度响应特性的参数。增加增益可以使控制器更加激进，但对于具有较大转动惯量的系统可能需要增加增益，而对于具有较小转动惯量的系统可能需要降低增益。较高的增益值会导致更快的响应，但可能会产生振荡和过度超调。较低的增益值会导致响应速度较慢，但更平稳。
- `[Min, Max]`：`[0.00, 1.00]`
- 默认值：`1`
- 单位：`C/rad`


4. ctl_hz_idle (FLOAT)
- 名称：ctl_hz_idle (FLOAT)
- 参数描述：Idle speed (e Hz) Comment: Idle speed (e Hz)
  - 翻译：空闲速度（e赫兹） 说明：空闲速度（e赫兹）
  - gpt注解：空闲速度是指无负载情况下电机的运行速度，单位为e赫兹。
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`3.5`
- 单位：`Hz`


5. ctl_start_rate (INT32)
- 名称：ctl_start_rate (INT32)
- 参数描述：Spin-up rate (e Hz/s) Comment: Spin-up rate (e Hz/s)
  - 翻译：启动速率（e赫兹/秒） 说明：启动速率（e赫兹/秒）
  - gpt注解：启动速率指的是电机从静止状态加速至目标速度的速率，单位为e赫兹每秒。
- `[Min, Max]`：`[5, 1000]`
- 默认值：`25`
- 单位：`1/s^2`


6. esc_index (INT32)
- 名称：esc_index (INT32)
- 参数描述：Index of this ESC in throttle command messages. Comment: Index of this ESC in throttle command messages.
  - 翻译：电调索引在油门命令消息中的位置 说明：电调索引在油门命令消息中的位置。
  - gpt注解：电调索引是指在油门命令消息中确定此电调的位置。通常，该值范围从0到15，对应着不同电调的位置。
- `[Min, Max]`：`[0, 15]`
- 默认值：`0`
- 单位：``


7. id_ext_status (INT32)
- 名称：id_ext_status (INT32)
- 参数描述：Extended status ID Comment: Extended status ID
  - 翻译：扩展状态标识 说明：扩展状态标识
  - gpt注解：扩展状态标识用于标记特定的状态或事件。其值范围通常从1到1000000。
- `[Min, Max]`：`[1, 1000000]`
- 默认值：`20034`
- 单位：``


8. int_ext_status (INT32)
- 名称：int_ext_status (INT32)
- 参数描述：Extended status interval (µs) Comment: Extended status interval (µs)
  - 翻译：扩展状态间隔（微秒） 说明：扩展状态间隔（微秒）
  - gpt注解：扩展状态间隔是指生成扩展状态信息的时间间隔，单位为微秒（µs）。该间隔决定了扩展状态信息的更新频率。
- `[Min, Max]`：`[0, 1000000]`
- 默认值：`50000`
- 单位：`µs`


9. int_status (INT32)
- 名称：int_status (INT32)
- 参数描述：ESC status interval (µs) Comment: ESC status interval (µs)
  - 翻译：电调状态间隔（微秒） 说明：电调状态间隔（微秒）
  - gpt注解：电调状态间隔是指生成电调状态信息的时间间隔，单位为微秒（µs）。该间隔决定了电调状态信息的更新频率。
- `[Min, Max]`：`[?, 1000000]`
- 默认值：`50000`
- 单位：`µs`


10. mot_i_max (FLOAT)
- 名称：mot_i_max (FLOAT)
- 参数描述：Motor current limit in amps Comment: Motor current limit in amps. This determines the maximum current controller setpoint, as well as the maximum allowable current setpoint slew rate. This value should generally be set to the continuous current rating listed in the motor’s specification sheet, or set equal to the motor’s specified continuous power divided by the motor voltage limit.
  - 翻译：电机电流限制（安培） 说明：电机电流限制（安培）。这确定了电流控制器的最大电流设定点，以及最大允许的电流设定点斜率。通常，此值应设置为电机规格表中列出的连续电流额定值，或设置为电机指定的连续功率除以电机电压限制。
  - gpt注解：电机电流限制是指电机能够承受的最大电流值，单位为安培（A）。它不仅影响电流控制器的最大电流设定点，还影响电流设定点的最大允许斜率。通常，应将此值设置为电机规格表中列出的连续电流额定值，或根据电机的连续功率和电压限制来计算。
- `[Min, Max]`：`[1, 80]`
- 默认值：`12`
- 单位：`A`


11. mot_kv (INT32)
- 名称：mot_kv (INT32)
- 参数描述：Motor Kv in RPM per volt Comment: Motor Kv in RPM per volt. This can be taken from the motor’s specification sheet; accuracy will help control performance but some deviation from the specified value is acceptable.
  - 翻译：电机Kv值（每伏特转数） 说明：电机Kv值，单位为每伏特转数（rpm/V）。可以从电机的规格表中获取；精确度将有助于控制性能，但允许与规定值有一定偏差。
  - gpt注解：电机Kv值是指每伏特电压下电机的旋转速度，单位为每伏特转数（rpm/V）。这个值通常可以从电机的规格表中找到，精确的数值有助于控制性能，但允许有一定的偏差。
- `[Min, Max]`：`[0, 4000]`
- 默认值：`2300`
- 单位：`rpm/V`


12. mot_ls (FLOAT)
- 名称：mot_ls (FLOAT)
- 参数描述：READ ONLY: Motor inductance in henries. Comment: READ ONLY: Motor inductance in henries. This is measured on start-up.
  - 翻译：只读：电机电感（亨利） 说明：只读：电机电感（亨利）。这是在启动时测量的。
  - gpt注解：电机电感是指电机的电感值，单位为亨利（H）。此参数是只读的，表示无法进行设置或更改，其值是在电机启动时进行测量的。
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`H`


13. mot_num_poles (INT32)
- 名称：mot_num_poles (INT32)
- 参数描述：Number of motor poles. Comment: Number of motor poles. Used to convert mechanical speeds to electrical speeds. This number should be taken from the motor’s specification sheet.
  - 翻译：电机极数 说明：电机极数。用于将机械速度转换为电机速度。这个数值应该从电机的规格表中获取。
  - gpt注解：电机极数是指电机内部的磁极数量。它用于将机械速度转换为电机电气速度。通常，应该从电机的规格表中获取这个数值。
- `[Min, Max]`：`[2, 40]`
- 默认值：`14`
- 单位：``


14. mot_rs (FLOAT)
- 名称：mot_rs (FLOAT)
- 参数描述：READ ONLY: Motor resistance in ohms Comment: READ ONLY: Motor resistance in ohms. This is measured on start-up. When tuning a new motor, check that this value is approximately equal to the value shown in the motor’s specification sheet.
  - 翻译：只读：电机电阻（欧姆） 说明：只读：电机电阻（欧姆）。这是在启动时测量的。在调谐新电机时，检查此值是否与电机规格表中显示的数值大致相等。
  - gpt注解：电机电阻是指电机内部的电阻值，单位为欧姆。此参数是只读的，表示无法进行设置或更改，其值是在电机启动时进行测量的。当调谐新电机时，应检查此值是否与电机规格表中显示的数值大致相等。
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`欧姆`


15. mot_v_accel (FLOAT)
- 名称：mot_v_accel (FLOAT)
- 参数描述：Acceleration limit (V) Comment: Acceleration limit (V)
  - 翻译：加速度限制（伏特） 说明：加速度限制（伏特）
  - gpt注解：加速度限制指的是电机电压的加速度限制，单位为伏特（V）。此参数限制了电机电压的变化速率，用于控制加速和减速的速度。通常，较低的值会导致更平稳的加减速过程，而较高的值会导致更快的加减速，但可能引起不稳定。
- `[Min, Max]`：`[0.01, 1.00]`
- 默认值：`0.5`
- 单位：`V`


16. mot_v_max (FLOAT)
- 名称：mot_v_max (FLOAT)
- 参数描述：Motor voltage limit in volts Comment: Motor voltage limit in volts. The current controller’s commanded voltage will never exceed this value. Note that this may safely be above the nominal voltage of the motor; to determine the actual motor voltage limit, divide the motor’s rated power by the motor current limit.
  - 翻译：电机电压限制（伏特） 说明：电机电压限制（伏特）。电流控制器的命令电压永远不会超过此值。请注意，这个值可以安全地高于电机的名义电压；要确定实际的电机电压限制，将电机的额定功率除以电机的电流限制。
  - gpt注解：电机电压限制是指电机电压的最大允许值，单位为伏特（V）。电流控制器的命令电压永远不会超过这个限制。需要注意的是，这个值可以安全地高于电机的名义电压，但要确定实际的电机电压限制，可以将电机的额定功率除以电机的电流限制来计算。
- `[Min, Max]`：`[0, ?]`
- 默认值：`14.8`
- 单位：`V`


17. gnss.dyn_model (INT32)
- 名称：gnss.dyn_model (INT32)
- 参数描述：GNSS dynamic model Comment: Dynamic model used in the GNSS positioning engine. 0 – Automotive, 1 – Sea, 2 – Airborne.
  - 翻译：GNSS动态模型 说明：用于GNSS定位引擎的动态模型。0 – 汽车，1 – 海上，2 – 空中。
  - gpt注解：GNSS动态模型是指用于GNSS定位引擎的运动模型。0表示汽车，1表示海上，2表示空中。不同的动态模型用于适应不同应用场景，例如汽车导航、海上导航或空中导航。
- `[Min, Max]`：`[0, 2]`
- 默认值：`2`
- 单位：``


18. gnss.old_fix_msg (INT32)
- 名称：gnss.old_fix_msg (INT32)
- 参数描述：Broadcast old GNSS fix message Comment: Broadcast the old (deprecated) GNSS fix message uavcan.equipment.gnss.Fix alongside the new alternative uavcan.equipment.gnss.Fix2. It is recommended to disable this feature to reduce the CAN bus traffic.
  - 翻译：广播旧的GNSS定位信息消息 说明：在新的替代方案uavcan.equipment.gnss.Fix2之外，广播旧的（已弃用的）GNSS定位信息消息uavcan.equipment.gnss.Fix。建议禁用此功能以减少CAN总线流量。
  - gpt注解：广播旧的GNSS定位信息消息可以同时与新的uavcan.equipment.gnss.Fix2消息一起广播。然而，出于减少CAN总线流量的考虑，建议禁用此功能。参数取值为0表示只广播Fix2，取值为1表示同时广播Fix和Fix2。
- `[Min, Max]`：`[0, 1]`
- 默认值：`1`
- 单位：``


19. gnss.warn_dimens (INT32)
- 名称：gnss.warn_dimens (INT32)
- 参数描述：device health warning Comment: Set the device health to Warning if the dimensionality of the GNSS solution is less than this value. 3 for the full (3D) solution, 2 for planar (2D) solution, 1 for time-only solution, 0 disables the feature.
  - 翻译：设备健康警告 说明：如果GNSS解决方案的维度小于此值，则将设备健康状态设置为警告。3表示完整（3D）解决方案，2表示平面（2D）解决方案，1表示仅时间解决方案，0禁用此功能。
  - gpt注解：设备健康警告是指在GNSS解决方案的维度低于特定值时，将设备的健康状态设置为警告。具体取值说明：3表示完整（3D）解决方案，2表示平面（2D）解决方案，1表示仅时间解决方案，0表示禁用此功能。
- `[Min, Max]`：`[0, 3]`
- 默认值：`0`
- 单位：``


20. gnss.warn_sats (INT32)
- 名称：gnss.warn_sats (INT32)
- 参数描述：Comment: Set the device health to Warning if the number of satellites used in the GNSS solution is below this threshold. Zero disables the feature.
  - 翻译：设备健康警告卫星数阈值 说明：如果用于GNSS解决方案的卫星数量低于此阈值，将设备健康状态设置为警告。零禁用此功能。
  - gpt注解：设备健康警告卫星数阈值是指当GNSS解决方案中使用的卫星数量低于特定值时，将设备的健康状态设置为警告。零表示禁用此功能。
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


21. uavcan.pubp-pres (INT32)
- 名称：uavcan.pubp-pres (INT32)
- 参数描述：Comment: Set the device health to Warning if the number of satellites used in the GNSS solution is below this threshold. Zero disables the feature.
  - 翻译：设置设备健康状态为警告，如果GNSS解决方案中使用的卫星数量低于此阈值，则设备健康状态为警告。零禁用此功能。
  - gpt注解：当GNSS解决方案中使用的卫星数量低于特定阈值时，设置设备的健康状态为警告。零表示禁用此功能。
- `[Min, Max]`：`[0, 1000000]`
- 默认值：`0`
- 单位：`µs`


22. ADSB_CALLSIGN_1 (INT32)
- 名称：ADSB_CALLSIGN_1 (INT32)
- 参数描述：First 4 characters of CALLSIGN Comment: Sets first 4 characters of a total of 8. Valid characters are A-Z, 0-9, " ". Example "PX4 " -> 1347957792 For CALLSIGN shorter than 8 characters use the null terminator at the end '\0'. Reboot required: true
  - 翻译：呼号的前4个字符 说明：设置呼号的前4个字符，总共8个字符。有效字符包括A-Z、0-9和空格。例如 "PX4 " -> 1347957792 如果呼号长度不足8个字符，请在末尾使用空字符 '\0'。需要重新启动：是
  - gpt注解：呼号的前4个字符是呼号的一部分，总共包括8个字符。这些字符必须是有效的，有效字符包括大写字母A-Z、数字0-9和空格。例如，"PX4 " -> 1347957792。如果呼号长度不足8个字符，应在末尾使用空字符 '\0' 来填充。更改此参数后需要重新启动设备。
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


23. ADSB_CALLSIGN_2 (INT32)
- 名称：ADSB_CALLSIGN_2 (INT32)
- 参数描述：Second 4 characters of CALLSIGN Comment: Sets second 4 characters of a total of 8. Valid characters are A-Z, 0-9, " " only. Example "TEST" -> 1413829460 For CALLSIGN shorter than 8 characters use the null terminator at the end '\0'. Reboot required: true
  - 翻译：呼号的后4个字符 说明：设置呼号的后4个字符，总共8个字符。有效字符包括A-Z、0-9和空格。例如 "TEST" -> 1413829460 如果呼号长度不足8个字符，请在末尾使用空字符 '\0'。需要重新启动：是
  - gpt注解：呼号的后4个字符是呼号的一部分，总共包括8个字符。这些字符必须是有效的，有效字符包括大写字母A-Z、数字0-9和空格。例如，"TEST" -> 1413829460。如果呼号长度不足8个字符，应在末尾使用空字符 '\0' 来填充。更改此参数后需要重新启动设备。
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


24. ADSB_EMERGC (INT32)
- 名称：ADSB_EMERGC (INT32)
- 参数描述：ADSB-Out Emergency State Comment: Sets the vehicle emergency state
  - 翻译：ADSB-Out紧急状态 说明：设置飞行器的紧急状态
  - gpt注解：ADSB-Out紧急状态是指设置飞行器的紧急状态。具体取值如下：0: 无紧急情况 1: 一般情况 2: 医疗情况 3: 低燃料情况 4: 无通信情况 5: 干扰情况 6: 坠毁情况 更改此参数后无需重新启动设备。
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


25. ADSB_EMIT_TYPE (INT32)
- 名称：ADSB_EMIT_TYPE (INT32)
- 参数描述：ADSB-Out Vehicle Emitter Type Comment: Configure the emitter type of the vehicle.
  - 翻译：ADSB-Out飞行器发射器类型 说明：配置飞行器的发射器类型
  - gpt注解：ADSB-Out飞行器发射器类型用于配置飞行器的发射器类型。具体取值如下：0: 未知 1: 轻型 2: 小型 3: 大型 4: 高涡旋 5: 重型 6: 高性能 7: 旋翼机 8: 保留 9: 滑翔机 10: 轻型飞行器 11: 降落伞 12: 超轻型飞行器 13: 保留 14: 无人机（UAV） 15: 太空飞行器 更改此参数后需要重新启动设备。
- `[Min, Max]`：`[0, 15]`
- 默认值：`14`
- 单位：``


26. ADSB_GPS_OFF_LAT (INT32)
- 名称：ADSB_GPS_OFF_LAT (INT32)
- 参数描述：ADSB-Out GPS Offset lat Comment: Sets GPS lateral offset encoding
  - 翻译：ADSB-Out GPS横向偏移纬度 说明：设置GPS横向偏移编码
  - gpt注解：ADSB-Out GPS横向偏移纬度用于设置GPS的横向偏移编码。具体取值如下：0: 无数据 1: 纬度向左2米 2: 纬度向左4米 3: 纬度向左6米 4: 纬度向右0米 5: 纬度向右2米 6: 纬度向右4米 7: 纬度向右6米 更改此参数后无需重新启动设备。
- `[Min, Max]`：`[0, 7]`
- 默认值：`0`
- 单位：``


27. ADSB_GPS_OFF_LON (INT32)
- 名称：ADSB_GPS_OFF_LON (INT32)
- 参数描述：ADSB-Out GPS Offset lon Comment: Sets GPS longitudinal offset encoding
  - 翻译：ADSB-Out GPS纵向偏移经度 说明：设置GPS纵向偏移编码
  - gpt注解：ADSB-Out GPS纵向偏移经度用于设置GPS的纵向偏移编码。具体取值如下：0: 无数据 1: 传感器应用 更改此参数后无需重新启动设备。
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


28. ADSB_ICAO_ID (INT32)
- 名称：ADSB_ICAO_ID (INT32)
- 参数描述：ADSB-Out ICAO configuration Comment: Defines the ICAO ID of the vehicle
  - 翻译：ADSB-Out ICAO配置 说明：定义飞行器的ICAO ID
  - gpt注解：ADSB-Out ICAO配置用于定义飞行器的ICAO ID。ICAO ID是国际民航组织（ICAO）为每架飞行器分配的唯一标识符。更改此参数后需要重新启动设备。
- `[Min, Max]`：`[-1, 16777215]`
- 默认值：`1194684`
- 单位：``


29. ADSB_ICAO_SPECL (INT32)
- 名称：ADSB_ICAO_SPECL (INT32)
- 参数描述：ADSB-In Special ICAO configuration Comment: This vehicle is always tracked. Use 0 to disable.
  - 翻译：ADSB-In特殊ICAO配置 说明：此飞行器始终被跟踪。使用0来禁用。
  - gpt注解：ADSB-In特殊ICAO配置用于指定此飞行器始终被跟踪。使用0来禁用此功能。更改此参数后无需重新启动设备。
- `[Min, Max]`：`[0, 16777215]`
- 默认值：`0`
- 单位：``


30. ADSB_IDENT (INT32)
- 名称：ADSB_IDENT (INT32)
- 参数描述：ADSB-Out Ident Configuration Comment: Enable Identification of Position feature
  - 翻译：ADSB-Out识别配置 说明：启用位置识别功能
  - gpt注解：ADSB-Out识别配置用于启用位置识别功能。启用此功能后，飞行器的位置将被识别。更改此参数后无需重新启动设备。
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


31. ADSB_LEN_WIDTH (INT32)
- 名称：ADSB_LEN_WIDTH (INT32)
- 参数描述：ADSB-Out Vehicle Size Configuration Comment: Report the length and width of the vehicle in meters. In most cases, use '1' for the smallest vehicle size.
  - 翻译：ADSB-Out飞行器尺寸配置 说明：报告飞行器的长度和宽度，单位为米。在大多数情况下，使用'1'表示最小的飞行器尺寸。
  - gpt注解：ADSB-Out飞行器尺寸配置用于报告飞行器的长度和宽度，单位为米。在大多数情况下，使用'1'来表示最小的飞行器尺寸。具体取值如下：0: 尺寸未知 1: 长15米，宽23米 2: 长25米，宽28米 3: 长25米，宽34米 4: 长35米，宽33米 5: 长35米，宽38米 6: 长45米，宽39米 7: 长45米，宽45米 8: 长55米，宽45米 9: 长55米，宽52米 10: 长65米，宽59米 11: 长65米，宽67米 12: 长75米，宽72米 13: 长75米，宽80米 14: 长85米，宽80米 15: 长85米，宽90米 更改此参数后需要重新启动设备。
- `[Min, Max]`：`[0, 15]`
- 默认值：`1`
- 单位：``


32. ADSB_LIST_MAX (INT32)
- 名称：ADSB_LIST_MAX (INT32)
- 参数描述：ADSB-In Vehicle List Size Comment: Change number of targets to track
  - 翻译：ADSB-In飞行器列表大小 说明：更改要跟踪的目标数量
  - gpt注解：ADSB-In飞行器列表大小用于更改要跟踪的目标数量。具体范围为0到50。更改此参数后需要重新启动设备。
- `[Min, Max]`：`[0, 50]`
- 默认值：`25`
- 单位：``


33. ADSB_MAX_SPEED (INT32)
- 名称：ADSB_MAX_SPEED (INT32)
- 参数描述：ADSB-Out Vehicle Max Speed Comment: Informs ADSB vehicles of this vehicle's max speed capability
  - 翻译：ADSB-Out飞行器最大速度 说明：通知ADSB飞行器本飞行器的最大速度能力
  - gpt注解：ADSB-Out飞行器最大速度用于通知ADSB飞行器本飞行器的最大速度能力。具体取值如下：0: 未知最大速度 1: 75节（约138.9公里/小时） 2: 150节（约277.8公里/小时） 3: 300节（约555.6公里/小时） 4: 600节（约1111.1公里/小时） 5: 1200节（约2222.2公里/小时） 6: 超过1200节 更改此参数后需要重新启动设备。
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


34. ADSB_SQUAWK (INT32)
- 名称：ADSB_SQUAWK (INT32)
- 参数描述：ADSB-Out squawk code configuration Comment: This parameter defines the squawk code. Value should be between 0000 and 7777.
  - 翻译：ADSB-Out应急频率码配置 说明：此参数定义了应急频率码。值应在0000和7777之间。
  - gpt注解：ADSB-Out应急频率码配置用于定义应急频率码。应急频率码是一个4位数值，通常用于飞行器的识别和通信。此参数的值应在0000和7777之间。更改此参数后无需重新启动设备。
- `[Min, Max]`：`[0, 7777]`
- 默认值：`1200`
- 单位：``


35. MODAL_IO_FUNC1 (INT32)
- 名称：MODAL_IO_FUNC1 (INT32)
- 参数描述：MODAL IO Output ESC 1 Output Function Comment: Select what should be output on MODAL IO Output ESC 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest
  - 翻译：MODAL IO输出 ESC 1输出功能 说明：选择应该输出到MODAL IO输出 ESC 1上的内容。默认的失控保护值根据所选功能设置如下： - '最小' 对于ConstantMin - '最大' 对于ConstantMax - '最大' 对于Parachute -  ('最大'+'最小')/2 对于Servos - 'Disarmed' 对于其余情况
  - gpt注解：MODAL IO输出 ESC 1输出功能用于选择应该输出到MODAL IO输出 ESC 1上的内容。默认的失控保护值取决于所选功能： - '最小' 适用于ConstantMin - '最大' 适用于ConstantMax - '最大' 适用于Parachute - ('最大'+'最小')/2 适用于Servos - 'Disarmed' 适用于其余情况。具体取值如下：0: 禁用 1: Constant Min 2: Constant Max 101: 电机 1 102: 电机 2 103: 电机 3 104: 电机 4 105: 电机 5 106: 电机 6 107: 电机 7 108: 电机 8 109: 电机 9 110: 电机 10 111: 电机 11 112: 电机 12 201: 舵机 1 202: 舵机 2 203: 舵机 3 204: 舵机 4 205: 舵机 5 206: 舵机 6 207: 舵机 7 208: 舵机 8 301: 离轨执行器设置 1 302: 离轨执行器设置 2 303: 离轨执行器设置 3 304: 离轨执行器设置 4 305: 离轨执行器设置 5 306: 离轨执行器设置 6 400: 起落架 401: 降落伞 402: 遥控滚动 403: 遥控俯仰 404: 遥控油门 405: 遥控偏航 406: 遥控襟翼 407: 遥控辅助 1 408: 遥控辅助 2 409: 遥控辅助 3 410: 遥控辅助 4 411: 遥控辅助 5 412: 遥控辅助 6 420: 云台滚动 421: 云台俯仰 422: 云台偏航 430: 抓手 440: 起落架轮子
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


36. MODAL_IO_FUNC2 (INT32)
- 名称：MODAL_IO_FUNC2 (INT32)
- 参数描述：MODAL IO Output ESC 2 Output Function Comment: Select what should be output on MODAL IO Output ESC 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest
  - 翻译：MODAL IO输出 ESC 2输出功能 说明：选择应该输出到MODAL IO输出 ESC 2上的内容。默认的失控保护值根据所选功能设置如下： - '最小' 对于ConstantMin - '最大' 对于ConstantMax - '最大' 对于Parachute -  ('最大'+'最小')/2 对于Servos - 'Disarmed' 对于其余情况
  - gpt注解：MODAL IO输出 ESC 2输出功能用于选择应该输出到MODAL IO输出 ESC 2上的内容。默认的失控保护值取决于所选功能： - '最小' 适用于ConstantMin - '最大' 适用于ConstantMax - '最大' 适用于Parachute - ('最大'+'最小')/2 适用于Servos - 'Disarmed' 适用于其余情况。具体取值如下：0: 禁用 1: Constant Min 2: Constant Max 101: 电机 1 102: 电机 2 103: 电机 3 104: 电机 4 105: 电机 5 106: 电机 6 107: 电机 7 108: 电机 8 109: 电机 9 110: 电机 10 111: 电机 11 112: 电机 12 201: 舵机 1 202: 舵机 2 203: 舵机 3 204: 舵机 4 205: 舵机 5 206: 舵机 6 207: 舵机 7 208: 舵机 8 301: 离轨执行器设置 1 302: 离轨执行器设置 2 303: 离轨执行器设置 3 304: 离轨执行器设置 4 305: 离轨执行器设置 5 306: 离轨执行器设置 6 400: 起落架 401: 降落伞 402: 遥控滚动 403: 遥控俯仰 404: 遥控油门 405: 遥控偏航 406: 遥控襟翼 407: 遥控辅助 1 408: 遥控辅助 2 409: 遥控辅助 3 410: 遥控辅助 4 411: 遥控辅助 5 412: 遥控辅助 6 420: 云台滚动 421: 云台俯仰 422: 云台偏航 430: 抓手 440: 起落架轮子
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


37. MODAL_IO_FUNC3 (INT32)
- 名称：MODAL_IO_FUNC3 (INT32)
- 参数描述：MODAL IO Output ESC 3 Output Function Comment: Select what should be output on MODAL IO Output ESC 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest
  - 翻译：MODAL IO输出 ESC 3输出功能 说明：选择应该输出到MODAL IO输出 ESC 3上的内容。默认的失控保护值根据所选功能设置如下： - '最小' 对于ConstantMin - '最大' 对于ConstantMax - '最大' 对于Parachute -  ('最大'+'最小')/2 对于Servos - 'Disarmed' 对于其余情况
  - gpt注解：MODAL IO输出 ESC 3输出功能用于选择应该输出到MODAL IO输出 ESC 3上的内容。默认的失控保护值取决于所选功能： - '最小' 适用于ConstantMin - '最大' 适用于ConstantMax - '最大' 适用于Parachute - ('最大'+'最小')/2 适用于Servos - 'Disarmed' 适用于其余情况。具体取值如下：0: 禁用 1: Constant Min 2: Constant Max 101: 电机 1 102: 电机 2 103: 电机 3 104: 电机 4 105: 电机 5 106: 电机 6 107: 电机 7 108: 电机 8 109: 电机 9 110: 电机 10 111: 电机 11 112: 电机 12 201: 舵机 1 202: 舵机 2 203: 舵机 3 204: 舵机 4 205: 舵机 5 206: 舵机 6 207: 舵机 7 208: 舵机 8 301: 离轨执行器设置 1 302: 离轨执行器设置 2 303: 离轨执行器设置 3 304: 离轨执行器设置 4 305: 离轨执行器设置 5 306: 离轨执行器设置 6 400: 起落架 401: 降落伞 402: 遥控滚动 403: 遥控俯仰 404: 遥控油门 405: 遥控偏航 406: 遥控襟翼 407: 遥控辅助 1 408: 遥控辅助 2 409: 遥控辅助 3 410: 遥控辅助 4 411: 遥控辅助 5 412: 遥控辅助 6 420: 云台滚动 421: 云台俯仰 422: 云台偏航 430: 抓手 440: 起落架轮子
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


38. MODAL_IO_FUNC4 (INT32)
- 名称：MODAL_IO_FUNC4 (INT32)
- 参数描述：MODAL IO Output ESC 4 Output Function Comment: Select what should be output on MODAL IO Output ESC 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest
  - 翻译：MODAL IO输出 ESC 4输出功能 说明：选择应该输出到MODAL IO输出 ESC 4上的内容。默认的失控保护值根据所选功能设置如下： - '最小' 对于ConstantMin - '最大' 对于ConstantMax - '最大' 对于Parachute -  ('最大'+'最小')/2 对于Servos - 'Disarmed' 对于其余情况
  - gpt注解：MODAL IO输出 ESC 4输出功能用于选择应该输出到MODAL IO输出 ESC 4上的内容。默认的失控保护值取决于所选功能： - '最小' 适用于ConstantMin - '最大' 适用于ConstantMax - '最大' 适用于Parachute - ('最大'+'最小')/2 适用于Servos - 'Disarmed' 适用于其余情况。具体取值如下：0: 禁用 1: Constant Min 2: Constant Max 101: 电机 1 102: 电机 2 103: 电机 3 104: 电机 4 105: 电机 5 106: 电机 6 107: 电机 7 108: 电机 8 109: 电机 9 110: 电机 10 111: 电机 11 112: 电机 12 201: 舵机 1 202: 舵机 2 203: 舵机 3 204: 舵机 4 205: 舵机 5 206: 舵机 6 207: 舵机 7 208: 舵机 8 301: 离轨执行器设置 1 302: 离轨执行器设置 2 303: 离轨执行器设置 3 304: 离轨执行器设置 4 305: 离轨执行器设置 5 306: 离轨执行器设置 6 400: 起落架 401: 降落伞 402: 遥控滚动 403: 遥控俯仰 404: 遥控油门 405: 遥控偏航 406: 遥控襟翼 407: 遥控辅助 1 408: 遥控辅助 2 409: 遥控辅助 3 410: 遥控辅助 4 411: 遥控辅助 5 412: 遥控辅助 6 420: 云台滚动 421: 云台俯仰 422: 云台偏航 430: 抓手 440: 起落架轮子
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


39. MODAL_IO_REV (INT32)
- 名称：MODAL_IO_REV (INT32)
- 参数描述：Reverse Output Range for MODAL IO Output Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: MODAL IO Output ESC 1 1: MODAL IO Output ESC 2 2: MODAL IO Output ESC 3 3: MODAL IO Output ESC 4
  - 翻译：MODAL IO输出通道反向输出范围 说明：允许反向输出范围的每个通道。注意：这仅对舵机有用。位掩码：0: MODAL IO输出 ESC 1 1: MODAL IO输出 ESC 2 2: MODAL IO输出 ESC 3 3: MODAL IO输出 ESC 4
  - gpt注解：MODAL IO输出通道反向输出范围用于允许反向输出范围的每个通道。请注意，这仅对舵机有用。位掩码表示哪些通道应用反向输出范围：0: MODAL IO输出 ESC 1 1: MODAL IO输出 ESC 2 2: MODAL IO输出 ESC 3 3: MODAL IO输出 ESC 4
- `[Min, Max]`：`[0, 15]`
- 默认值：`0`
- 单位：``


40. PCA9685_DIS1 (INT32)
- 名称：PCA9685_DIS1 (INT32)
- 参数描述：PCA9685 Output Channel 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 1 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 1 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


41. PCA9685_DIS10 (INT32)
- 名称：PCA9685_DIS10 (INT32)
- 参数描述：PCA9685 Output Channel 10 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 10 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 10 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


42. PCA9685_DIS11 (INT32)
- 名称：PCA9685_DIS11 (INT32)
- 参数描述：PCA9685 Output Channel 11 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 11 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 11 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


43. PCA9685_DIS12 (INT32)
- 名称：PCA9685_DIS12 (INT32)
- 参数描述：PCA9685 Output Channel 12 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 12 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 12 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


44. PCA9685_DIS13 (INT32)
- 名称：PCA9685_DIS13 (INT32)
- 参数描述：PCA9685 Output Channel 13 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 13 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 13 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


45. PCA9685_DIS14 (INT32)
- 名称：PCA9685_DIS14 (INT32)
- 参数描述：PCA9685 Output Channel 14 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 14 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 14 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


46. PCA9685_DIS15 (INT32)
- 名称：PCA9685_DIS15 (INT32)
- 参数描述：PCA9685 Output Channel 15 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 15 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 15 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


47. PCA9685_DIS16 (INT32)
- 名称：PCA9685_DIS16 (INT32)
- 参数描述：PCA9685 Output Channel 16 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 16 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 16 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


48. PCA9685_DIS2 (INT32)
- 名称：PCA9685_DIS2 (INT32)
- 参数描述：PCA9685 Output Channel 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 2 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 2 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


49. PCA9685_DIS3 (INT32)
- 名称：PCA9685_DIS3 (INT32)
- 参数描述：PCA9685 Output Channel 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 3 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 3 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


50. PCA9685_DIS4 (INT32)
- 名称：PCA9685_DIS4 (INT32)
- 参数描述：PCA9685 Output Channel 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 4 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 4 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


51. PCA9685_DIS5 (INT32)
- 名称：PCA9685_DIS5 (INT32)
- 参数描述：PCA9685 Output Channel 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 5 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 5 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


52. PCA9685_DIS6 (INT32)
- 名称：PCA9685_DIS6 (INT32)
- 参数描述：PCA9685 Output Channel 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 6 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 6 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


53. PCA9685_DIS7 (INT32)
- 名称：PCA9685_DIS7 (INT32)
- 参数描述：PCA9685 Output Channel 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 7 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 7 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


54. PCA9685_DIS8 (INT32)
- 名称：PCA9685_DIS8 (INT32)
- 参数描述：PCA9685 Output Channel 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 8 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 8 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


55. PCA9685_DIS9 (INT32)
- 名称：PCA9685_DIS9 (INT32)
- 参数描述：PCA9685 Output Channel 9 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：PCA9685 输出通道 9 失效值 说明：这是在未解锁时设置的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
  - gpt注解：PCA9685 输出通道 9 失效值用于设置未解锁时的输出值。请注意，如果设置了 COM_PREARM_MODE，则非电机输出可能已在准备解锁状态下激活。
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


56. PCA9685_DUTY_EN (INT32)
- 名称：PCA9685_DUTY_EN (INT32)
- 参数描述：Put the selected channels into Duty-Cycle output mode Comment: The driver will output standard pulse-width encoded signal without this bit set. To make PCA9685 output in duty-cycle fashion, please enable the corresponding channel bit here and adjusting standard params to suit your need. The driver will have 12bits resolution for duty-cycle output. That means to achieve 0% to 100% output range on one channel, the corresponding params MIN and MAX for the channel should be set to 0 and 4096. Other standard params follows the same rule. Bitmask:0: Put CH1 to Duty-Cycle mode 1: Put CH2 to Duty-Cycle mode 2: Put CH3 to Duty-Cycle mode 3: Put CH4 to Duty-Cycle mode 4: Put CH5 to Duty-Cycle mode 5: Put CH6 to Duty-Cycle mode 6: Put CH7 to Duty-Cycle mode 7: Put CH8 to Duty-Cycle mode 8: Put CH9 to Duty-Cycle mode 9: Put CH10 to Duty-Cycle mode 10: Put CH11 to Duty-Cycle mode 11: Put CH12 to Duty-Cycle mode 12: Put CH13 to Duty-Cycle mode 13: Put CH14 to Duty-Cycle mode 14: Put CH15 to Duty-Cycle mode 15: Put CH16 to Duty-Cycle mode
  - 翻译：将选定的通道置于占空比输出模式 Comment: 如果没有设置此位，驱动程序将输出标准的脉宽编码信号。要使PCA9685以占空比方式输出，请在此处启用相应的通道位，并调整标准参数以满足您的需求。驱动程序将具有12位分辨率的占空比输出。这意味着要在一个通道上实现0%到100%的输出范围，该通道的相应参数 MIN 和 MAX 应设置为0和4096。其他标准参数遵循相同的规则。 Bitmask:0: 将 CH1 置于占空比模式 1: 将 CH2 置于占空比模式 2: 将 CH3 置于占空比模式 3: 将 CH4 置于占空比模式 4: 将 CH5 置于占空比模式 5: 将 CH6 置于占空比模式 6: 将 CH7 置于占空比模式 7: 将 CH8 置于占空比模式 8: 将 CH9 置于占空比模式 9: 将 CH10 置于占空比模式 10: 将 CH11 置于占空比模式 11: 将 CH12 置于占空比模式 12: 将 CH13 置于占空比模式 13: 将 CH14 置于占空比模式 14: 将 CH15 置于占空比模式 15: 将 CH16 置于占空比模式
  - gpt注解：PCA9685_DUTY_EN 参数用于将选定的通道切换到占空比输出模式。如果未设置此位，PCA9685驱动程序将输出标准的脉宽编码信号。要使PCA9685以占空比方式输出，请在此参数中启用相应通道位，并根据需要调整标准参数。驱动程序将以12位分辨率输出占空比信号。这意味着为了在一个通道上实现0%到100%的输出范围，该通道的 MIN 和 MAX 参数应分别设置为0和4096。其他标准参数遵循相同的规则。
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


57. PCA9685_FAIL1 (INT32)
- 名称：PCA9685_FAIL1 (INT32)
- 参数描述：PCA9685 Output Channel 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC1).
  - 翻译：PCA9685 输出通道 1 失控值 Comment: 这是在失控模式下设置的输出值。当设置为 -1（默认值）时，该值取决于功能（参见 PCA9685_FUNC1）。
  - gpt注解：PCA9685_FAIL1 参数用于设置失控模式下的输出值。当将其设置为 -1 时（默认值），该值将取决于 PCA9685_FUNC1 参数的设置。
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


58. PCA9685_FAIL10 (INT32)
- 名称：PCA9685_FAIL10 (INT32)
- 参数描述：PCA9685 Output Channel 10 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC10).
  - 翻译：PCA9685 输出通道 10 失控值 Comment: 这是在失控模式下设置的输出值。当设置为 -1（默认值）时，该值取决于功能（参见 PCA9685_FUNC10）。
  - gpt注解：PCA9685_FAIL10 参数用于设置失控模式下的输出值。当将其设置为 -1 时（默认值），该值将取决于 PCA9685_FUNC10 参数的设置。
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


59. PCA9685_FAIL11 (INT32)
- 名称：PCA9685_FAIL11 (INT32)
- 参数描述：PCA9685 Output Channel 11 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC11).
  - 翻译：PCA9685 输出通道 11 失控值 Comment: 这是在失控模式下设置的输出值。当设置为 -1（默认值）时，该值取决于功能（参见 PCA9685_FUNC11）。
  - gpt注解：PCA9685_FAIL11 参数用于设置失控模式下的输出值。当将其设置为 -1 时（默认值），该值将取决于 PCA9685_FUNC11 参数的设置。
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


60. PCA9685_FAIL12 (INT32)
- 名称：PCA9685_FAIL12 (INT32)
- 参数描述：PCA9685 Output Channel 12 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC12).
  - 翻译：PCA9685 输出通道 12 失控值 Comment: 这是在失控模式下设置的输出值。当设置为 -1（默认值）时，该值取决于功能（参见 PCA9685_FUNC12）。
  - gpt注解：PCA9685_FAIL12 参数用于设置失控模式下的输出值。当将其设置为 -1 时（默认值），该值将取决于 PCA9685_FUNC12 参数的设置。
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


61. PCA9685_FAIL13 (INT32)
- 名称：PCA9685_FAIL13 (INT32)
- 参数描述：PCA9685 Output Channel 13 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC13).
  - 翻译：PCA9685 输出通道 13 失控值 Comment: 这是在失控模式下设置的输出值。当设置为 -1（默认值）时，该值取决于功能（参见 PCA9685_FUNC13）。
  - gpt注解：PCA9685_FAIL13 参数用于设置失控模式下的输出值。当将其设置为 -1 时（默认值），该值将取决于 PCA9685_FUNC13 参数的设置。
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


62. PCA9685_FAIL14 (INT32)
- 名称：PCA9685_FAIL14 (INT32)
- 参数描述：PCA9685 Output Channel 14 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC14).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


63. PCA9685_FAIL15 (INT32)
- 名称：PCA9685_FAIL15 (INT32)
- 参数描述：PCA9685 Output Channel 15 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC15).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


64. PCA9685_FAIL16 (INT32)
- 名称：PCA9685_FAIL16 (INT32)
- 参数描述：PCA9685 Output Channel 16 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC16).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


65. PCA9685_FAIL2 (INT32)
- 名称：PCA9685_FAIL2 (INT32)
- 参数描述：PCA9685 Output Channel 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


66. PCA9685_FAIL3 (INT32)
- 名称：PCA9685_FAIL3 (INT32)
- 参数描述：PCA9685 Output Channel 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


67. PCA9685_FAIL4 (INT32)
- 名称：PCA9685_FAIL4 (INT32)
- 参数描述：PCA9685 Output Channel 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


68. PCA9685_FAIL5 (INT32)
- 名称：PCA9685_FAIL5 (INT32)
- 参数描述：PCA9685 Output Channel 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


69. PCA9685_FAIL6 (INT32)
- 名称：PCA9685_FAIL6 (INT32)
- 参数描述：PCA9685 Output Channel 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


70. PCA9685_FAIL7 (INT32)
- 名称：PCA9685_FAIL7 (INT32)
- 参数描述：PCA9685 Output Channel 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


71. PCA9685_FAIL8 (INT32)
- 名称：PCA9685_FAIL8 (INT32)
- 参数描述：PCA9685 Output Channel 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


72. PCA9685_FAIL9 (INT32)
- 名称：PCA9685_FAIL9 (INT32)
- 参数描述：PCA9685 Output Channel 9 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PCA9685_FUNC9).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


73. PCA9685_FUNC1 (INT32)
- 名称：PCA9685_FUNC1 (INT32)
- 参数描述：PCA9685 Output Channel 1 Output Function Comment: Select what should be output on PCA9685 Output Channel 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


74. PCA9685_FUNC10 (INT32)
- 名称：PCA9685_FUNC10 (INT32)
- 参数描述：PCA9685 Output Channel 10 Output Function Comment: Select what should be output on PCA9685 Output Channel 10. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


75. PCA9685_FUNC11 (INT32)
- 名称：PCA9685_FUNC11 (INT32)
- 参数描述：PCA9685 Output Channel 11 Output Function Comment: Select what should be output on PCA9685 Output Channel 11. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


76. PCA9685_FUNC12 (INT32)
- 名称：PCA9685_FUNC12 (INT32)
- 参数描述：PCA9685 Output Channel 12 Output Function Comment: Select what should be output on PCA9685 Output Channel 12. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


77. PCA9685_FUNC13 (INT32)
- 名称：PCA9685_FUNC13 (INT32)
- 参数描述：PCA9685 Output Channel 13 Output Function Comment: Select what should be output on PCA9685 Output Channel 13. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


78. PCA9685_FUNC14 (INT32)
- 名称：PCA9685_FUNC14 (INT32)
- 参数描述：PCA9685 Output Channel 14 Output Function Comment: Select what should be output on PCA9685 Output Channel 14. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


79. PCA9685_FUNC15 (INT32)
- 名称：PCA9685_FUNC15 (INT32)
- 参数描述：PCA9685 Output Channel 15 Output Function Comment: Select what should be output on PCA9685 Output Channel 15. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


80. PCA9685_FUNC16 (INT32)
- 名称：PCA9685_FUNC16 (INT32)
- 参数描述：PCA9685 Output Channel 16 Output Function Comment: Select what should be output on PCA9685 Output Channel 16. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


81. PCA9685_FUNC2 (INT32)
- 名称：PCA9685_FUNC2 (INT32)
- 参数描述：PCA9685 Output Channel 2 Output Function Comment: Select what should be output on PCA9685 Output Channel 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


82. PCA9685_FUNC3 (INT32)
- 名称：PCA9685_FUNC3 (INT32)
- 参数描述：PCA9685 Output Channel 3 Output Function Comment: Select what should be output on PCA9685 Output Channel 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


83. PCA9685_FUNC4 (INT32)
- 名称：PCA9685_FUNC4 (INT32)
- 参数描述：PCA9685 Output Channel 4 Output Function Comment: Select what should be output on PCA9685 Output Channel 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


84. PCA9685_FUNC5 (INT32)
- 名称：PCA9685_FUNC5 (INT32)
- 参数描述：PCA9685 Output Channel 5 Output Function Comment: Select what should be output on PCA9685 Output Channel 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


85. PCA9685_FUNC6 (INT32)
- 名称：PCA9685_FUNC6 (INT32)
- 参数描述：PCA9685 Output Channel 6 Output Function Comment: Select what should be output on PCA9685 Output Channel 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


86. PCA9685_FUNC7 (INT32)
- 名称：PCA9685_FUNC7 (INT32)
- 参数描述：PCA9685 Output Channel 7 Output Function Comment: Select what should be output on PCA9685 Output Channel 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


87. PCA9685_FUNC8 (INT32)
- 名称：PCA9685_FUNC8 (INT32)
- 参数描述：PCA9685 Output Channel 8 Output Function Comment: Select what should be output on PCA9685 Output Channel 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


88. PCA9685_FUNC9 (INT32)
- 名称：PCA9685_FUNC9 (INT32)
- 参数描述：PCA9685 Output Channel 9 Output Function Comment: Select what should be output on PCA9685 Output Channel 9. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


89. PCA9685_MAX1 (INT32)
- 名称：PCA9685_MAX1 (INT32)
- 参数描述：PCA9685 Output Channel 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


90. PCA9685_MAX10 (INT32)
- 名称：PCA9685_MAX10 (INT32)
- 参数描述：PCA9685 Output Channel 10 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


91. PCA9685_MAX11 (INT32)
- 名称：PCA9685_MAX11 (INT32)
- 参数描述：PCA9685 Output Channel 11 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


92. PCA9685_MAX12 (INT32)
- 名称：PCA9685_MAX12 (INT32)
- 参数描述：PCA9685 Output Channel 12 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


93. PCA9685_MAX13 (INT32)
- 名称：PCA9685_MAX13 (INT32)
- 参数描述：PCA9685 Output Channel 13 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


94. PCA9685_MAX14 (INT32)
- 名称：PCA9685_MAX14 (INT32)
- 参数描述：PCA9685 Output Channel 14 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


95. PCA9685_MAX15 (INT32)
- 名称：PCA9685_MAX15 (INT32)
- 参数描述：PCA9685 Output Channel 15 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


96. PCA9685_MAX16 (INT32)
- 名称：PCA9685_MAX16 (INT32)
- 参数描述：PCA9685 Output Channel 16 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


97. PCA9685_MAX2 (INT32)
- 名称：PCA9685_MAX2 (INT32)
- 参数描述：PCA9685 Output Channel 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


98. PCA9685_MAX3 (INT32)
- 名称：PCA9685_MAX3 (INT32)
- 参数描述：PCA9685 Output Channel 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


99. PCA9685_MAX4 (INT32)
- 名称：PCA9685_MAX4 (INT32)
- 参数描述：PCA9685 Output Channel 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


100. PCA9685_MAX5 (INT32)
- 名称：PCA9685_MAX5 (INT32)
- 参数描述：PCA9685 Output Channel 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


101. PCA9685_MAX6 (INT32)
- 名称：PCA9685_MAX6 (INT32)
- 参数描述：PCA9685 Output Channel 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


102. PCA9685_MAX7 (INT32)
- 名称：PCA9685_MAX7 (INT32)
- 参数描述：PCA9685 Output Channel 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


103. PCA9685_MAX8 (INT32)
- 名称：PCA9685_MAX8 (INT32)
- 参数描述：PCA9685 Output Channel 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


104. PCA9685_MAX9 (INT32)
- 名称：PCA9685_MAX9 (INT32)
- 参数描述：PCA9685 Output Channel 9 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`1900`
- 单位：``


105. PCA9685_MIN1 (INT32)
- 名称：PCA9685_MIN1 (INT32)
- 参数描述：PCA9685 Output Channel 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


106. PCA9685_MIN10 (INT32)
- 名称：PCA9685_MIN10 (INT32)
- 参数描述：PCA9685 Output Channel 10 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


107. PCA9685_MIN11 (INT32)
- 名称：PCA9685_MIN11 (INT32)
- 参数描述：PCA9685 Output Channel 11 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


108. PCA9685_MIN12 (INT32)
- 名称：PCA9685_MIN12 (INT32)
- 参数描述：PCA9685 Output Channel 12 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


109. PCA9685_MIN13 (INT32)
- 名称：PCA9685_MIN13 (INT32)
- 参数描述：PCA9685 Output Channel 13 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


110. PCA9685_MIN14 (INT32)
- 名称：PCA9685_MIN14 (INT32)
- 参数描述：PCA9685 Output Channel 14 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


111. PCA9685_MIN15 (INT32)
- 名称：PCA9685_MIN15 (INT32)
- 参数描述：PCA9685 Output Channel 15 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


112. PCA9685_MIN16 (INT32)
- 名称：PCA9685_MIN16 (INT32)
- 参数描述：PCA9685 Output Channel 16 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


113. PCA9685_MIN2 (INT32)
- 名称：PCA9685_MIN2 (INT32)
- 参数描述：PCA9685 Output Channel 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


114. PCA9685_MIN3 (INT32)
- 名称：PCA9685_MIN3 (INT32)
- 参数描述：PCA9685 Output Channel 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


115. PCA9685_MIN4 (INT32)
- 名称：PCA9685_MIN4 (INT32)
- 参数描述：PCA9685 Output Channel 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


116. PCA9685_MIN5 (INT32)
- 名称：PCA9685_MIN5 (INT32)
- 参数描述：PCA9685 Output Channel 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


117. PCA9685_MIN6 (INT32)
- 名称：PCA9685_MIN6 (INT32)
- 参数描述：PCA9685 Output Channel 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


118. PCA9685_MIN7 (INT32)
- 名称：PCA9685_MIN7 (INT32)
- 参数描述：PCA9685 Output Channel 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


119. PCA9685_MIN8 (INT32)
- 名称：PCA9685_MIN8 (INT32)
- 参数描述：PCA9685 Output Channel 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


120. PCA9685_MIN9 (INT32)
- 名称：PCA9685_MIN9 (INT32)
- 参数描述：PCA9685 Output Channel 9 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1100`
- 单位：``


121. PCA9685_PWM_FREQ (FLOAT)
- 名称：PCA9685_PWM_FREQ (FLOAT)
- 参数描述：PWM cycle frequency Comment: Controls the PWM frequency at timing perspective. This is independent from PWM update frequency, as PCA9685 is capable to output without being continuously commanded by FC. Higher frequency leads to more accurate pulse width, but some ESCs and servos may not support it. This parameter should be set to the same value as PWM update rate in most case. This parameter MUST NOT exceed upper limit of 400.0, if any outputs as generic 1000~2000us pulse width is desired. Frequency higher than 400 only makes sense in duty-cycle mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[23.8, 1525.87]`
- 默认值：`50.0`
- 单位：``


122. PCA9685_REV (INT32)
- 名称：PCA9685_REV (INT32)
- 参数描述：Reverse Output Range for PCA9685 Output Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: PCA9685 Output Channel 1 1: PCA9685 Output Channel 2 2: PCA9685 Output Channel 3 3: PCA9685 Output Channel 4 4: PCA9685 Output Channel 5 5: PCA9685 Output Channel 6 6: PCA9685 Output Channel 7 7: PCA9685 Output Channel 8 8: PCA9685 Output Channel 9 9: PCA9685 Output Channel 10 10: PCA9685 Output Channel 11 11: PCA9685 Output Channel 12 12: PCA9685 Output Channel 13 13: PCA9685 Output Channel 14 14: PCA9685 Output Channel 15 15: PCA9685 Output Channel 16
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


123. PCA9685_SCHD_HZ (FLOAT)
- 名称：PCA9685_SCHD_HZ (FLOAT)
- 参数描述：PWM update rate Comment: Controls the update rate of PWM output. Flight Controller will inform those numbers of update events in a second, to PCA9685. Higher update rate will consume more I2C bandwidth, which may even lead to worse output latency, or completely block I2C bus.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[50.0, 400.0]`
- 默认值：`50.0`
- 单位：``


124. PWM_AUX_DIS1 (INT32)
- 名称：PWM_AUX_DIS1 (INT32)
- 参数描述：PWM Aux 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


125. PWM_AUX_DIS10 (INT32)
- 名称：PWM_AUX_DIS10 (INT32)
- 参数描述：PWM Capture 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


126. PWM_AUX_DIS11 (INT32)
- 名称：PWM_AUX_DIS11 (INT32)
- 参数描述：PWM Capture 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


127. PWM_AUX_DIS2 (INT32)
- 名称：PWM_AUX_DIS2 (INT32)
- 参数描述：PWM Aux 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


128. PWM_AUX_DIS3 (INT32)
- 名称：PWM_AUX_DIS3 (INT32)
- 参数描述：PWM Aux 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


129. PWM_AUX_DIS4 (INT32)
- 名称：PWM_AUX_DIS4 (INT32)
- 参数描述：PWM Aux 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


130. PWM_AUX_DIS5 (INT32)
- 名称：PWM_AUX_DIS5 (INT32)
- 参数描述：PWM Aux 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


131. PWM_AUX_DIS6 (INT32)
- 名称：PWM_AUX_DIS6 (INT32)
- 参数描述：PWM Aux 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


132. PWM_AUX_DIS7 (INT32)
- 名称：PWM_AUX_DIS7 (INT32)
- 参数描述：PWM Aux 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


133. PWM_AUX_DIS8 (INT32)
- 名称：PWM_AUX_DIS8 (INT32)
- 参数描述：PWM Aux 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


134. PWM_AUX_DIS9 (INT32)
- 名称：PWM_AUX_DIS9 (INT32)
- 参数描述：PWM Capture 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


135. PWM_AUX_FAIL1 (INT32)
- 名称：PWM_AUX_FAIL1 (INT32)
- 参数描述：PWM Aux 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


136. PWM_AUX_FAIL10 (INT32)
- 名称：PWM_AUX_FAIL10 (INT32)
- 参数描述：PWM Capture 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


137. PWM_AUX_FAIL11 (INT32)
- 名称：PWM_AUX_FAIL11 (INT32)
- 参数描述：PWM Capture 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


138. PWM_AUX_FAIL2 (INT32)
- 名称：PWM_AUX_FAIL2 (INT32)
- 参数描述：PWM Aux 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


139. PWM_AUX_FAIL3 (INT32)
- 名称：PWM_AUX_FAIL3 (INT32)
- 参数描述：PWM Aux 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


140. PWM_AUX_FAIL4 (INT32)
- 名称：PWM_AUX_FAIL4 (INT32)
- 参数描述：PWM Aux 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


141. PWM_AUX_FAIL5 (INT32)
- 名称：PWM_AUX_FAIL5 (INT32)
- 参数描述：PWM Aux 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


142. PWM_AUX_FAIL6 (INT32)
- 名称：PWM_AUX_FAIL6 (INT32)
- 参数描述：PWM Aux 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


143. PWM_AUX_FAIL7 (INT32)
- 名称：PWM_AUX_FAIL7 (INT32)
- 参数描述：PWM Aux 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


144. PWM_AUX_FAIL8 (INT32)
- 名称：PWM_AUX_FAIL8 (INT32)
- 参数描述：PWM Aux 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


145. PWM_AUX_FAIL9 (INT32)
- 名称：PWM_AUX_FAIL9 (INT32)
- 参数描述：PWM Capture 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_AUX_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


146. PWM_AUX_FUNC1 (INT32)
- 名称：PWM_AUX_FUNC1 (INT32)
- 参数描述：PWM Aux 1 Output Function Comment: Select what should be output on PWM Aux 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


147. PWM_AUX_FUNC10 (INT32)
- 名称：PWM_AUX_FUNC10 (INT32)
- 参数描述：PWM Capture 2 Output Function Comment: Select what should be output on PWM Capture 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


148. PWM_AUX_FUNC11 (INT32)
- 名称：PWM_AUX_FUNC11 (INT32)
- 参数描述：PWM Capture 3 Output Function Comment: Select what should be output on PWM Capture 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


149. PWM_AUX_FUNC2 (INT32)
- 名称：PWM_AUX_FUNC2 (INT32)
- 参数描述：PWM Aux 2 Output Function Comment: Select what should be output on PWM Aux 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


150. PWM_AUX_FUNC3 (INT32)
- 名称：PWM_AUX_FUNC3 (INT32)
- 参数描述：PWM Aux 3 Output Function Comment: Select what should be output on PWM Aux 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


151. PWM_AUX_FUNC4 (INT32)
- 名称：PWM_AUX_FUNC4 (INT32)
- 参数描述：PWM Aux 4 Output Function Comment: Select what should be output on PWM Aux 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


152. PWM_AUX_FUNC5 (INT32)
- 名称：PWM_AUX_FUNC5 (INT32)
- 参数描述：PWM Aux 5 Output Function Comment: Select what should be output on PWM Aux 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


153. PWM_AUX_FUNC6 (INT32)
- 名称：PWM_AUX_FUNC6 (INT32)
- 参数描述：PWM Aux 6 Output Function Comment: Select what should be output on PWM Aux 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


154. PWM_AUX_FUNC7 (INT32)
- 名称：PWM_AUX_FUNC7 (INT32)
- 参数描述：PWM Aux 7 Output Function Comment: Select what should be output on PWM Aux 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


155. PWM_AUX_FUNC8 (INT32)
- 名称：PWM_AUX_FUNC8 (INT32)
- 参数描述：PWM Aux 8 Output Function Comment: Select what should be output on PWM Aux 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


156. PWM_AUX_FUNC9 (INT32)
- 名称：PWM_AUX_FUNC9 (INT32)
- 参数描述：PWM Capture 1 Output Function Comment: Select what should be output on PWM Capture 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel 2000: Camera Trigger 2032: Camera Capture 2064: PPS Input
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


157. PWM_AUX_MAX1 (INT32)
- 名称：PWM_AUX_MAX1 (INT32)
- 参数描述：PWM Aux 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


158. PWM_AUX_MAX10 (INT32)
- 名称：PWM_AUX_MAX10 (INT32)
- 参数描述：PWM Capture 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


159. PWM_AUX_MAX11 (INT32)
- 名称：PWM_AUX_MAX11 (INT32)
- 参数描述：PWM Capture 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


160. PWM_AUX_MAX2 (INT32)
- 名称：PWM_AUX_MAX2 (INT32)
- 参数描述：PWM Aux 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


161. PWM_AUX_MAX3 (INT32)
- 名称：PWM_AUX_MAX3 (INT32)
- 参数描述：PWM Aux 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


162. PWM_AUX_MAX4 (INT32)
- 名称：PWM_AUX_MAX4 (INT32)
- 参数描述：PWM Aux 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


163. PWM_AUX_MAX5 (INT32)
- 名称：PWM_AUX_MAX5 (INT32)
- 参数描述：PWM Aux 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


164. PWM_AUX_MAX6 (INT32)
- 名称：PWM_AUX_MAX6 (INT32)
- 参数描述：PWM Aux 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


165. PWM_AUX_MAX7 (INT32)
- 名称：PWM_AUX_MAX7 (INT32)
- 参数描述：PWM Aux 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


166. PWM_AUX_MAX8 (INT32)
- 名称：PWM_AUX_MAX8 (INT32)
- 参数描述：PWM Aux 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


167. PWM_AUX_MAX9 (INT32)
- 名称：PWM_AUX_MAX9 (INT32)
- 参数描述：PWM Capture 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


168. PWM_AUX_MIN1 (INT32)
- 名称：PWM_AUX_MIN1 (INT32)
- 参数描述：PWM Aux 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


169. PWM_AUX_MIN10 (INT32)
- 名称：PWM_AUX_MIN10 (INT32)
- 参数描述：PWM Capture 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


170. PWM_AUX_MIN11 (INT32)
- 名称：PWM_AUX_MIN11 (INT32)
- 参数描述：PWM Capture 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


171. PWM_AUX_MIN2 (INT32)
- 名称：PWM_AUX_MIN2 (INT32)
- 参数描述：PWM Aux 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


172. PWM_AUX_MIN3 (INT32)
- 名称：PWM_AUX_MIN3 (INT32)
- 参数描述：PWM Aux 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


173. PWM_AUX_MIN4 (INT32)
- 名称：PWM_AUX_MIN4 (INT32)
- 参数描述：PWM Aux 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


174. PWM_AUX_MIN5 (INT32)
- 名称：PWM_AUX_MIN5 (INT32)
- 参数描述：PWM Aux 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


175. PWM_AUX_MIN6 (INT32)
- 名称：PWM_AUX_MIN6 (INT32)
- 参数描述：PWM Aux 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


176. PWM_AUX_MIN7 (INT32)
- 名称：PWM_AUX_MIN7 (INT32)
- 参数描述：PWM Aux 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


177. PWM_AUX_MIN8 (INT32)
- 名称：PWM_AUX_MIN8 (INT32)
- 参数描述：PWM Aux 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


178. PWM_AUX_MIN9 (INT32)
- 名称：PWM_AUX_MIN9 (INT32)
- 参数描述：PWM Capture 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


179. PWM_AUX_REV (INT32)
- 名称：PWM_AUX_REV (INT32)
- 参数描述：Reverse Output Range for PWM AUX Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: PWM Aux 1 1: PWM Aux 2 2: PWM Aux 3 3: PWM Aux 4 4: PWM Aux 5 5: PWM Aux 6 6: PWM Aux 7 7: PWM Aux 8 8: PWM Capture 1 9: PWM Capture 2 10: PWM Capture 3
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2047]`
- 默认值：`0`
- 单位：``


180. PWM_AUX_TIM0 (INT32)
- 名称：PWM_AUX_TIM0 (INT32)
- 参数描述：Output Protocol Configuration for PWM Aux 1-4 Comment: Select which Output Protocol to use for outputs PWM Aux 1-4. Custom PWM rates can be used by directly setting any value >0. 参数对照:-5: DShot150 -4: DShot300 -3: DShot600 -2: DShot1200 -1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


181. PWM_AUX_TIM1 (INT32)
- 名称：PWM_AUX_TIM1 (INT32)
- 参数描述：Output Protocol Configuration for PWM Aux 5-6 Comment: Select which Output Protocol to use for outputs PWM Aux 5-6. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


182. PWM_AUX_TIM2 (INT32)
- 名称：PWM_AUX_TIM2 (INT32)
- 参数描述：Output Protocol Configuration for PWM Aux 7-8 Comment: Select which Output Protocol to use for outputs PWM Aux 7-8. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


183. PWM_AUX_TIM3 (INT32)
- 名称：PWM_AUX_TIM3 (INT32)
- 参数描述：Output Protocol Configuration for PWM Capture 1-3 Comment: Select which Output Protocol to use for outputs PWM Capture 1-3. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


184. PWM_MAIN_DIS1 (INT32)
- 名称：PWM_MAIN_DIS1 (INT32)
- 参数描述：MAIN 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


185. PWM_MAIN_DIS2 (INT32)
- 名称：PWM_MAIN_DIS2 (INT32)
- 参数描述：MAIN 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


186. PWM_MAIN_DIS3 (INT32)
- 名称：PWM_MAIN_DIS3 (INT32)
- 参数描述：MAIN 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


187. PWM_MAIN_DIS4 (INT32)
- 名称：PWM_MAIN_DIS4 (INT32)
- 参数描述：MAIN 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


188. PWM_MAIN_DIS5 (INT32)
- 名称：PWM_MAIN_DIS5 (INT32)
- 参数描述：MAIN 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


189. PWM_MAIN_DIS6 (INT32)
- 名称：PWM_MAIN_DIS6 (INT32)
- 参数描述：MAIN 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


190. PWM_MAIN_DIS7 (INT32)
- 名称：PWM_MAIN_DIS7 (INT32)
- 参数描述：MAIN 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


191. PWM_MAIN_DIS8 (INT32)
- 名称：PWM_MAIN_DIS8 (INT32)
- 参数描述：MAIN 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 2200]`
- 默认值：`1000`
- 单位：``


192. PWM_MAIN_FAIL1 (INT32)
- 名称：PWM_MAIN_FAIL1 (INT32)
- 参数描述：MAIN 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


193. PWM_MAIN_FAIL2 (INT32)
- 名称：PWM_MAIN_FAIL2 (INT32)
- 参数描述：MAIN 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


194. PWM_MAIN_FAIL3 (INT32)
- 名称：PWM_MAIN_FAIL3 (INT32)
- 参数描述：MAIN 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


195. PWM_MAIN_FAIL4 (INT32)
- 名称：PWM_MAIN_FAIL4 (INT32)
- 参数描述：MAIN 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


196. PWM_MAIN_FAIL5 (INT32)
- 名称：PWM_MAIN_FAIL5 (INT32)
- 参数描述：MAIN 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


197. PWM_MAIN_FAIL6 (INT32)
- 名称：PWM_MAIN_FAIL6 (INT32)
- 参数描述：MAIN 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


198. PWM_MAIN_FAIL7 (INT32)
- 名称：PWM_MAIN_FAIL7 (INT32)
- 参数描述：MAIN 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


199. PWM_MAIN_FAIL8 (INT32)
- 名称：PWM_MAIN_FAIL8 (INT32)
- 参数描述：MAIN 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see PWM_MAIN_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 2200]`
- 默认值：`-1`
- 单位：``


200. PWM_MAIN_FUNC1 (INT32)
- 名称：PWM_MAIN_FUNC1 (INT32)
- 参数描述：MAIN 1 Output Function Comment: Select what should be output on MAIN 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


201. PWM_MAIN_FUNC2 (INT32)
- 名称：PWM_MAIN_FUNC2 (INT32)
- 参数描述：MAIN 2 Output Function Comment: Select what should be output on MAIN 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


202. PWM_MAIN_FUNC3 (INT32)
- 名称：PWM_MAIN_FUNC3 (INT32)
- 参数描述：MAIN 3 Output Function Comment: Select what should be output on MAIN 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


203. PWM_MAIN_FUNC4 (INT32)
- 名称：PWM_MAIN_FUNC4 (INT32)
- 参数描述：MAIN 4 Output Function Comment: Select what should be output on MAIN 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


204. PWM_MAIN_FUNC5 (INT32)
- 名称：PWM_MAIN_FUNC5 (INT32)
- 参数描述：MAIN 5 Output Function Comment: Select what should be output on MAIN 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


205. PWM_MAIN_FUNC6 (INT32)
- 名称：PWM_MAIN_FUNC6 (INT32)
- 参数描述：MAIN 6 Output Function Comment: Select what should be output on MAIN 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


206. PWM_MAIN_FUNC7 (INT32)
- 名称：PWM_MAIN_FUNC7 (INT32)
- 参数描述：MAIN 7 Output Function Comment: Select what should be output on MAIN 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


207. PWM_MAIN_FUNC8 (INT32)
- 名称：PWM_MAIN_FUNC8 (INT32)
- 参数描述：MAIN 8 Output Function Comment: Select what should be output on MAIN 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


208. PWM_MAIN_MAX1 (INT32)
- 名称：PWM_MAIN_MAX1 (INT32)
- 参数描述：MAIN 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


209. PWM_MAIN_MAX2 (INT32)
- 名称：PWM_MAIN_MAX2 (INT32)
- 参数描述：MAIN 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


210. PWM_MAIN_MAX3 (INT32)
- 名称：PWM_MAIN_MAX3 (INT32)
- 参数描述：MAIN 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


211. PWM_MAIN_MAX4 (INT32)
- 名称：PWM_MAIN_MAX4 (INT32)
- 参数描述：MAIN 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


212. PWM_MAIN_MAX5 (INT32)
- 名称：PWM_MAIN_MAX5 (INT32)
- 参数描述：MAIN 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


213. PWM_MAIN_MAX6 (INT32)
- 名称：PWM_MAIN_MAX6 (INT32)
- 参数描述：MAIN 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


214. PWM_MAIN_MAX7 (INT32)
- 名称：PWM_MAIN_MAX7 (INT32)
- 参数描述：MAIN 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


215. PWM_MAIN_MAX8 (INT32)
- 名称：PWM_MAIN_MAX8 (INT32)
- 参数描述：MAIN 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1600, 2200]`
- 默认值：`2000`
- 单位：``


216. PWM_MAIN_MIN1 (INT32)
- 名称：PWM_MAIN_MIN1 (INT32)
- 参数描述：MAIN 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


217. PWM_MAIN_MIN2 (INT32)
- 名称：PWM_MAIN_MIN2 (INT32)
- 参数描述：MAIN 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


218. PWM_MAIN_MIN3 (INT32)
- 名称：PWM_MAIN_MIN3 (INT32)
- 参数描述：MAIN 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


219. PWM_MAIN_MIN4 (INT32)
- 名称：PWM_MAIN_MIN4 (INT32)
- 参数描述：MAIN 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


220. PWM_MAIN_MIN5 (INT32)
- 名称：PWM_MAIN_MIN5 (INT32)
- 参数描述：MAIN 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


221. PWM_MAIN_MIN6 (INT32)
- 名称：PWM_MAIN_MIN6 (INT32)
- 参数描述：MAIN 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


222. PWM_MAIN_MIN7 (INT32)
- 名称：PWM_MAIN_MIN7 (INT32)
- 参数描述：MAIN 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


223. PWM_MAIN_MIN8 (INT32)
- 名称：PWM_MAIN_MIN8 (INT32)
- 参数描述：MAIN 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800, 1400]`
- 默认值：`1000`
- 单位：``


224. PWM_MAIN_REV (INT32)
- 名称：PWM_MAIN_REV (INT32)
- 参数描述：Reverse Output Range for PWM MAIN Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: MAIN 1 1: MAIN 2 2: MAIN 3 3: MAIN 4 4: MAIN 5 5: MAIN 6 6: MAIN 7 7: MAIN 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


225. PWM_MAIN_TIM0 (INT32)
- 名称：PWM_MAIN_TIM0 (INT32)
- 参数描述：Output Protocol Configuration for MAIN 1-2 Comment: Select which Output Protocol to use for outputs MAIN 1-2. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


226. PWM_MAIN_TIM1 (INT32)
- 名称：PWM_MAIN_TIM1 (INT32)
- 参数描述：Output Protocol Configuration for MAIN 3-4 Comment: Select which Output Protocol to use for outputs MAIN 3-4. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


227. PWM_MAIN_TIM2 (INT32)
- 名称：PWM_MAIN_TIM2 (INT32)
- 参数描述：Output Protocol Configuration for MAIN 5-8 Comment: Select which Output Protocol to use for outputs MAIN 5-8. Custom PWM rates can be used by directly setting any value >0. 参数对照:-1: OneShot 50: PWM 50 Hz 100: PWM 100 Hz 200: PWM 200 Hz 400: PWM 400 Hz Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`400`
- 单位：``


228. SIM_GZ_EC_DIS1 (INT32)
- 名称：SIM_GZ_EC_DIS1 (INT32)
- 参数描述：SIM_GZ ESC 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


229. SIM_GZ_EC_DIS2 (INT32)
- 名称：SIM_GZ_EC_DIS2 (INT32)
- 参数描述：SIM_GZ ESC 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


230. SIM_GZ_EC_DIS3 (INT32)
- 名称：SIM_GZ_EC_DIS3 (INT32)
- 参数描述：SIM_GZ ESC 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


231. SIM_GZ_EC_DIS4 (INT32)
- 名称：SIM_GZ_EC_DIS4 (INT32)
- 参数描述：SIM_GZ ESC 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


232. SIM_GZ_EC_DIS5 (INT32)
- 名称：SIM_GZ_EC_DIS5 (INT32)
- 参数描述：SIM_GZ ESC 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


233. SIM_GZ_EC_DIS6 (INT32)
- 名称：SIM_GZ_EC_DIS6 (INT32)
- 参数描述：SIM_GZ ESC 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


234. SIM_GZ_EC_DIS7 (INT32)
- 名称：SIM_GZ_EC_DIS7 (INT32)
- 参数描述：SIM_GZ ESC 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


235. SIM_GZ_EC_DIS8 (INT32)
- 名称：SIM_GZ_EC_DIS8 (INT32)
- 参数描述：SIM_GZ ESC 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


236. SIM_GZ_EC_FAIL1 (INT32)
- 名称：SIM_GZ_EC_FAIL1 (INT32)
- 参数描述：SIM_GZ ESC 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


237. SIM_GZ_EC_FAIL2 (INT32)
- 名称：SIM_GZ_EC_FAIL2 (INT32)
- 参数描述：SIM_GZ ESC 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


238. SIM_GZ_EC_FAIL3 (INT32)
- 名称：SIM_GZ_EC_FAIL3 (INT32)
- 参数描述：SIM_GZ ESC 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


239. SIM_GZ_EC_FAIL4 (INT32)
- 名称：SIM_GZ_EC_FAIL4 (INT32)
- 参数描述：SIM_GZ ESC 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


240. SIM_GZ_EC_FAIL5 (INT32)
- 名称：SIM_GZ_EC_FAIL5 (INT32)
- 参数描述：SIM_GZ ESC 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


241. SIM_GZ_EC_FAIL6 (INT32)
- 名称：SIM_GZ_EC_FAIL6 (INT32)
- 参数描述：SIM_GZ ESC 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


242. SIM_GZ_EC_FAIL7 (INT32)
- 名称：SIM_GZ_EC_FAIL7 (INT32)
- 参数描述：SIM_GZ ESC 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


243. SIM_GZ_EC_FAIL8 (INT32)
- 名称：SIM_GZ_EC_FAIL8 (INT32)
- 参数描述：SIM_GZ ESC 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_EC_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


244. SIM_GZ_EC_FUNC1 (INT32)
- 名称：SIM_GZ_EC_FUNC1 (INT32)
- 参数描述：SIM_GZ ESC 1 Output Function Comment: Select what should be output on SIM_GZ ESC 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


245. SIM_GZ_EC_FUNC2 (INT32)
- 名称：SIM_GZ_EC_FUNC2 (INT32)
- 参数描述：SIM_GZ ESC 2 Output Function Comment: Select what should be output on SIM_GZ ESC 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


246. SIM_GZ_EC_FUNC3 (INT32)
- 名称：SIM_GZ_EC_FUNC3 (INT32)
- 参数描述：SIM_GZ ESC 3 Output Function Comment: Select what should be output on SIM_GZ ESC 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


247. SIM_GZ_EC_FUNC4 (INT32)
- 名称：SIM_GZ_EC_FUNC4 (INT32)
- 参数描述：SIM_GZ ESC 4 Output Function Comment: Select what should be output on SIM_GZ ESC 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


248. SIM_GZ_EC_FUNC5 (INT32)
- 名称：SIM_GZ_EC_FUNC5 (INT32)
- 参数描述：SIM_GZ ESC 5 Output Function Comment: Select what should be output on SIM_GZ ESC 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


249. SIM_GZ_EC_FUNC6 (INT32)
- 名称：SIM_GZ_EC_FUNC6 (INT32)
- 参数描述：SIM_GZ ESC 6 Output Function Comment: Select what should be output on SIM_GZ ESC 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


250. SIM_GZ_EC_FUNC7 (INT32)
- 名称：SIM_GZ_EC_FUNC7 (INT32)
- 参数描述：SIM_GZ ESC 7 Output Function Comment: Select what should be output on SIM_GZ ESC 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


251. SIM_GZ_EC_FUNC8 (INT32)
- 名称：SIM_GZ_EC_FUNC8 (INT32)
- 参数描述：SIM_GZ ESC 8 Output Function Comment: Select what should be output on SIM_GZ ESC 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


252. SIM_GZ_EC_MAX1 (INT32)
- 名称：SIM_GZ_EC_MAX1 (INT32)
- 参数描述：SIM_GZ ESC 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


253. SIM_GZ_EC_MAX2 (INT32)
- 名称：SIM_GZ_EC_MAX2 (INT32)
- 参数描述：SIM_GZ ESC 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


254. SIM_GZ_EC_MAX3 (INT32)
- 名称：SIM_GZ_EC_MAX3 (INT32)
- 参数描述：SIM_GZ ESC 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


255. SIM_GZ_EC_MAX4 (INT32)
- 名称：SIM_GZ_EC_MAX4 (INT32)
- 参数描述：SIM_GZ ESC 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


256. SIM_GZ_EC_MAX5 (INT32)
- 名称：SIM_GZ_EC_MAX5 (INT32)
- 参数描述：SIM_GZ ESC 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


257. SIM_GZ_EC_MAX6 (INT32)
- 名称：SIM_GZ_EC_MAX6 (INT32)
- 参数描述：SIM_GZ ESC 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


258. SIM_GZ_EC_MAX7 (INT32)
- 名称：SIM_GZ_EC_MAX7 (INT32)
- 参数描述：SIM_GZ ESC 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


259. SIM_GZ_EC_MAX8 (INT32)
- 名称：SIM_GZ_EC_MAX8 (INT32)
- 参数描述：SIM_GZ ESC 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


260. SIM_GZ_EC_MIN1 (INT32)
- 名称：SIM_GZ_EC_MIN1 (INT32)
- 参数描述：SIM_GZ ESC 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


261. SIM_GZ_EC_MIN2 (INT32)
- 名称：SIM_GZ_EC_MIN2 (INT32)
- 参数描述：SIM_GZ ESC 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


262. SIM_GZ_EC_MIN3 (INT32)
- 名称：SIM_GZ_EC_MIN3 (INT32)
- 参数描述：SIM_GZ ESC 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


263. SIM_GZ_EC_MIN4 (INT32)
- 名称：SIM_GZ_EC_MIN4 (INT32)
- 参数描述：SIM_GZ ESC 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


264. SIM_GZ_EC_MIN5 (INT32)
- 名称：SIM_GZ_EC_MIN5 (INT32)
- 参数描述：SIM_GZ ESC 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


265. SIM_GZ_EC_MIN6 (INT32)
- 名称：SIM_GZ_EC_MIN6 (INT32)
- 参数描述：SIM_GZ ESC 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


266. SIM_GZ_EC_MIN7 (INT32)
- 名称：SIM_GZ_EC_MIN7 (INT32)
- 参数描述：SIM_GZ ESC 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


267. SIM_GZ_EC_MIN8 (INT32)
- 名称：SIM_GZ_EC_MIN8 (INT32)
- 参数描述：SIM_GZ ESC 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


268. SIM_GZ_EC_REV (INT32)
- 名称：SIM_GZ_EC_REV (INT32)
- 参数描述：Reverse Output Range for SIM_GZ Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: SIM_GZ ESC 1 1: SIM_GZ ESC 2 2: SIM_GZ ESC 3 3: SIM_GZ ESC 4 4: SIM_GZ ESC 5 5: SIM_GZ ESC 6 6: SIM_GZ ESC 7 7: SIM_GZ ESC 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


269. SIM_GZ_SV_DIS1 (INT32)
- 名称：SIM_GZ_SV_DIS1 (INT32)
- 参数描述：SIM_GZ Servo 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


270. SIM_GZ_SV_DIS2 (INT32)
- 名称：SIM_GZ_SV_DIS2 (INT32)
- 参数描述：SIM_GZ Servo 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


271. SIM_GZ_SV_DIS3 (INT32)
- 名称：SIM_GZ_SV_DIS3 (INT32)
- 参数描述：SIM_GZ Servo 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


272. SIM_GZ_SV_DIS4 (INT32)
- 名称：SIM_GZ_SV_DIS4 (INT32)
- 参数描述：SIM_GZ Servo 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


273. SIM_GZ_SV_DIS5 (INT32)
- 名称：SIM_GZ_SV_DIS5 (INT32)
- 参数描述：SIM_GZ Servo 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


274. SIM_GZ_SV_DIS6 (INT32)
- 名称：SIM_GZ_SV_DIS6 (INT32)
- 参数描述：SIM_GZ Servo 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


275. SIM_GZ_SV_DIS7 (INT32)
- 名称：SIM_GZ_SV_DIS7 (INT32)
- 参数描述：SIM_GZ Servo 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


276. SIM_GZ_SV_DIS8 (INT32)
- 名称：SIM_GZ_SV_DIS8 (INT32)
- 参数描述：SIM_GZ Servo 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


277. SIM_GZ_SV_FAIL1 (INT32)
- 名称：SIM_GZ_SV_FAIL1 (INT32)
- 参数描述：SIM_GZ Servo 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


278. SIM_GZ_SV_FAIL2 (INT32)
- 名称：SIM_GZ_SV_FAIL2 (INT32)
- 参数描述：SIM_GZ Servo 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


279. SIM_GZ_SV_FAIL3 (INT32)
- 名称：SIM_GZ_SV_FAIL3 (INT32)
- 参数描述：SIM_GZ Servo 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


280. SIM_GZ_SV_FAIL4 (INT32)
- 名称：SIM_GZ_SV_FAIL4 (INT32)
- 参数描述：SIM_GZ Servo 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


281. SIM_GZ_SV_FAIL5 (INT32)
- 名称：SIM_GZ_SV_FAIL5 (INT32)
- 参数描述：SIM_GZ Servo 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


282. SIM_GZ_SV_FAIL6 (INT32)
- 名称：SIM_GZ_SV_FAIL6 (INT32)
- 参数描述：SIM_GZ Servo 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


283. SIM_GZ_SV_FAIL7 (INT32)
- 名称：SIM_GZ_SV_FAIL7 (INT32)
- 参数描述：SIM_GZ Servo 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


284. SIM_GZ_SV_FAIL8 (INT32)
- 名称：SIM_GZ_SV_FAIL8 (INT32)
- 参数描述：SIM_GZ Servo 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see SIM_GZ_SV_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


285. SIM_GZ_SV_FUNC1 (INT32)
- 名称：SIM_GZ_SV_FUNC1 (INT32)
- 参数描述：SIM_GZ Servo 1 Output Function Comment: Select what should be output on SIM_GZ Servo 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


286. SIM_GZ_SV_FUNC2 (INT32)
- 名称：SIM_GZ_SV_FUNC2 (INT32)
- 参数描述：SIM_GZ Servo 2 Output Function Comment: Select what should be output on SIM_GZ Servo 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


287. SIM_GZ_SV_FUNC3 (INT32)
- 名称：SIM_GZ_SV_FUNC3 (INT32)
- 参数描述：SIM_GZ Servo 3 Output Function Comment: Select what should be output on SIM_GZ Servo 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


288. SIM_GZ_SV_FUNC4 (INT32)
- 名称：SIM_GZ_SV_FUNC4 (INT32)
- 参数描述：SIM_GZ Servo 4 Output Function Comment: Select what should be output on SIM_GZ Servo 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


289. SIM_GZ_SV_FUNC5 (INT32)
- 名称：SIM_GZ_SV_FUNC5 (INT32)
- 参数描述：SIM_GZ Servo 5 Output Function Comment: Select what should be output on SIM_GZ Servo 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


290. SIM_GZ_SV_FUNC6 (INT32)
- 名称：SIM_GZ_SV_FUNC6 (INT32)
- 参数描述：SIM_GZ Servo 6 Output Function Comment: Select what should be output on SIM_GZ Servo 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


291. SIM_GZ_SV_FUNC7 (INT32)
- 名称：SIM_GZ_SV_FUNC7 (INT32)
- 参数描述：SIM_GZ Servo 7 Output Function Comment: Select what should be output on SIM_GZ Servo 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


292. SIM_GZ_SV_FUNC8 (INT32)
- 名称：SIM_GZ_SV_FUNC8 (INT32)
- 参数描述：SIM_GZ Servo 8 Output Function Comment: Select what should be output on SIM_GZ Servo 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


293. SIM_GZ_SV_MAX1 (INT32)
- 名称：SIM_GZ_SV_MAX1 (INT32)
- 参数描述：SIM_GZ Servo 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


294. SIM_GZ_SV_MAX2 (INT32)
- 名称：SIM_GZ_SV_MAX2 (INT32)
- 参数描述：SIM_GZ Servo 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


295. SIM_GZ_SV_MAX3 (INT32)
- 名称：SIM_GZ_SV_MAX3 (INT32)
- 参数描述：SIM_GZ Servo 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


296. SIM_GZ_SV_MAX4 (INT32)
- 名称：SIM_GZ_SV_MAX4 (INT32)
- 参数描述：SIM_GZ Servo 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


297. SIM_GZ_SV_MAX5 (INT32)
- 名称：SIM_GZ_SV_MAX5 (INT32)
- 参数描述：SIM_GZ Servo 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


298. SIM_GZ_SV_MAX6 (INT32)
- 名称：SIM_GZ_SV_MAX6 (INT32)
- 参数描述：SIM_GZ Servo 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


299. SIM_GZ_SV_MAX7 (INT32)
- 名称：SIM_GZ_SV_MAX7 (INT32)
- 参数描述：SIM_GZ Servo 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


300. SIM_GZ_SV_MAX8 (INT32)
- 名称：SIM_GZ_SV_MAX8 (INT32)
- 参数描述：SIM_GZ Servo 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


301. SIM_GZ_SV_MIN1 (INT32)
- 名称：SIM_GZ_SV_MIN1 (INT32)
- 参数描述：SIM_GZ Servo 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


302. SIM_GZ_SV_MIN2 (INT32)
- 名称：SIM_GZ_SV_MIN2 (INT32)
- 参数描述：SIM_GZ Servo 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


303. SIM_GZ_SV_MIN3 (INT32)
- 名称：SIM_GZ_SV_MIN3 (INT32)
- 参数描述：SIM_GZ Servo 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


304. SIM_GZ_SV_MIN4 (INT32)
- 名称：SIM_GZ_SV_MIN4 (INT32)
- 参数描述：SIM_GZ Servo 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


305. SIM_GZ_SV_MIN5 (INT32)
- 名称：SIM_GZ_SV_MIN5 (INT32)
- 参数描述：SIM_GZ Servo 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


306. SIM_GZ_SV_MIN6 (INT32)
- 名称：SIM_GZ_SV_MIN6 (INT32)
- 参数描述：SIM_GZ Servo 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


307. SIM_GZ_SV_MIN7 (INT32)
- 名称：SIM_GZ_SV_MIN7 (INT32)
- 参数描述：SIM_GZ Servo 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


308. SIM_GZ_SV_MIN8 (INT32)
- 名称：SIM_GZ_SV_MIN8 (INT32)
- 参数描述：SIM_GZ Servo 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


309. SIM_GZ_SV_REV (INT32)
- 名称：SIM_GZ_SV_REV (INT32)
- 参数描述：Reverse Output Range for SIM_GZ Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: SIM_GZ Servo 1 1: SIM_GZ Servo 2 2: SIM_GZ Servo 3 3: SIM_GZ Servo 4 4: SIM_GZ Servo 5 5: SIM_GZ Servo 6 6: SIM_GZ Servo 7 7: SIM_GZ Servo 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


310. TAP_ESC_FUNC1 (INT32)
- 名称：TAP_ESC_FUNC1 (INT32)
- 参数描述：TAP ESC Output ESC 1 Output Function Comment: Select what should be output on TAP ESC Output ESC 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


311. TAP_ESC_FUNC2 (INT32)
- 名称：TAP_ESC_FUNC2 (INT32)
- 参数描述：TAP ESC Output ESC 2 Output Function Comment: Select what should be output on TAP ESC Output ESC 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


312. TAP_ESC_FUNC3 (INT32)
- 名称：TAP_ESC_FUNC3 (INT32)
- 参数描述：TAP ESC Output ESC 3 Output Function Comment: Select what should be output on TAP ESC Output ESC 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


313. TAP_ESC_FUNC4 (INT32)
- 名称：TAP_ESC_FUNC4 (INT32)
- 参数描述：TAP ESC Output ESC 4 Output Function Comment: Select what should be output on TAP ESC Output ESC 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


314. TAP_ESC_FUNC5 (INT32)
- 名称：TAP_ESC_FUNC5 (INT32)
- 参数描述：TAP ESC Output ESC 5 Output Function Comment: Select what should be output on TAP ESC Output ESC 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


315. TAP_ESC_FUNC6 (INT32)
- 名称：TAP_ESC_FUNC6 (INT32)
- 参数描述：TAP ESC Output ESC 6 Output Function Comment: Select what should be output on TAP ESC Output ESC 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


316. TAP_ESC_FUNC7 (INT32)
- 名称：TAP_ESC_FUNC7 (INT32)
- 参数描述：TAP ESC Output ESC 7 Output Function Comment: Select what should be output on TAP ESC Output ESC 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


317. TAP_ESC_FUNC8 (INT32)
- 名称：TAP_ESC_FUNC8 (INT32)
- 参数描述：TAP ESC Output ESC 8 Output Function Comment: Select what should be output on TAP ESC Output ESC 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


318. TAP_ESC_REV (INT32)
- 名称：TAP_ESC_REV (INT32)
- 参数描述：Reverse Output Range for TAP ESC Output Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: TAP ESC Output ESC 1 1: TAP ESC Output ESC 2 2: TAP ESC Output ESC 3 3: TAP ESC Output ESC 4 4: TAP ESC Output ESC 5 5: TAP ESC Output ESC 6 6: TAP ESC Output ESC 7 7: TAP ESC Output ESC 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


319. UAVCAN_EC_FAIL1 (INT32)
- 名称：UAVCAN_EC_FAIL1 (INT32)
- 参数描述：UAVCAN ESC 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


320. UAVCAN_EC_FAIL2 (INT32)
- 名称：UAVCAN_EC_FAIL2 (INT32)
- 参数描述：UAVCAN ESC 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


321. UAVCAN_EC_FAIL3 (INT32)
- 名称：UAVCAN_EC_FAIL3 (INT32)
- 参数描述：UAVCAN ESC 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


322. UAVCAN_EC_FAIL4 (INT32)
- 名称：UAVCAN_EC_FAIL4 (INT32)
- 参数描述：UAVCAN ESC 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


323. UAVCAN_EC_FAIL5 (INT32)
- 名称：UAVCAN_EC_FAIL5 (INT32)
- 参数描述：UAVCAN ESC 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


324. UAVCAN_EC_FAIL6 (INT32)
- 名称：UAVCAN_EC_FAIL6 (INT32)
- 参数描述：UAVCAN ESC 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


325. UAVCAN_EC_FAIL7 (INT32)
- 名称：UAVCAN_EC_FAIL7 (INT32)
- 参数描述：UAVCAN ESC 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


326. UAVCAN_EC_FAIL8 (INT32)
- 名称：UAVCAN_EC_FAIL8 (INT32)
- 参数描述：UAVCAN ESC 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_EC_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


327. UAVCAN_EC_FUNC1 (INT32)
- 名称：UAVCAN_EC_FUNC1 (INT32)
- 参数描述：UAVCAN ESC 1 Output Function Comment: Select what should be output on UAVCAN ESC 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


328. UAVCAN_EC_FUNC2 (INT32)
- 名称：UAVCAN_EC_FUNC2 (INT32)
- 参数描述：UAVCAN ESC 2 Output Function Comment: Select what should be output on UAVCAN ESC 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


329. UAVCAN_EC_FUNC3 (INT32)
- 名称：UAVCAN_EC_FUNC3 (INT32)
- 参数描述：UAVCAN ESC 3 Output Function Comment: Select what should be output on UAVCAN ESC 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


330. UAVCAN_EC_FUNC4 (INT32)
- 名称：UAVCAN_EC_FUNC4 (INT32)
- 参数描述：UAVCAN ESC 4 Output Function Comment: Select what should be output on UAVCAN ESC 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


331. UAVCAN_EC_FUNC5 (INT32)
- 名称：UAVCAN_EC_FUNC5 (INT32)
- 参数描述：UAVCAN ESC 5 Output Function Comment: Select what should be output on UAVCAN ESC 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


332. UAVCAN_EC_FUNC6 (INT32)
- 名称：UAVCAN_EC_FUNC6 (INT32)
- 参数描述：UAVCAN ESC 6 Output Function Comment: Select what should be output on UAVCAN ESC 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


333. UAVCAN_EC_FUNC7 (INT32)
- 名称：UAVCAN_EC_FUNC7 (INT32)
- 参数描述：UAVCAN ESC 7 Output Function Comment: Select what should be output on UAVCAN ESC 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


334. UAVCAN_EC_FUNC8 (INT32)
- 名称：UAVCAN_EC_FUNC8 (INT32)
- 参数描述：UAVCAN ESC 8 Output Function Comment: Select what should be output on UAVCAN ESC 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


335. UAVCAN_EC_MAX1 (INT32)
- 名称：UAVCAN_EC_MAX1 (INT32)
- 参数描述：UAVCAN ESC 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


336. UAVCAN_EC_MAX2 (INT32)
- 名称：UAVCAN_EC_MAX2 (INT32)
- 参数描述：UAVCAN ESC 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


337. UAVCAN_EC_MAX3 (INT32)
- 名称：UAVCAN_EC_MAX3 (INT32)
- 参数描述：UAVCAN ESC 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


338. UAVCAN_EC_MAX4 (INT32)
- 名称：UAVCAN_EC_MAX4 (INT32)
- 参数描述：UAVCAN ESC 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


339. UAVCAN_EC_MAX5 (INT32)
- 名称：UAVCAN_EC_MAX5 (INT32)
- 参数描述：UAVCAN ESC 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


340. UAVCAN_EC_MAX6 (INT32)
- 名称：UAVCAN_EC_MAX6 (INT32)
- 参数描述：UAVCAN ESC 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


341. UAVCAN_EC_MAX7 (INT32)
- 名称：UAVCAN_EC_MAX7 (INT32)
- 参数描述：UAVCAN ESC 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


342. UAVCAN_EC_MAX8 (INT32)
- 名称：UAVCAN_EC_MAX8 (INT32)
- 参数描述：UAVCAN ESC 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


343. UAVCAN_EC_MIN1 (INT32)
- 名称：UAVCAN_EC_MIN1 (INT32)
- 参数描述：UAVCAN ESC 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


344. UAVCAN_EC_MIN2 (INT32)
- 名称：UAVCAN_EC_MIN2 (INT32)
- 参数描述：UAVCAN ESC 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


345. UAVCAN_EC_MIN3 (INT32)
- 名称：UAVCAN_EC_MIN3 (INT32)
- 参数描述：UAVCAN ESC 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


346. UAVCAN_EC_MIN4 (INT32)
- 名称：UAVCAN_EC_MIN4 (INT32)
- 参数描述：UAVCAN ESC 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


347. UAVCAN_EC_MIN5 (INT32)
- 名称：UAVCAN_EC_MIN5 (INT32)
- 参数描述：UAVCAN ESC 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


348. UAVCAN_EC_MIN6 (INT32)
- 名称：UAVCAN_EC_MIN6 (INT32)
- 参数描述：UAVCAN ESC 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


349. UAVCAN_EC_MIN7 (INT32)
- 名称：UAVCAN_EC_MIN7 (INT32)
- 参数描述：UAVCAN ESC 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


350. UAVCAN_EC_MIN8 (INT32)
- 名称：UAVCAN_EC_MIN8 (INT32)
- 参数描述：UAVCAN ESC 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


351. UAVCAN_EC_REV (INT32)
- 名称：UAVCAN_EC_REV (INT32)
- 参数描述：Reverse Output Range for UAVCAN Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: UAVCAN ESC 1 1: UAVCAN ESC 2 2: UAVCAN ESC 3 3: UAVCAN ESC 4 4: UAVCAN ESC 5 5: UAVCAN ESC 6 6: UAVCAN ESC 7 7: UAVCAN ESC 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


352. UAVCAN_SV_DIS1 (INT32)
- 名称：UAVCAN_SV_DIS1 (INT32)
- 参数描述：UAVCAN Servo 1 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


353. UAVCAN_SV_DIS2 (INT32)
- 名称：UAVCAN_SV_DIS2 (INT32)
- 参数描述：UAVCAN Servo 2 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


354. UAVCAN_SV_DIS3 (INT32)
- 名称：UAVCAN_SV_DIS3 (INT32)
- 参数描述：UAVCAN Servo 3 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


355. UAVCAN_SV_DIS4 (INT32)
- 名称：UAVCAN_SV_DIS4 (INT32)
- 参数描述：UAVCAN Servo 4 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


356. UAVCAN_SV_DIS5 (INT32)
- 名称：UAVCAN_SV_DIS5 (INT32)
- 参数描述：UAVCAN Servo 5 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


357. UAVCAN_SV_DIS6 (INT32)
- 名称：UAVCAN_SV_DIS6 (INT32)
- 参数描述：UAVCAN Servo 6 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


358. UAVCAN_SV_DIS7 (INT32)
- 名称：UAVCAN_SV_DIS7 (INT32)
- 参数描述：UAVCAN Servo 7 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


359. UAVCAN_SV_DIS8 (INT32)
- 名称：UAVCAN_SV_DIS8 (INT32)
- 参数描述：UAVCAN Servo 8 Disarmed Value Comment: This is the output value that is set when not armed. Note that non-motor outputs might already be active in prearm state if COM_PREARM_MODE is set.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`500`
- 单位：``


360. UAVCAN_SV_FAIL1 (INT32)
- 名称：UAVCAN_SV_FAIL1 (INT32)
- 参数描述：UAVCAN Servo 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


361. UAVCAN_SV_FAIL2 (INT32)
- 名称：UAVCAN_SV_FAIL2 (INT32)
- 参数描述：UAVCAN Servo 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


362. UAVCAN_SV_FAIL3 (INT32)
- 名称：UAVCAN_SV_FAIL3 (INT32)
- 参数描述：UAVCAN Servo 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


363. UAVCAN_SV_FAIL4 (INT32)
- 名称：UAVCAN_SV_FAIL4 (INT32)
- 参数描述：UAVCAN Servo 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


364. UAVCAN_SV_FAIL5 (INT32)
- 名称：UAVCAN_SV_FAIL5 (INT32)
- 参数描述：UAVCAN Servo 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


365. UAVCAN_SV_FAIL6 (INT32)
- 名称：UAVCAN_SV_FAIL6 (INT32)
- 参数描述：UAVCAN Servo 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


366. UAVCAN_SV_FAIL7 (INT32)
- 名称：UAVCAN_SV_FAIL7 (INT32)
- 参数描述：UAVCAN Servo 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


367. UAVCAN_SV_FAIL8 (INT32)
- 名称：UAVCAN_SV_FAIL8 (INT32)
- 参数描述：UAVCAN Servo 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UAVCAN_SV_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：``


368. UAVCAN_SV_FUNC1 (INT32)
- 名称：UAVCAN_SV_FUNC1 (INT32)
- 参数描述：UAVCAN Servo 1 Output Function Comment: Select what should be output on UAVCAN Servo 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


369. UAVCAN_SV_FUNC2 (INT32)
- 名称：UAVCAN_SV_FUNC2 (INT32)
- 参数描述：UAVCAN Servo 2 Output Function Comment: Select what should be output on UAVCAN Servo 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


370. UAVCAN_SV_FUNC3 (INT32)
- 名称：UAVCAN_SV_FUNC3 (INT32)
- 参数描述：UAVCAN Servo 3 Output Function Comment: Select what should be output on UAVCAN Servo 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


371. UAVCAN_SV_FUNC4 (INT32)
- 名称：UAVCAN_SV_FUNC4 (INT32)
- 参数描述：UAVCAN Servo 4 Output Function Comment: Select what should be output on UAVCAN Servo 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


372. UAVCAN_SV_FUNC5 (INT32)
- 名称：UAVCAN_SV_FUNC5 (INT32)
- 参数描述：UAVCAN Servo 5 Output Function Comment: Select what should be output on UAVCAN Servo 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


373. UAVCAN_SV_FUNC6 (INT32)
- 名称：UAVCAN_SV_FUNC6 (INT32)
- 参数描述：UAVCAN Servo 6 Output Function Comment: Select what should be output on UAVCAN Servo 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


374. UAVCAN_SV_FUNC7 (INT32)
- 名称：UAVCAN_SV_FUNC7 (INT32)
- 参数描述：UAVCAN Servo 7 Output Function Comment: Select what should be output on UAVCAN Servo 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


375. UAVCAN_SV_FUNC8 (INT32)
- 名称：UAVCAN_SV_FUNC8 (INT32)
- 参数描述：UAVCAN Servo 8 Output Function Comment: Select what should be output on UAVCAN Servo 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


376. UAVCAN_SV_MAX1 (INT32)
- 名称：UAVCAN_SV_MAX1 (INT32)
- 参数描述：UAVCAN Servo 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


377. UAVCAN_SV_MAX2 (INT32)
- 名称：UAVCAN_SV_MAX2 (INT32)
- 参数描述：UAVCAN Servo 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


378. UAVCAN_SV_MAX3 (INT32)
- 名称：UAVCAN_SV_MAX3 (INT32)
- 参数描述：UAVCAN Servo 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


379. UAVCAN_SV_MAX4 (INT32)
- 名称：UAVCAN_SV_MAX4 (INT32)
- 参数描述：UAVCAN Servo 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


380. UAVCAN_SV_MAX5 (INT32)
- 名称：UAVCAN_SV_MAX5 (INT32)
- 参数描述：UAVCAN Servo 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


381. UAVCAN_SV_MAX6 (INT32)
- 名称：UAVCAN_SV_MAX6 (INT32)
- 参数描述：UAVCAN Servo 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


382. UAVCAN_SV_MAX7 (INT32)
- 名称：UAVCAN_SV_MAX7 (INT32)
- 参数描述：UAVCAN Servo 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


383. UAVCAN_SV_MAX8 (INT32)
- 名称：UAVCAN_SV_MAX8 (INT32)
- 参数描述：UAVCAN Servo 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`1000`
- 单位：``


384. UAVCAN_SV_MIN1 (INT32)
- 名称：UAVCAN_SV_MIN1 (INT32)
- 参数描述：UAVCAN Servo 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


385. UAVCAN_SV_MIN2 (INT32)
- 名称：UAVCAN_SV_MIN2 (INT32)
- 参数描述：UAVCAN Servo 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


386. UAVCAN_SV_MIN3 (INT32)
- 名称：UAVCAN_SV_MIN3 (INT32)
- 参数描述：UAVCAN Servo 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


387. UAVCAN_SV_MIN4 (INT32)
- 名称：UAVCAN_SV_MIN4 (INT32)
- 参数描述：UAVCAN Servo 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


388. UAVCAN_SV_MIN5 (INT32)
- 名称：UAVCAN_SV_MIN5 (INT32)
- 参数描述：UAVCAN Servo 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


389. UAVCAN_SV_MIN6 (INT32)
- 名称：UAVCAN_SV_MIN6 (INT32)
- 参数描述：UAVCAN Servo 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


390. UAVCAN_SV_MIN7 (INT32)
- 名称：UAVCAN_SV_MIN7 (INT32)
- 参数描述：UAVCAN Servo 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


391. UAVCAN_SV_MIN8 (INT32)
- 名称：UAVCAN_SV_MIN8 (INT32)
- 参数描述：UAVCAN Servo 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1000]`
- 默认值：`0`
- 单位：``


392. UAVCAN_SV_REV (INT32)
- 名称：UAVCAN_SV_REV (INT32)
- 参数描述：Reverse Output Range for UAVCAN Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: UAVCAN Servo 1 1: UAVCAN Servo 2 2: UAVCAN Servo 3 3: UAVCAN Servo 4 4: UAVCAN Servo 5 5: UAVCAN Servo 6 6: UAVCAN Servo 7 7: UAVCAN Servo 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`0`
- 单位：``


393. UCAN1_ESC_FAIL1 (INT32)
- 名称：UCAN1_ESC_FAIL1 (INT32)
- 参数描述：UAVCANv1 ESC 1 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC1).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


394. UCAN1_ESC_FAIL10 (INT32)
- 名称：UCAN1_ESC_FAIL10 (INT32)
- 参数描述：UAVCANv1 ESC 10 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC10).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


395. UCAN1_ESC_FAIL11 (INT32)
- 名称：UCAN1_ESC_FAIL11 (INT32)
- 参数描述：UAVCANv1 ESC 11 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC11).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


396. UCAN1_ESC_FAIL12 (INT32)
- 名称：UCAN1_ESC_FAIL12 (INT32)
- 参数描述：UAVCANv1 ESC 12 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC12).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


397. UCAN1_ESC_FAIL13 (INT32)
- 名称：UCAN1_ESC_FAIL13 (INT32)
- 参数描述：UAVCANv1 ESC 13 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC13).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


398. UCAN1_ESC_FAIL14 (INT32)
- 名称：UCAN1_ESC_FAIL14 (INT32)
- 参数描述：UAVCANv1 ESC 14 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC14).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


399. UCAN1_ESC_FAIL15 (INT32)
- 名称：UCAN1_ESC_FAIL15 (INT32)
- 参数描述：UAVCANv1 ESC 15 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC15).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


400. UCAN1_ESC_FAIL16 (INT32)
- 名称：UCAN1_ESC_FAIL16 (INT32)
- 参数描述：UAVCANv1 ESC 16 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC16).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


401. UCAN1_ESC_FAIL2 (INT32)
- 名称：UCAN1_ESC_FAIL2 (INT32)
- 参数描述：UAVCANv1 ESC 2 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC2).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


402. UCAN1_ESC_FAIL3 (INT32)
- 名称：UCAN1_ESC_FAIL3 (INT32)
- 参数描述：UAVCANv1 ESC 3 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC3).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


403. UCAN1_ESC_FAIL4 (INT32)
- 名称：UCAN1_ESC_FAIL4 (INT32)
- 参数描述：UAVCANv1 ESC 4 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC4).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


404. UCAN1_ESC_FAIL5 (INT32)
- 名称：UCAN1_ESC_FAIL5 (INT32)
- 参数描述：UAVCANv1 ESC 5 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC5).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


405. UCAN1_ESC_FAIL6 (INT32)
- 名称：UCAN1_ESC_FAIL6 (INT32)
- 参数描述：UAVCANv1 ESC 6 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC6).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


406. UCAN1_ESC_FAIL7 (INT32)
- 名称：UCAN1_ESC_FAIL7 (INT32)
- 参数描述：UAVCANv1 ESC 7 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC7).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


407. UCAN1_ESC_FAIL8 (INT32)
- 名称：UCAN1_ESC_FAIL8 (INT32)
- 参数描述：UAVCANv1 ESC 8 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC8).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


408. UCAN1_ESC_FAIL9 (INT32)
- 名称：UCAN1_ESC_FAIL9 (INT32)
- 参数描述：UAVCANv1 ESC 9 Failsafe Value Comment: This is the output value that is set when in failsafe mode. When set to -1 (default), the value depends on the function (see UCAN1_ESC_FUNC9).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 8191]`
- 默认值：`-1`
- 单位：``


409. UCAN1_ESC_FUNC1 (INT32)
- 名称：UCAN1_ESC_FUNC1 (INT32)
- 参数描述：UAVCANv1 ESC 1 Output Function Comment: Select what should be output on UAVCANv1 ESC 1. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


410. UCAN1_ESC_FUNC10 (INT32)
- 名称：UCAN1_ESC_FUNC10 (INT32)
- 参数描述：UAVCANv1 ESC 10 Output Function Comment: Select what should be output on UAVCANv1 ESC 10. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


411. UCAN1_ESC_FUNC11 (INT32)
- 名称：UCAN1_ESC_FUNC11 (INT32)
- 参数描述：UAVCANv1 ESC 11 Output Function Comment: Select what should be output on UAVCANv1 ESC 11. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


412. UCAN1_ESC_FUNC12 (INT32)
- 名称：UCAN1_ESC_FUNC12 (INT32)
- 参数描述：UAVCANv1 ESC 12 Output Function Comment: Select what should be output on UAVCANv1 ESC 12. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


413. UCAN1_ESC_FUNC13 (INT32)
- 名称：UCAN1_ESC_FUNC13 (INT32)
- 参数描述：UAVCANv1 ESC 13 Output Function Comment: Select what should be output on UAVCANv1 ESC 13. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


414. UCAN1_ESC_FUNC14 (INT32)
- 名称：UCAN1_ESC_FUNC14 (INT32)
- 参数描述：UAVCANv1 ESC 14 Output Function Comment: Select what should be output on UAVCANv1 ESC 14. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


415. UCAN1_ESC_FUNC15 (INT32)
- 名称：UCAN1_ESC_FUNC15 (INT32)
- 参数描述：UAVCANv1 ESC 15 Output Function Comment: Select what should be output on UAVCANv1 ESC 15. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


416. UCAN1_ESC_FUNC16 (INT32)
- 名称：UCAN1_ESC_FUNC16 (INT32)
- 参数描述：UAVCANv1 ESC 16 Output Function Comment: Select what should be output on UAVCANv1 ESC 16. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


417. UCAN1_ESC_FUNC2 (INT32)
- 名称：UCAN1_ESC_FUNC2 (INT32)
- 参数描述：UAVCANv1 ESC 2 Output Function Comment: Select what should be output on UAVCANv1 ESC 2. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


418. UCAN1_ESC_FUNC3 (INT32)
- 名称：UCAN1_ESC_FUNC3 (INT32)
- 参数描述：UAVCANv1 ESC 3 Output Function Comment: Select what should be output on UAVCANv1 ESC 3. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


419. UCAN1_ESC_FUNC4 (INT32)
- 名称：UCAN1_ESC_FUNC4 (INT32)
- 参数描述：UAVCANv1 ESC 4 Output Function Comment: Select what should be output on UAVCANv1 ESC 4. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


420. UCAN1_ESC_FUNC5 (INT32)
- 名称：UCAN1_ESC_FUNC5 (INT32)
- 参数描述：UAVCANv1 ESC 5 Output Function Comment: Select what should be output on UAVCANv1 ESC 5. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


421. UCAN1_ESC_FUNC6 (INT32)
- 名称：UCAN1_ESC_FUNC6 (INT32)
- 参数描述：UAVCANv1 ESC 6 Output Function Comment: Select what should be output on UAVCANv1 ESC 6. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


422. UCAN1_ESC_FUNC7 (INT32)
- 名称：UCAN1_ESC_FUNC7 (INT32)
- 参数描述：UAVCANv1 ESC 7 Output Function Comment: Select what should be output on UAVCANv1 ESC 7. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


423. UCAN1_ESC_FUNC8 (INT32)
- 名称：UCAN1_ESC_FUNC8 (INT32)
- 参数描述：UAVCANv1 ESC 8 Output Function Comment: Select what should be output on UAVCANv1 ESC 8. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


424. UCAN1_ESC_FUNC9 (INT32)
- 名称：UCAN1_ESC_FUNC9 (INT32)
- 参数描述：UAVCANv1 ESC 9 Output Function Comment: Select what should be output on UAVCANv1 ESC 9. The default failsafe value is set according to the selected function: - 'Min' for ConstantMin - 'Max' for ConstantMax - 'Max' for Parachute - ('Max'+'Min')/2 for Servos - 'Disarmed' for the rest 参数对照:0: Disabled 1: Constant Min 2: Constant Max 101: Motor 1 102: Motor 2 103: Motor 3 104: Motor 4 105: Motor 5 106: Motor 6 107: Motor 7 108: Motor 8 109: Motor 9 110: Motor 10 111: Motor 11 112: Motor 12 201: Servo 1 202: Servo 2 203: Servo 3 204: Servo 4 205: Servo 5 206: Servo 6 207: Servo 7 208: Servo 8 301: Offboard Actuator Set 1 302: Offboard Actuator Set 2 303: Offboard Actuator Set 3 304: Offboard Actuator Set 4 305: Offboard Actuator Set 5 306: Offboard Actuator Set 6 400: Landing Gear 401: Parachute 402: RC Roll 403: RC Pitch 404: RC Throttle 405: RC Yaw 406: RC Flaps 407: RC AUX 1 408: RC AUX 2 409: RC AUX 3 410: RC AUX 4 411: RC AUX 5 412: RC AUX 6 420: Gimbal Roll 421: Gimbal Pitch 422: Gimbal Yaw 430: Gripper 440: Landing Gear Wheel
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


425. UCAN1_ESC_MAX1 (INT32)
- 名称：UCAN1_ESC_MAX1 (INT32)
- 参数描述：UAVCANv1 ESC 1 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


426. UCAN1_ESC_MAX10 (INT32)
- 名称：UCAN1_ESC_MAX10 (INT32)
- 参数描述：UAVCANv1 ESC 10 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


427. UCAN1_ESC_MAX11 (INT32)
- 名称：UCAN1_ESC_MAX11 (INT32)
- 参数描述：UAVCANv1 ESC 11 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


428. UCAN1_ESC_MAX12 (INT32)
- 名称：UCAN1_ESC_MAX12 (INT32)
- 参数描述：UAVCANv1 ESC 12 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


429. UCAN1_ESC_MAX13 (INT32)
- 名称：UCAN1_ESC_MAX13 (INT32)
- 参数描述：UAVCANv1 ESC 13 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


430. UCAN1_ESC_MAX14 (INT32)
- 名称：UCAN1_ESC_MAX14 (INT32)
- 参数描述：UAVCANv1 ESC 14 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


431. UCAN1_ESC_MAX15 (INT32)
- 名称：UCAN1_ESC_MAX15 (INT32)
- 参数描述：UAVCANv1 ESC 15 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


432. UCAN1_ESC_MAX16 (INT32)
- 名称：UCAN1_ESC_MAX16 (INT32)
- 参数描述：UAVCANv1 ESC 16 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


433. UCAN1_ESC_MAX2 (INT32)
- 名称：UCAN1_ESC_MAX2 (INT32)
- 参数描述：UAVCANv1 ESC 2 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


434. UCAN1_ESC_MAX3 (INT32)
- 名称：UCAN1_ESC_MAX3 (INT32)
- 参数描述：UAVCANv1 ESC 3 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


435. UCAN1_ESC_MAX4 (INT32)
- 名称：UCAN1_ESC_MAX4 (INT32)
- 参数描述：UAVCANv1 ESC 4 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


436. UCAN1_ESC_MAX5 (INT32)
- 名称：UCAN1_ESC_MAX5 (INT32)
- 参数描述：UAVCANv1 ESC 5 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


437. UCAN1_ESC_MAX6 (INT32)
- 名称：UCAN1_ESC_MAX6 (INT32)
- 参数描述：UAVCANv1 ESC 6 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


438. UCAN1_ESC_MAX7 (INT32)
- 名称：UCAN1_ESC_MAX7 (INT32)
- 参数描述：UAVCANv1 ESC 7 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


439. UCAN1_ESC_MAX8 (INT32)
- 名称：UCAN1_ESC_MAX8 (INT32)
- 参数描述：UAVCANv1 ESC 8 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


440. UCAN1_ESC_MAX9 (INT32)
- 名称：UCAN1_ESC_MAX9 (INT32)
- 参数描述：UAVCANv1 ESC 9 Maximum Value Comment: Maxmimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`8191`
- 单位：``


441. UCAN1_ESC_MIN1 (INT32)
- 名称：UCAN1_ESC_MIN1 (INT32)
- 参数描述：UAVCANv1 ESC 1 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


442. UCAN1_ESC_MIN10 (INT32)
- 名称：UCAN1_ESC_MIN10 (INT32)
- 参数描述：UAVCANv1 ESC 10 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


443. UCAN1_ESC_MIN11 (INT32)
- 名称：UCAN1_ESC_MIN11 (INT32)
- 参数描述：UAVCANv1 ESC 11 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


444. UCAN1_ESC_MIN12 (INT32)
- 名称：UCAN1_ESC_MIN12 (INT32)
- 参数描述：UAVCANv1 ESC 12 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


445. UCAN1_ESC_MIN13 (INT32)
- 名称：UCAN1_ESC_MIN13 (INT32)
- 参数描述：UAVCANv1 ESC 13 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


446. UCAN1_ESC_MIN14 (INT32)
- 名称：UCAN1_ESC_MIN14 (INT32)
- 参数描述：UAVCANv1 ESC 14 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


447. UCAN1_ESC_MIN15 (INT32)
- 名称：UCAN1_ESC_MIN15 (INT32)
- 参数描述：UAVCANv1 ESC 15 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


448. UCAN1_ESC_MIN16 (INT32)
- 名称：UCAN1_ESC_MIN16 (INT32)
- 参数描述：UAVCANv1 ESC 16 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


449. UCAN1_ESC_MIN2 (INT32)
- 名称：UCAN1_ESC_MIN2 (INT32)
- 参数描述：UAVCANv1 ESC 2 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


450. UCAN1_ESC_MIN3 (INT32)
- 名称：UCAN1_ESC_MIN3 (INT32)
- 参数描述：UAVCANv1 ESC 3 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


451. UCAN1_ESC_MIN4 (INT32)
- 名称：UCAN1_ESC_MIN4 (INT32)
- 参数描述：UAVCANv1 ESC 4 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


452. UCAN1_ESC_MIN5 (INT32)
- 名称：UCAN1_ESC_MIN5 (INT32)
- 参数描述：UAVCANv1 ESC 5 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


453. UCAN1_ESC_MIN6 (INT32)
- 名称：UCAN1_ESC_MIN6 (INT32)
- 参数描述：UAVCANv1 ESC 6 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


454. UCAN1_ESC_MIN7 (INT32)
- 名称：UCAN1_ESC_MIN7 (INT32)
- 参数描述：UAVCANv1 ESC 7 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


455. UCAN1_ESC_MIN8 (INT32)
- 名称：UCAN1_ESC_MIN8 (INT32)
- 参数描述：UAVCANv1 ESC 8 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


456. UCAN1_ESC_MIN9 (INT32)
- 名称：UCAN1_ESC_MIN9 (INT32)
- 参数描述：UAVCANv1 ESC 9 Minimum Value Comment: Minimum output value (when not disarmed).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 8191]`
- 默认值：`1`
- 单位：``


457. UCAN1_ESC_REV (INT32)
- 名称：UCAN1_ESC_REV (INT32)
- 参数描述：Reverse Output Range for UAVCANv1 Comment: Allows to reverse the output range for each channel. Note: this is only useful for servos. Bitmask:0: UAVCANv1 ESC 1 1: UAVCANv1 ESC 2 2: UAVCANv1 ESC 3 3: UAVCANv1 ESC 4 4: UAVCANv1 ESC 5 5: UAVCANv1 ESC 6 6: UAVCANv1 ESC 7 7: UAVCANv1 ESC 8 8: UAVCANv1 ESC 9 9: UAVCANv1 ESC 10 10: UAVCANv1 ESC 11 11: UAVCANv1 ESC 12 12: UAVCANv1 ESC 13 13: UAVCANv1 ESC 14 14: UAVCANv1 ESC 15 15: UAVCANv1 ESC 16
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 65535]`
- 默认值：`0`
- 单位：``


458. ASPD_BETA_GATE (INT32)
- 名称：ASPD_BETA_GATE (INT32)
- 参数描述：Gate size for sideslip angle fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 5]`
- 默认值：`1`
- 单位：`SD`


459. ASPD_BETA_NOISE (FLOAT)
- 名称：ASPD_BETA_NOISE (FLOAT)
- 参数描述：Wind estimator sideslip measurement noise Comment: Sideslip measurement noise of the internal wind estimator(s) of the airspeed selector.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.3`
- 单位：`rad`


460. ASPD_DO_CHECKS (INT32)
- 名称：ASPD_DO_CHECKS (INT32)
- 参数描述：Enable checks on airspeed sensors Comment: Controls which checks are run to check airspeed data for validity. Only applied if ASPD_PRIMARY > 0. Bitmask:0: Only data missing check (triggers if more than 1s no data) 1: Data stuck (triggers if data is exactly constant for 2s in FW mode) 2: Innovation check (see ASPD_FS_INNOV) 3: Load factor check (triggers if measurement is below stall speed)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 15]`
- 默认值：`7`
- 单位：``


461. ASPD_FALLBACK_GW (INT32)
- 名称：ASPD_FALLBACK_GW (INT32)
- 参数描述：Enable fallback to sensor-less airspeed estimation Comment: If set to true and airspeed checks are enabled, it will use a sensor-less airspeed estimation based on groundspeed minus windspeed if no other airspeed sensor available to fall back to. 参数对照:0: Disable fallback to sensor-less estimation 1: Enable fallback to sensor-less estimation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


462. ASPD_FS_INNOV (FLOAT)
- 名称：ASPD_FS_INNOV (FLOAT)
- 参数描述：Airspeed failure innovation threshold Comment: This specifies the minimum airspeed innovation required to trigger a failsafe. Larger values make the check less sensitive, smaller values make it more sensitive. Large innovations indicate an inconsistency between predicted (groundspeed - windspeeed) and measured airspeed. The time required to detect a fault when the threshold is exceeded depends on the size of the exceedance and is controlled by the ASPD_FS_INTEG parameter.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 10.0]`
- 默认值：`5.`
- 单位：`m/s`


463. ASPD_FS_INTEG (FLOAT)
- 名称：ASPD_FS_INTEG (FLOAT)
- 参数描述：Airspeed failure innovation integral threshold Comment: This sets the time integral of airspeed innovation exceedance above ASPD_FS_INNOV required to trigger a failsafe. Larger values make the check less sensitive, smaller positive values make it more sensitive.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 50.0]`
- 默认值：`10.`
- 单位：`m`


464. ASPD_FS_T_START (INT32)
- 名称：ASPD_FS_T_START (INT32)
- 参数描述：Airspeed failsafe start delay Comment: Delay before switching back to using airspeed sensor if checks indicate sensor is good. Set to a negative value to disable the re-enabling in flight.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1000]`
- 默认值：`-1`
- 单位：`s`


465. ASPD_FS_T_STOP (INT32)
- 名称：ASPD_FS_T_STOP (INT32)
- 参数描述：Airspeed failsafe stop delay Comment: Delay before stopping use of airspeed sensor if checks indicate sensor is bad.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 10]`
- 默认值：`2`
- 单位：`s`


466. ASPD_PRIMARY (INT32)
- 名称：ASPD_PRIMARY (INT32)
- 参数描述：Index or primary airspeed measurement source  Values:-1: Disabled 0: Groundspeed minus windspeed 1: First airspeed sensor 2: Second airspeed sensor 3: Third airspeed sensor Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


467. ASPD_SCALE_1 (FLOAT)
- 名称：ASPD_SCALE_1 (FLOAT)
- 参数描述：Scale of airspeed sensor 1 Comment: This is the scale IAS --> CAS of the first airspeed sensor instance Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 2.0]`
- 默认值：`1.0`
- 单位：``


468. ASPD_SCALE_2 (FLOAT)
- 名称：ASPD_SCALE_2 (FLOAT)
- 参数描述：Scale of airspeed sensor 2 Comment: This is the scale IAS --> CAS of the second airspeed sensor instance Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 2.0]`
- 默认值：`1.0`
- 单位：``


469. ASPD_SCALE_3 (FLOAT)
- 名称：ASPD_SCALE_3 (FLOAT)
- 参数描述：Scale of airspeed sensor 3 Comment: This is the scale IAS --> CAS of the third airspeed sensor instance Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 2.0]`
- 默认值：`1.0`
- 单位：``


470. ASPD_SCALE_APPLY (INT32)
- 名称：ASPD_SCALE_APPLY (INT32)
- 参数描述：Controls when to apply the new estimated airspeed scale(s)  Values:0: Do not automatically apply the estimated scale 1: Apply the estimated scale after disarm 2: Apply the estimated scale in air
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


471. ASPD_SCALE_NSD (FLOAT)
- 名称：ASPD_SCALE_NSD (FLOAT)
- 参数描述：Wind estimator true airspeed scale process noise spectral density Comment: Airspeed scale process noise of the internal wind estimator(s) of the airspeed selector. When unaided, the scale uncertainty (1-sigma, unitless) increases by this amount every second.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.1]`
- 默认值：`1.e-4`
- 单位：`1/s/sqrt(Hz)`


472. ASPD_TAS_GATE (INT32)
- 名称：ASPD_TAS_GATE (INT32)
- 参数描述：Gate size for true airspeed fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 5]`
- 默认值：`3`
- 单位：`SD`


473. ASPD_TAS_NOISE (FLOAT)
- 名称：ASPD_TAS_NOISE (FLOAT)
- 参数描述：Wind estimator true airspeed measurement noise Comment: True airspeed measurement noise of the internal wind estimator(s) of the airspeed selector.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`1.4`
- 单位：`m/s`


474. ASPD_WERR_THR (FLOAT)
- 名称：ASPD_WERR_THR (FLOAT)
- 参数描述：Horizontal wind uncertainty threshold for synthetic airspeed Comment: The synthetic airspeed estimate (from groundspeed and heading) will be declared valid as soon and as long the horizontal wind uncertainty is below this value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.001, 5]`
- 默认值：`0.55`
- 单位：`m/s`


475. ASPD_WIND_NSD (FLOAT)
- 名称：ASPD_WIND_NSD (FLOAT)
- 参数描述：Wind estimator wind process noise spectral density Comment: Wind process noise of the internal wind estimator(s) of the airspeed selector. When unaided, the wind estimate uncertainty (1-sigma, in m/s) increases by this amount every second.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`1.e-2`
- 单位：`m/s^2/sqrt(Hz)`


476. ATT_ACC_COMP (INT32)
- 名称：ATT_ACC_COMP (INT32)
- 参数描述：Acceleration compensation based on GPS velocity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


477. ATT_BIAS_MAX (FLOAT)
- 名称：ATT_BIAS_MAX (FLOAT)
- 参数描述：Gyro bias limit
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0.05`
- 单位：`rad/s`


478. ATT_EXT_HDG_M (INT32)
- 名称：ATT_EXT_HDG_M (INT32)
- 参数描述：External heading usage mode (from Motion capture/Vision) Comment: Set to 1 to use heading estimate from vision. Set to 2 to use heading from motion capture. 参数对照:0: None 1: Vision 2: Motion Capture
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


479. ATT_MAG_DECL (FLOAT)
- 名称：ATT_MAG_DECL (FLOAT)
- 参数描述：Magnetic declination, in degrees Comment: This parameter is not used in normal operation, as the declination is looked up based on the GPS coordinates of the vehicle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`deg`


480. ATT_MAG_DECL_A (INT32)
- 名称：ATT_MAG_DECL_A (INT32)
- 参数描述：Automatic GPS based declination compensation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


481. ATT_W_ACC (FLOAT)
- 名称：ATT_W_ACC (FLOAT)
- 参数描述：Complimentary filter accelerometer weight
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.2`
- 单位：``


482. ATT_W_EXT_HDG (FLOAT)
- 名称：ATT_W_EXT_HDG (FLOAT)
- 参数描述：Complimentary filter external heading weight
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.1`
- 单位：``


483. ATT_W_GYRO_BIAS (FLOAT)
- 名称：ATT_W_GYRO_BIAS (FLOAT)
- 参数描述：Complimentary filter gyroscope bias weight
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.1`
- 单位：``


484. ATT_W_MAG (FLOAT)
- 名称：ATT_W_MAG (FLOAT)
- 参数描述：Complimentary filter magnetometer weight Comment: Set to 0 to avoid using the magnetometer.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.1`
- 单位：``


485. FW_AT_APPLY (INT32)
- 名称：FW_AT_APPLY (INT32)
- 参数描述：Controls when to apply the new gains Comment: After the auto-tuning sequence is completed, a new set of gains is available and can be applied immediately or after landing. 参数对照:0: Do not apply the new gains (logging only) 1: Apply the new gains after disarm 2: Apply the new gains in air
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


486. FW_AT_AXES (INT32)
- 名称：FW_AT_AXES (INT32)
- 参数描述：Tuning axes selection Comment: Defines which axes will be tuned during the auto-tuning sequence Set bits in the following positions to enable: 0 : Roll 1 : Pitch 2 : Yaw Bitmask:0: roll 1: pitch 2: yaw
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 7]`
- 默认值：`3`
- 单位：``


487. FW_AT_MAN_AUX (INT32)
- 名称：FW_AT_MAN_AUX (INT32)
- 参数描述：Enable/disable auto tuning using an RC AUX input Comment: Defines which RC_MAP_AUXn parameter maps the RC channel used to enable/disable auto tuning. 参数对照:0: Disable 1: Aux1 2: Aux2 3: Aux3 4: Aux4 5: Aux5 6: Aux6
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


488. FW_AT_START (INT32)
- 名称：FW_AT_START (INT32)
- 参数描述：Start the autotuning sequence Comment: WARNING: this will inject steps to the rate controller and can be dangerous. Only activate if you know what you are doing, and in a safe environment. Any motion of the remote stick will abort the signal injection and reset this parameter Best is to perform the identification in position or hold mode. Increase the amplitude of the injected signal using FW_AT_SYSID_AMP for more signal/noise ratio
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


489. FW_AT_SYSID_AMP (FLOAT)
- 名称：FW_AT_SYSID_AMP (FLOAT)
- 参数描述：Amplitude of the injected signal Comment: This parameter scales the signal sent to the rate controller during system identification.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 6.0]`
- 默认值：`1.0`
- 单位：``


490. MC_AT_APPLY (INT32)
- 名称：MC_AT_APPLY (INT32)
- 参数描述：Controls when to apply the new gains Comment: After the auto-tuning sequence is completed, a new set of gains is available and can be applied immediately or after landing. WARNING Applying the gains in air is dangerous as there is no guarantee that those new gains will be able to stabilize the drone properly. 参数对照:0: Do not apply the new gains (logging only) 1: Apply the new gains after disarm 2: WARNING Apply the new gains in air
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


491. MC_AT_EN (INT32)
- 名称：MC_AT_EN (INT32)
- 参数描述：Multicopter autotune module enable
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


492. MC_AT_RISE_TIME (FLOAT)
- 名称：MC_AT_RISE_TIME (FLOAT)
- 参数描述：Desired angular rate closed-loop rise time
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 0.5]`
- 默认值：`0.14`
- 单位：`s`


493. MC_AT_START (INT32)
- 名称：MC_AT_START (INT32)
- 参数描述：Start the autotuning sequence Comment: WARNING: this will inject steps to the rate controller and can be dangerous. Only activate if you know what you are doing, and in a safe environment. Any motion of the remote stick will abort the signal injection and reset this parameter Best is to perform the identification in position or hold mode. Increase the amplitude of the injected signal using MC_AT_SYSID_AMP for more signal/noise ratio
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


494. MC_AT_SYSID_AMP (FLOAT)
- 名称：MC_AT_SYSID_AMP (FLOAT)
- 参数描述：Amplitude of the injected signal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 6.0]`
- 默认值：`0.7`
- 单位：``


495. BAT1_A_PER_V (FLOAT)
- 名称：BAT1_A_PER_V (FLOAT)
- 参数描述：Battery 1 current per volt (A/V) Comment: The voltage seen by the ADC multiplied by this factor will determine the battery current. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1.0`
- 单位：``


496. BAT1_CAPACITY (FLOAT)
- 名称：BAT1_CAPACITY (FLOAT)
- 参数描述：Battery 1 capacity Comment: Defines the capacity of battery 1 in mAh. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 100000] (50)`
- 默认值：`-1.0`
- 单位：`mAh`


497. BAT1_I_CHANNEL (INT32)
- 名称：BAT1_I_CHANNEL (INT32)
- 参数描述：Battery 1 Current ADC Channel Comment: This parameter specifies the ADC channel used to monitor current of main power battery. A value of -1 means to use the board default. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`-1`
- 单位：``


498. BAT1_N_CELLS (INT32)
- 名称：BAT1_N_CELLS (INT32)
- 参数描述：Number of cells for battery 1 Comment: Defines the number of cells the attached battery consists of. 参数对照:0: Unknown 1: 1S Battery 2: 2S Battery 3: 3S Battery 4: 4S Battery 5: 5S Battery 6: 6S Battery 7: 7S Battery 8: 8S Battery 9: 9S Battery 10: 10S Battery 11: 11S Battery 12: 12S Battery 13: 13S Battery 14: 14S Battery 15: 15S Battery 16: 16S Battery Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


499. BAT1_R_INTERNAL (FLOAT)
- 名称：BAT1_R_INTERNAL (FLOAT)
- 参数描述：Explicitly defines the per cell internal resistance for battery 1 Comment: If non-negative, then this will be used in place of BAT1_V_LOAD_DROP for all calculations. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 0.2] (0.0005)`
- 默认值：`0.005`
- 单位：`欧姆`


500. BAT1_SOURCE (INT32)
- 名称：BAT1_SOURCE (INT32)
- 参数描述：Battery 1 monitoring source Comment: This parameter controls the source of battery data. The value 'Power Module' means that measurements are expected to come from a power module. If the value is set to 'External' then the system expects to receive mavlink battery status messages. If the value is set to 'ESCs', the battery information are taken from the esc_status message. This requires the ESC to provide both voltage as well as current. 参数对照:-1: Disabled 0: Power Module 1: External 2: ESCs Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


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
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1000, 2000]`
- 默认值：`1500`
- 单位：`µs`


539. TRIG_PWM_SHOOT (INT32)
- 名称：TRIG_PWM_SHOOT (INT32)
- 参数描述：PWM output to trigger shot    Reboot required: true
  - 翻译：
  - gpt注解：
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
- 参数描述：Cyphal Node ID Comment: Read the specs at http://uavcan.org to learn more about Node ID. Reboot required: true
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


1001. CA_ROTOR1_CT (FLOAT)
- 名称：CA_ROTOR1_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 1 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1002. CA_ROTOR1_KM (FLOAT)
- 名称：CA_ROTOR1_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 1 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1003. CA_ROTOR1_PX (FLOAT)
- 名称：CA_ROTOR1_PX (FLOAT)
- 参数描述：Position of rotor 1 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1004. CA_ROTOR1_PY (FLOAT)
- 名称：CA_ROTOR1_PY (FLOAT)
- 参数描述：Position of rotor 1 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1005. CA_ROTOR1_PZ (FLOAT)
- 名称：CA_ROTOR1_PZ (FLOAT)
- 参数描述：Position of rotor 1 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1006. CA_ROTOR1_TILT (INT32)
- 名称：CA_ROTOR1_TILT (INT32)
- 参数描述：Rotor 1 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1007. CA_ROTOR2_AX (FLOAT)
- 名称：CA_ROTOR2_AX (FLOAT)
- 参数描述：Axis of rotor 2 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1008. CA_ROTOR2_AY (FLOAT)
- 名称：CA_ROTOR2_AY (FLOAT)
- 参数描述：Axis of rotor 2 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1009. CA_ROTOR2_AZ (FLOAT)
- 名称：CA_ROTOR2_AZ (FLOAT)
- 参数描述：Axis of rotor 2 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1010. CA_ROTOR2_CT (FLOAT)
- 名称：CA_ROTOR2_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 2 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1011. CA_ROTOR2_KM (FLOAT)
- 名称：CA_ROTOR2_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 2 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1012. CA_ROTOR2_PX (FLOAT)
- 名称：CA_ROTOR2_PX (FLOAT)
- 参数描述：Position of rotor 2 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1013. CA_ROTOR2_PY (FLOAT)
- 名称：CA_ROTOR2_PY (FLOAT)
- 参数描述：Position of rotor 2 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1014. CA_ROTOR2_PZ (FLOAT)
- 名称：CA_ROTOR2_PZ (FLOAT)
- 参数描述：Position of rotor 2 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1015. CA_ROTOR2_TILT (INT32)
- 名称：CA_ROTOR2_TILT (INT32)
- 参数描述：Rotor 2 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1016. CA_ROTOR3_AX (FLOAT)
- 名称：CA_ROTOR3_AX (FLOAT)
- 参数描述：Axis of rotor 3 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1017. CA_ROTOR3_AY (FLOAT)
- 名称：CA_ROTOR3_AY (FLOAT)
- 参数描述：Axis of rotor 3 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1018. CA_ROTOR3_AZ (FLOAT)
- 名称：CA_ROTOR3_AZ (FLOAT)
- 参数描述：Axis of rotor 3 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1019. CA_ROTOR3_CT (FLOAT)
- 名称：CA_ROTOR3_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 3 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1020. CA_ROTOR3_KM (FLOAT)
- 名称：CA_ROTOR3_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 3 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1021. CA_ROTOR3_PX (FLOAT)
- 名称：CA_ROTOR3_PX (FLOAT)
- 参数描述：Position of rotor 3 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1022. CA_ROTOR3_PY (FLOAT)
- 名称：CA_ROTOR3_PY (FLOAT)
- 参数描述：Position of rotor 3 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1023. CA_ROTOR3_PZ (FLOAT)
- 名称：CA_ROTOR3_PZ (FLOAT)
- 参数描述：Position of rotor 3 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1024. CA_ROTOR3_TILT (INT32)
- 名称：CA_ROTOR3_TILT (INT32)
- 参数描述：Rotor 3 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1025. CA_ROTOR4_AX (FLOAT)
- 名称：CA_ROTOR4_AX (FLOAT)
- 参数描述：Axis of rotor 4 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1026. CA_ROTOR4_AY (FLOAT)
- 名称：CA_ROTOR4_AY (FLOAT)
- 参数描述：Axis of rotor 4 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1027. CA_ROTOR4_AZ (FLOAT)
- 名称：CA_ROTOR4_AZ (FLOAT)
- 参数描述：Axis of rotor 4 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1028. CA_ROTOR4_CT (FLOAT)
- 名称：CA_ROTOR4_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 4 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1029. CA_ROTOR4_KM (FLOAT)
- 名称：CA_ROTOR4_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 4 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1030. CA_ROTOR4_PX (FLOAT)
- 名称：CA_ROTOR4_PX (FLOAT)
- 参数描述：Position of rotor 4 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1031. CA_ROTOR4_PY (FLOAT)
- 名称：CA_ROTOR4_PY (FLOAT)
- 参数描述：Position of rotor 4 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1032. CA_ROTOR4_PZ (FLOAT)
- 名称：CA_ROTOR4_PZ (FLOAT)
- 参数描述：Position of rotor 4 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1033. CA_ROTOR4_TILT (INT32)
- 名称：CA_ROTOR4_TILT (INT32)
- 参数描述：Rotor 4 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1034. CA_ROTOR5_AX (FLOAT)
- 名称：CA_ROTOR5_AX (FLOAT)
- 参数描述：Axis of rotor 5 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1035. CA_ROTOR5_AY (FLOAT)
- 名称：CA_ROTOR5_AY (FLOAT)
- 参数描述：Axis of rotor 5 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1036. CA_ROTOR5_AZ (FLOAT)
- 名称：CA_ROTOR5_AZ (FLOAT)
- 参数描述：Axis of rotor 5 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1037. CA_ROTOR5_CT (FLOAT)
- 名称：CA_ROTOR5_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 5 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1038. CA_ROTOR5_KM (FLOAT)
- 名称：CA_ROTOR5_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 5 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1039. CA_ROTOR5_PX (FLOAT)
- 名称：CA_ROTOR5_PX (FLOAT)
- 参数描述：Position of rotor 5 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1040. CA_ROTOR5_PY (FLOAT)
- 名称：CA_ROTOR5_PY (FLOAT)
- 参数描述：Position of rotor 5 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1041. CA_ROTOR5_PZ (FLOAT)
- 名称：CA_ROTOR5_PZ (FLOAT)
- 参数描述：Position of rotor 5 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1042. CA_ROTOR5_TILT (INT32)
- 名称：CA_ROTOR5_TILT (INT32)
- 参数描述：Rotor 5 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1043. CA_ROTOR6_AX (FLOAT)
- 名称：CA_ROTOR6_AX (FLOAT)
- 参数描述：Axis of rotor 6 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1044. CA_ROTOR6_AY (FLOAT)
- 名称：CA_ROTOR6_AY (FLOAT)
- 参数描述：Axis of rotor 6 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1045. CA_ROTOR6_AZ (FLOAT)
- 名称：CA_ROTOR6_AZ (FLOAT)
- 参数描述：Axis of rotor 6 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1046. CA_ROTOR6_CT (FLOAT)
- 名称：CA_ROTOR6_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 6 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1047. CA_ROTOR6_KM (FLOAT)
- 名称：CA_ROTOR6_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 6 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1048. CA_ROTOR6_PX (FLOAT)
- 名称：CA_ROTOR6_PX (FLOAT)
- 参数描述：Position of rotor 6 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1049. CA_ROTOR6_PY (FLOAT)
- 名称：CA_ROTOR6_PY (FLOAT)
- 参数描述：Position of rotor 6 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1050. CA_ROTOR6_PZ (FLOAT)
- 名称：CA_ROTOR6_PZ (FLOAT)
- 参数描述：Position of rotor 6 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1051. CA_ROTOR6_TILT (INT32)
- 名称：CA_ROTOR6_TILT (INT32)
- 参数描述：Rotor 6 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1052. CA_ROTOR7_AX (FLOAT)
- 名称：CA_ROTOR7_AX (FLOAT)
- 参数描述：Axis of rotor 7 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1053. CA_ROTOR7_AY (FLOAT)
- 名称：CA_ROTOR7_AY (FLOAT)
- 参数描述：Axis of rotor 7 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1054. CA_ROTOR7_AZ (FLOAT)
- 名称：CA_ROTOR7_AZ (FLOAT)
- 参数描述：Axis of rotor 7 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1055. CA_ROTOR7_CT (FLOAT)
- 名称：CA_ROTOR7_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 7 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1056. CA_ROTOR7_KM (FLOAT)
- 名称：CA_ROTOR7_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 7 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1057. CA_ROTOR7_PX (FLOAT)
- 名称：CA_ROTOR7_PX (FLOAT)
- 参数描述：Position of rotor 7 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1058. CA_ROTOR7_PY (FLOAT)
- 名称：CA_ROTOR7_PY (FLOAT)
- 参数描述：Position of rotor 7 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1059. CA_ROTOR7_PZ (FLOAT)
- 名称：CA_ROTOR7_PZ (FLOAT)
- 参数描述：Position of rotor 7 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1060. CA_ROTOR7_TILT (INT32)
- 名称：CA_ROTOR7_TILT (INT32)
- 参数描述：Rotor 7 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1061. CA_ROTOR8_AX (FLOAT)
- 名称：CA_ROTOR8_AX (FLOAT)
- 参数描述：Axis of rotor 8 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1062. CA_ROTOR8_AY (FLOAT)
- 名称：CA_ROTOR8_AY (FLOAT)
- 参数描述：Axis of rotor 8 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1063. CA_ROTOR8_AZ (FLOAT)
- 名称：CA_ROTOR8_AZ (FLOAT)
- 参数描述：Axis of rotor 8 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1064. CA_ROTOR8_CT (FLOAT)
- 名称：CA_ROTOR8_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 8 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1065. CA_ROTOR8_KM (FLOAT)
- 名称：CA_ROTOR8_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 8 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1066. CA_ROTOR8_PX (FLOAT)
- 名称：CA_ROTOR8_PX (FLOAT)
- 参数描述：Position of rotor 8 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1067. CA_ROTOR8_PY (FLOAT)
- 名称：CA_ROTOR8_PY (FLOAT)
- 参数描述：Position of rotor 8 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1068. CA_ROTOR8_PZ (FLOAT)
- 名称：CA_ROTOR8_PZ (FLOAT)
- 参数描述：Position of rotor 8 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1069. CA_ROTOR8_TILT (INT32)
- 名称：CA_ROTOR8_TILT (INT32)
- 参数描述：Rotor 8 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1070. CA_ROTOR9_AX (FLOAT)
- 名称：CA_ROTOR9_AX (FLOAT)
- 参数描述：Axis of rotor 9 thrust vector, X body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1071. CA_ROTOR9_AY (FLOAT)
- 名称：CA_ROTOR9_AY (FLOAT)
- 参数描述：Axis of rotor 9 thrust vector, Y body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：``


1072. CA_ROTOR9_AZ (FLOAT)
- 名称：CA_ROTOR9_AZ (FLOAT)
- 参数描述：Axis of rotor 9 thrust vector, Z body axis component Comment: Only the direction is considered (the vector is normalized).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`-1.0`
- 单位：``


1073. CA_ROTOR9_CT (FLOAT)
- 名称：CA_ROTOR9_CT (FLOAT)
- 参数描述：Thrust coefficient of rotor 9 Comment: The thrust coefficient if defined as Thrust = CT * u^2, where u (with value between actuator minimum and maximum) is the output signal sent to the motor controller.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`6.5`
- 单位：``


1074. CA_ROTOR9_KM (FLOAT)
- 名称：CA_ROTOR9_KM (FLOAT)
- 参数描述：Moment coefficient of rotor 9 Comment: The moment coefficient if defined as Torque = KM * Thrust. Use a positive value for a rotor with CCW rotation. Use a negative value for a rotor with CW rotation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.01)`
- 默认值：`0.05`
- 单位：``


1075. CA_ROTOR9_PX (FLOAT)
- 名称：CA_ROTOR9_PX (FLOAT)
- 参数描述：Position of rotor 9 along X body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1076. CA_ROTOR9_PY (FLOAT)
- 名称：CA_ROTOR9_PY (FLOAT)
- 参数描述：Position of rotor 9 along Y body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1077. CA_ROTOR9_PZ (FLOAT)
- 名称：CA_ROTOR9_PZ (FLOAT)
- 参数描述：Position of rotor 9 along Z body axis relative to center of gravity
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-100, 100] (0.1)`
- 默认值：`0.0`
- 单位：`m`


1078. CA_ROTOR9_TILT (INT32)
- 名称：CA_ROTOR9_TILT (INT32)
- 参数描述：Rotor 9 tilt assignment Comment: If not set to None, this motor is tilted by the configured tilt servo. 参数对照:0: None 1: Tilt 1 2: Tilt 2 3: Tilt 3 4: Tilt 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1079. CA_ROTOR_COUNT (INT32)
- 名称：CA_ROTOR_COUNT (INT32)
- 参数描述：Total number of rotors  Values:0: 0 1: 1 2: 2 3: 3 4: 4 5: 5 6: 6 7: 7 8: 8 9: 9 10: 10 11: 11 12: 12
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1080. CA_R_REV (INT32)
- 名称：CA_R_REV (INT32)
- 参数描述：Bidirectional/Reversible motors Comment: Configure motors to be bidirectional/reversible. Note that the output driver needs to support this as well. Bitmask:0: Motor 1 1: Motor 2 2: Motor 3 3: Motor 4 4: Motor 5 5: Motor 6 6: Motor 7 7: Motor 8 8: Motor 9 9: Motor 10 10: Motor 11 11: Motor 12
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4095]`
- 默认值：`0`
- 单位：``


1081. CA_SP0_ANG0 (FLOAT)
- 名称：CA_SP0_ANG0 (FLOAT)
- 参数描述：Angle for swash plate servo 0 Comment: The angle is measured clockwise (as seen from top), with 0 pointing forwards (X axis).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360] (10)`
- 默认值：`0`
- 单位：`deg`


1082. CA_SP0_ANG1 (FLOAT)
- 名称：CA_SP0_ANG1 (FLOAT)
- 参数描述：Angle for swash plate servo 1 Comment: The angle is measured clockwise (as seen from top), with 0 pointing forwards (X axis).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360] (10)`
- 默认值：`140`
- 单位：`deg`


1083. CA_SP0_ANG2 (FLOAT)
- 名称：CA_SP0_ANG2 (FLOAT)
- 参数描述：Angle for swash plate servo 2 Comment: The angle is measured clockwise (as seen from top), with 0 pointing forwards (X axis).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360] (10)`
- 默认值：`220`
- 单位：`deg`


1084. CA_SP0_ANG3 (FLOAT)
- 名称：CA_SP0_ANG3 (FLOAT)
- 参数描述：Angle for swash plate servo 3 Comment: The angle is measured clockwise (as seen from top), with 0 pointing forwards (X axis).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360] (10)`
- 默认值：`0`
- 单位：`deg`


1085. CA_SP0_ARM_L0 (FLOAT)
- 名称：CA_SP0_ARM_L0 (FLOAT)
- 参数描述：Arm length for swash plate servo 0 Comment: This is relative to the other arm lengths.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.1)`
- 默认值：`1.0`
- 单位：``


1086. CA_SP0_ARM_L1 (FLOAT)
- 名称：CA_SP0_ARM_L1 (FLOAT)
- 参数描述：Arm length for swash plate servo 1 Comment: This is relative to the other arm lengths.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.1)`
- 默认值：`1.0`
- 单位：``


1087. CA_SP0_ARM_L2 (FLOAT)
- 名称：CA_SP0_ARM_L2 (FLOAT)
- 参数描述：Arm length for swash plate servo 2 Comment: This is relative to the other arm lengths.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.1)`
- 默认值：`1.0`
- 单位：``


1088. CA_SP0_ARM_L3 (FLOAT)
- 名称：CA_SP0_ARM_L3 (FLOAT)
- 参数描述：Arm length for swash plate servo 3 Comment: This is relative to the other arm lengths.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.1)`
- 默认值：`1.0`
- 单位：``


1089. CA_SP0_COUNT (INT32)
- 名称：CA_SP0_COUNT (INT32)
- 参数描述：Number of swash plates servos  Values:2: 2 3: 3 4: 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`3`
- 单位：``


1090. CA_SV0_SLEW (FLOAT)
- 名称：CA_SV0_SLEW (FLOAT)
- 参数描述：Servo 0 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1091. CA_SV1_SLEW (FLOAT)
- 名称：CA_SV1_SLEW (FLOAT)
- 参数描述：Servo 1 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1092. CA_SV2_SLEW (FLOAT)
- 名称：CA_SV2_SLEW (FLOAT)
- 参数描述：Servo 2 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1093. CA_SV3_SLEW (FLOAT)
- 名称：CA_SV3_SLEW (FLOAT)
- 参数描述：Servo 3 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1094. CA_SV4_SLEW (FLOAT)
- 名称：CA_SV4_SLEW (FLOAT)
- 参数描述：Servo 4 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1095. CA_SV5_SLEW (FLOAT)
- 名称：CA_SV5_SLEW (FLOAT)
- 参数描述：Servo 5 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1096. CA_SV6_SLEW (FLOAT)
- 名称：CA_SV6_SLEW (FLOAT)
- 参数描述：Servo 6 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1097. CA_SV7_SLEW (FLOAT)
- 名称：CA_SV7_SLEW (FLOAT)
- 参数描述：Servo 7 slew rate limit Comment: Minimum time allowed for the servo input signal to pass through the full output range. A value x means that the servo signal can only go from -1 to 1 in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.05)`
- 默认值：`0.0`
- 单位：``


1098. CA_SV_CS0_FLAP (FLOAT)
- 名称：CA_SV_CS0_FLAP (FLOAT)
- 参数描述：Control Surface 0 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1099. CA_SV_CS0_SPOIL (FLOAT)
- 名称：CA_SV_CS0_SPOIL (FLOAT)
- 参数描述：Control Surface 0 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1100. CA_SV_CS0_TRIM (FLOAT)
- 名称：CA_SV_CS0_TRIM (FLOAT)
- 参数描述：Control Surface 0 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1101. CA_SV_CS0_TRQ_P (FLOAT)
- 名称：CA_SV_CS0_TRQ_P (FLOAT)
- 参数描述：Control Surface 0 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1102. CA_SV_CS0_TRQ_R (FLOAT)
- 名称：CA_SV_CS0_TRQ_R (FLOAT)
- 参数描述：Control Surface 0 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1103. CA_SV_CS0_TRQ_Y (FLOAT)
- 名称：CA_SV_CS0_TRQ_Y (FLOAT)
- 参数描述：Control Surface 0 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1104. CA_SV_CS0_TYPE (INT32)
- 名称：CA_SV_CS0_TYPE (INT32)
- 参数描述：Control Surface 0 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1105. CA_SV_CS1_FLAP (FLOAT)
- 名称：CA_SV_CS1_FLAP (FLOAT)
- 参数描述：Control Surface 1 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1106. CA_SV_CS1_SPOIL (FLOAT)
- 名称：CA_SV_CS1_SPOIL (FLOAT)
- 参数描述：Control Surface 1 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1107. CA_SV_CS1_TRIM (FLOAT)
- 名称：CA_SV_CS1_TRIM (FLOAT)
- 参数描述：Control Surface 1 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1108. CA_SV_CS1_TRQ_P (FLOAT)
- 名称：CA_SV_CS1_TRQ_P (FLOAT)
- 参数描述：Control Surface 1 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1109. CA_SV_CS1_TRQ_R (FLOAT)
- 名称：CA_SV_CS1_TRQ_R (FLOAT)
- 参数描述：Control Surface 1 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1110. CA_SV_CS1_TRQ_Y (FLOAT)
- 名称：CA_SV_CS1_TRQ_Y (FLOAT)
- 参数描述：Control Surface 1 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1111. CA_SV_CS1_TYPE (INT32)
- 名称：CA_SV_CS1_TYPE (INT32)
- 参数描述：Control Surface 1 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1112. CA_SV_CS2_FLAP (FLOAT)
- 名称：CA_SV_CS2_FLAP (FLOAT)
- 参数描述：Control Surface 2 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1113. CA_SV_CS2_SPOIL (FLOAT)
- 名称：CA_SV_CS2_SPOIL (FLOAT)
- 参数描述：Control Surface 2 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1114. CA_SV_CS2_TRIM (FLOAT)
- 名称：CA_SV_CS2_TRIM (FLOAT)
- 参数描述：Control Surface 2 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1115. CA_SV_CS2_TRQ_P (FLOAT)
- 名称：CA_SV_CS2_TRQ_P (FLOAT)
- 参数描述：Control Surface 2 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1116. CA_SV_CS2_TRQ_R (FLOAT)
- 名称：CA_SV_CS2_TRQ_R (FLOAT)
- 参数描述：Control Surface 2 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1117. CA_SV_CS2_TRQ_Y (FLOAT)
- 名称：CA_SV_CS2_TRQ_Y (FLOAT)
- 参数描述：Control Surface 2 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1118. CA_SV_CS2_TYPE (INT32)
- 名称：CA_SV_CS2_TYPE (INT32)
- 参数描述：Control Surface 2 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1119. CA_SV_CS3_FLAP (FLOAT)
- 名称：CA_SV_CS3_FLAP (FLOAT)
- 参数描述：Control Surface 3 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1120. CA_SV_CS3_SPOIL (FLOAT)
- 名称：CA_SV_CS3_SPOIL (FLOAT)
- 参数描述：Control Surface 3 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1121. CA_SV_CS3_TRIM (FLOAT)
- 名称：CA_SV_CS3_TRIM (FLOAT)
- 参数描述：Control Surface 3 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1122. CA_SV_CS3_TRQ_P (FLOAT)
- 名称：CA_SV_CS3_TRQ_P (FLOAT)
- 参数描述：Control Surface 3 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1123. CA_SV_CS3_TRQ_R (FLOAT)
- 名称：CA_SV_CS3_TRQ_R (FLOAT)
- 参数描述：Control Surface 3 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1124. CA_SV_CS3_TRQ_Y (FLOAT)
- 名称：CA_SV_CS3_TRQ_Y (FLOAT)
- 参数描述：Control Surface 3 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1125. CA_SV_CS3_TYPE (INT32)
- 名称：CA_SV_CS3_TYPE (INT32)
- 参数描述：Control Surface 3 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1126. CA_SV_CS4_FLAP (FLOAT)
- 名称：CA_SV_CS4_FLAP (FLOAT)
- 参数描述：Control Surface 4 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1127. CA_SV_CS4_SPOIL (FLOAT)
- 名称：CA_SV_CS4_SPOIL (FLOAT)
- 参数描述：Control Surface 4 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1128. CA_SV_CS4_TRIM (FLOAT)
- 名称：CA_SV_CS4_TRIM (FLOAT)
- 参数描述：Control Surface 4 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1129. CA_SV_CS4_TRQ_P (FLOAT)
- 名称：CA_SV_CS4_TRQ_P (FLOAT)
- 参数描述：Control Surface 4 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1130. CA_SV_CS4_TRQ_R (FLOAT)
- 名称：CA_SV_CS4_TRQ_R (FLOAT)
- 参数描述：Control Surface 4 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1131. CA_SV_CS4_TRQ_Y (FLOAT)
- 名称：CA_SV_CS4_TRQ_Y (FLOAT)
- 参数描述：Control Surface 4 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1132. CA_SV_CS4_TYPE (INT32)
- 名称：CA_SV_CS4_TYPE (INT32)
- 参数描述：Control Surface 4 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1133. CA_SV_CS5_FLAP (FLOAT)
- 名称：CA_SV_CS5_FLAP (FLOAT)
- 参数描述：Control Surface 5 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1134. CA_SV_CS5_SPOIL (FLOAT)
- 名称：CA_SV_CS5_SPOIL (FLOAT)
- 参数描述：Control Surface 5 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1135. CA_SV_CS5_TRIM (FLOAT)
- 名称：CA_SV_CS5_TRIM (FLOAT)
- 参数描述：Control Surface 5 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1136. CA_SV_CS5_TRQ_P (FLOAT)
- 名称：CA_SV_CS5_TRQ_P (FLOAT)
- 参数描述：Control Surface 5 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1137. CA_SV_CS5_TRQ_R (FLOAT)
- 名称：CA_SV_CS5_TRQ_R (FLOAT)
- 参数描述：Control Surface 5 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1138. CA_SV_CS5_TRQ_Y (FLOAT)
- 名称：CA_SV_CS5_TRQ_Y (FLOAT)
- 参数描述：Control Surface 5 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1139. CA_SV_CS5_TYPE (INT32)
- 名称：CA_SV_CS5_TYPE (INT32)
- 参数描述：Control Surface 5 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1140. CA_SV_CS6_FLAP (FLOAT)
- 名称：CA_SV_CS6_FLAP (FLOAT)
- 参数描述：Control Surface 6 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1141. CA_SV_CS6_SPOIL (FLOAT)
- 名称：CA_SV_CS6_SPOIL (FLOAT)
- 参数描述：Control Surface 6 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1142. CA_SV_CS6_TRIM (FLOAT)
- 名称：CA_SV_CS6_TRIM (FLOAT)
- 参数描述：Control Surface 6 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1143. CA_SV_CS6_TRQ_P (FLOAT)
- 名称：CA_SV_CS6_TRQ_P (FLOAT)
- 参数描述：Control Surface 6 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1144. CA_SV_CS6_TRQ_R (FLOAT)
- 名称：CA_SV_CS6_TRQ_R (FLOAT)
- 参数描述：Control Surface 6 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1145. CA_SV_CS6_TRQ_Y (FLOAT)
- 名称：CA_SV_CS6_TRQ_Y (FLOAT)
- 参数描述：Control Surface 6 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1146. CA_SV_CS6_TYPE (INT32)
- 名称：CA_SV_CS6_TYPE (INT32)
- 参数描述：Control Surface 6 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1147. CA_SV_CS7_FLAP (FLOAT)
- 名称：CA_SV_CS7_FLAP (FLOAT)
- 参数描述：Control Surface 7 configuration as flap
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1148. CA_SV_CS7_SPOIL (FLOAT)
- 名称：CA_SV_CS7_SPOIL (FLOAT)
- 参数描述：Control Surface 7 configuration as spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0`
- 单位：``


1149. CA_SV_CS7_TRIM (FLOAT)
- 名称：CA_SV_CS7_TRIM (FLOAT)
- 参数描述：Control Surface 7 trim Comment: Can be used to add an offset to the servo control.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`0.0`
- 单位：``


1150. CA_SV_CS7_TRQ_P (FLOAT)
- 名称：CA_SV_CS7_TRQ_P (FLOAT)
- 参数描述：Control Surface 7 pitch torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1151. CA_SV_CS7_TRQ_R (FLOAT)
- 名称：CA_SV_CS7_TRQ_R (FLOAT)
- 参数描述：Control Surface 7 roll torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1152. CA_SV_CS7_TRQ_Y (FLOAT)
- 名称：CA_SV_CS7_TRQ_Y (FLOAT)
- 参数描述：Control Surface 7 yaw torque scaling
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：``


1153. CA_SV_CS7_TYPE (INT32)
- 名称：CA_SV_CS7_TYPE (INT32)
- 参数描述：Control Surface 7 type  Values:0: (Not set) 1: Left Aileron 2: Right Aileron 3: Elevator 4: Rudder 5: Left Elevon 6: Right Elevon 7: Left V-Tail 8: Right V-Tail 9: Left Flap 10: Right Flap 11: Airbrake 12: Custom 13: Left A-tail 14: Right A-tail 15: Single Channel Aileron 16: Steering Wheel 17: Left Spoiler 18: Right Spoiler
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1154. CA_SV_CS_COUNT (INT32)
- 名称：CA_SV_CS_COUNT (INT32)
- 参数描述：Total number of Control Surfaces  Values:0: 0 1: 1 2: 2 3: 3 4: 4 5: 5 6: 6 7: 7 8: 8
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1155. CA_SV_TL0_CT (INT32)
- 名称：CA_SV_TL0_CT (INT32)
- 参数描述：Tilt 0 is used for control Comment: Define if this servo is used for additional control. 参数对照:0: None 1: Yaw 2: Pitch 3: Yaw and Pitch
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1156. CA_SV_TL0_MAXA (FLOAT)
- 名称：CA_SV_TL0_MAXA (FLOAT)
- 参数描述：Tilt Servo 0 Tilt Angle at Maximum Comment: Defines the tilt angle when the servo is at the maximum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`90.0`
- 单位：`deg`


1157. CA_SV_TL0_MINA (FLOAT)
- 名称：CA_SV_TL0_MINA (FLOAT)
- 参数描述：Tilt Servo 0 Tilt Angle at Minimum Comment: Defines the tilt angle when the servo is at the minimum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`0.0`
- 单位：`deg`


1158. CA_SV_TL0_TD (INT32)
- 名称：CA_SV_TL0_TD (INT32)
- 参数描述：Tilt Servo 0 Tilt Direction Comment: Defines the direction the servo tilts towards when moving towards the maximum tilt angle. For example if the minimum tilt angle is -90, the maximum 90, and the direction 'Towards Front', the motor axis aligns with the XZ-plane, points towards -X at the minimum and +X at the maximum tilt. 参数对照:0: Towards Front 90: Towards Right
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 359]`
- 默认值：`0`
- 单位：``


1159. CA_SV_TL1_CT (INT32)
- 名称：CA_SV_TL1_CT (INT32)
- 参数描述：Tilt 1 is used for control Comment: Define if this servo is used for additional control. 参数对照:0: None 1: Yaw 2: Pitch 3: Yaw and Pitch
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1160. CA_SV_TL1_MAXA (FLOAT)
- 名称：CA_SV_TL1_MAXA (FLOAT)
- 参数描述：Tilt Servo 1 Tilt Angle at Maximum Comment: Defines the tilt angle when the servo is at the maximum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`90.0`
- 单位：`deg`


1161. CA_SV_TL1_MINA (FLOAT)
- 名称：CA_SV_TL1_MINA (FLOAT)
- 参数描述：Tilt Servo 1 Tilt Angle at Minimum Comment: Defines the tilt angle when the servo is at the minimum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`0.0`
- 单位：`deg`


1162. CA_SV_TL1_TD (INT32)
- 名称：CA_SV_TL1_TD (INT32)
- 参数描述：Tilt Servo 1 Tilt Direction Comment: Defines the direction the servo tilts towards when moving towards the maximum tilt angle. For example if the minimum tilt angle is -90, the maximum 90, and the direction 'Towards Front', the motor axis aligns with the XZ-plane, points towards -X at the minimum and +X at the maximum tilt. 参数对照:0: Towards Front 90: Towards Right
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 359]`
- 默认值：`0`
- 单位：``


1163. CA_SV_TL2_CT (INT32)
- 名称：CA_SV_TL2_CT (INT32)
- 参数描述：Tilt 2 is used for control Comment: Define if this servo is used for additional control. 参数对照:0: None 1: Yaw 2: Pitch 3: Yaw and Pitch
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1164. CA_SV_TL2_MAXA (FLOAT)
- 名称：CA_SV_TL2_MAXA (FLOAT)
- 参数描述：Tilt Servo 2 Tilt Angle at Maximum Comment: Defines the tilt angle when the servo is at the maximum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`90.0`
- 单位：`deg`


1165. CA_SV_TL2_MINA (FLOAT)
- 名称：CA_SV_TL2_MINA (FLOAT)
- 参数描述：Tilt Servo 2 Tilt Angle at Minimum Comment: Defines the tilt angle when the servo is at the minimum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`0.0`
- 单位：`deg`


1166. CA_SV_TL2_TD (INT32)
- 名称：CA_SV_TL2_TD (INT32)
- 参数描述：Tilt Servo 2 Tilt Direction Comment: Defines the direction the servo tilts towards when moving towards the maximum tilt angle. For example if the minimum tilt angle is -90, the maximum 90, and the direction 'Towards Front', the motor axis aligns with the XZ-plane, points towards -X at the minimum and +X at the maximum tilt. 参数对照:0: Towards Front 90: Towards Right
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 359]`
- 默认值：`0`
- 单位：``


1167. CA_SV_TL3_CT (INT32)
- 名称：CA_SV_TL3_CT (INT32)
- 参数描述：Tilt 3 is used for control Comment: Define if this servo is used for additional control. 参数对照:0: None 1: Yaw 2: Pitch 3: Yaw and Pitch
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1168. CA_SV_TL3_MAXA (FLOAT)
- 名称：CA_SV_TL3_MAXA (FLOAT)
- 参数描述：Tilt Servo 3 Tilt Angle at Maximum Comment: Defines the tilt angle when the servo is at the maximum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`90.0`
- 单位：`deg`


1169. CA_SV_TL3_MINA (FLOAT)
- 名称：CA_SV_TL3_MINA (FLOAT)
- 参数描述：Tilt Servo 3 Tilt Angle at Minimum Comment: Defines the tilt angle when the servo is at the minimum. An angle of zero means upwards.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`0.0`
- 单位：`deg`


1170. CA_SV_TL3_TD (INT32)
- 名称：CA_SV_TL3_TD (INT32)
- 参数描述：Tilt Servo 3 Tilt Direction Comment: Defines the direction the servo tilts towards when moving towards the maximum tilt angle. For example if the minimum tilt angle is -90, the maximum 90, and the direction 'Towards Front', the motor axis aligns with the XZ-plane, points towards -X at the minimum and +X at the maximum tilt. 参数对照:0: Towards Front 90: Towards Right
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 359]`
- 默认值：`0`
- 单位：``


1171. CA_SV_TL_COUNT (INT32)
- 名称：CA_SV_TL_COUNT (INT32)
- 参数描述：Total number of Tilt Servos  Values:0: 0 1: 1 2: 2 3: 3 4: 4
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1172. HTE_ACC_GATE (FLOAT)
- 名称：HTE_ACC_GATE (FLOAT)
- 参数描述：Gate size for acceleration fusion Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10.0]`
- 默认值：`3.0`
- 单位：`SD`


1173. HTE_HT_ERR_INIT (FLOAT)
- 名称：HTE_HT_ERR_INIT (FLOAT)
- 参数描述：1-sigma initial hover thrust uncertainty Comment: Sets the number of standard deviations used by the innovation consistency test.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0]`
- 默认值：`0.1`
- 单位：`normalized_thrust`


1174. HTE_HT_NOISE (FLOAT)
- 名称：HTE_HT_NOISE (FLOAT)
- 参数描述：Hover thrust process noise Comment: Reduce to make the hover thrust estimate more stable, increase if the real hover thrust is expected to change quickly over time.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0001, 1.0]`
- 默认值：`0.0036`
- 单位：`normalized_thrust/s`


1175. HTE_THR_RANGE (FLOAT)
- 名称：HTE_THR_RANGE (FLOAT)
- 参数描述：Max deviation from MPC_THR_HOVER Comment: Defines the range of the hover thrust estimate around MPC_THR_HOVER. A value of 0.2 with MPC_THR_HOVER at 0.5 results in a range of [0.3, 0.7]. Set to a large value if the vehicle operates in varying physical conditions that affect the required hover thrust strongly (e.g. differently sized payloads).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 0.4]`
- 默认值：`0.2`
- 单位：`normalized_thrust`


1176. HTE_VXY_THR (FLOAT)
- 名称：HTE_VXY_THR (FLOAT)
- 参数描述：Horizontal velocity threshold for sensitivity reduction Comment: Above this speed, the measurement noise is linearly increased to reduce the sensitivity of the estimator from biased measurement. Set to a low value on vehicles with large lifting surfaces.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 20.0]`
- 默认值：`10.0`
- 单位：`m/s`


1177. HTE_VZ_THR (FLOAT)
- 名称：HTE_VZ_THR (FLOAT)
- 参数描述：Vertical velocity threshold for sensitivity reduction Comment: Above this speed, the measurement noise is linearly increased to reduce the sensitivity of the estimator from biased measurement. Set to a low value on vehicles affected by air drag when climbing or descending.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 10.0]`
- 默认值：`2.0`
- 单位：`m/s`


1178. ISBD_CONFIG (INT32)
- 名称：ISBD_CONFIG (INT32)
- 参数描述：Serial Configuration for Iridium (with MAVLink) Comment: Configure on which serial port to run Iridium (with MAVLink). 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1179. ISBD_READ_INT (INT32)
- 名称：ISBD_READ_INT (INT32)
- 参数描述：Satellite radio read interval. Only required to be nonzero if data is not sent using a ring call
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 5000]`
- 默认值：`0`
- 单位：`s`


1180. ISBD_SBD_TIMEOUT (INT32)
- 名称：ISBD_SBD_TIMEOUT (INT32)
- 参数描述：Iridium SBD session timeout
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 300]`
- 默认值：`60`
- 单位：`s`


1181. ISBD_STACK_TIME (INT32)
- 名称：ISBD_STACK_TIME (INT32)
- 参数描述：Time the Iridium driver will wait for additional mavlink messages to combine them into one SBD message Comment: Value 0 turns the functionality off
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 500]`
- 默认值：`0`
- 单位：`ms`


1182. LNDFW_AIRSPD_MAX (FLOAT)
- 名称：LNDFW_AIRSPD_MAX (FLOAT)
- 参数描述：Fixed-wing land detector: Max airspeed Comment: Maximum airspeed allowed in the landed state
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 20]`
- 默认值：`6.00`
- 单位：`m/s`


1183. LNDFW_TRIG_TIME (FLOAT)
- 名称：LNDFW_TRIG_TIME (FLOAT)
- 参数描述：Fixed-wing land detection trigger time Comment: Time the land conditions (speeds and acceleration) have to be satisfied to detect a landing. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, ?]`
- 默认值：`2.`
- 单位：`s`


1184. LNDFW_VEL_XY_MAX (FLOAT)
- 名称：LNDFW_VEL_XY_MAX (FLOAT)
- 参数描述：Fixed-wing land detector: Max horizontal velocity threshold Comment: Maximum horizontal velocity allowed in the landed state. A factor of 0.7 is applied in case of airspeed-less flying (either because no sensor is present or sensor data got invalid in flight).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 10]`
- 默认值：`5.0`
- 单位：`m/s`


1185. LNDFW_VEL_Z_MAX (FLOAT)
- 名称：LNDFW_VEL_Z_MAX (FLOAT)
- 参数描述：Fixed-wing land detector: Max vertiacal velocity threshold Comment: Maximum vertical velocity allowed in the landed state.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 20]`
- 默认值：`1.0`
- 单位：`m/s`


1186. LNDFW_XYACC_MAX (FLOAT)
- 名称：LNDFW_XYACC_MAX (FLOAT)
- 参数描述：Fixed-wing land detector: Max horizontal acceleration Comment: Maximum horizontal (x,y body axes) acceleration allowed in the landed state
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15]`
- 默认值：`8.0`
- 单位：`m/s^2`


1187. LNDMC_ALT_GND (FLOAT)
- 名称：LNDMC_ALT_GND (FLOAT)
- 参数描述：Ground effect altitude for multicopters Comment: The height above ground below which ground effect creates barometric altitude errors. A negative value indicates no ground effect.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, ?]`
- 默认值：`2.`
- 单位：`m`


1188. LNDMC_ALT_MAX (FLOAT)
- 名称：LNDMC_ALT_MAX (FLOAT)
- 参数描述：Maximum altitude for multicopters Comment: The system will obey this limit as a hard altitude limit. This setting will be consolidated with the GF_MAX_VER_DIST parameter. A negative value indicates no altitude limitation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 10000]`
- 默认值：`-1.0`
- 单位：`m`


1189. LNDMC_ROT_MAX (FLOAT)
- 名称：LNDMC_ROT_MAX (FLOAT)
- 参数描述：Multicopter max rotation Comment: Maximum allowed angular velocity around each axis allowed in the landed state.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`20.0`
- 单位：`deg/s`


1190. LNDMC_TRIG_TIME (FLOAT)
- 名称：LNDMC_TRIG_TIME (FLOAT)
- 参数描述：Multicopter land detection trigger time Comment: Total time it takes to go through all three land detection stages: ground contact, maybe landed, landed when all necessary conditions are constantly met.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10.0]`
- 默认值：`1.0`
- 单位：`s`


1191. LNDMC_XY_VEL_MAX (FLOAT)
- 名称：LNDMC_XY_VEL_MAX (FLOAT)
- 参数描述：Multicopter max horizontal velocity Comment: Maximum horizontal velocity allowed in the landed state
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1.5`
- 单位：`m/s`


1192. LNDMC_Z_VEL_MAX (FLOAT)
- 名称：LNDMC_Z_VEL_MAX (FLOAT)
- 参数描述：Multicopter vertical velocity threshold Comment: Vertical velocity threshold to detect landing. Has to be set lower than the expected minimal speed for landing, which is either MPC_LAND_SPEED or MPC_LAND_CRWL. This is enforced by an automatic check.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0.25`
- 单位：`m/s`


1193. LND_FLIGHT_T_HI (INT32)
- 名称：LND_FLIGHT_T_HI (INT32)
- 参数描述：Total flight time in microseconds Comment: Total flight time of this autopilot. Higher 32 bits of the value. Flight time in microseconds = (LND_FLIGHT_T_HI << 32) | LND_FLIGHT_T_LO.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0`
- 单位：``


1194. LND_FLIGHT_T_LO (INT32)
- 名称：LND_FLIGHT_T_LO (INT32)
- 参数描述：Total flight time in microseconds Comment: Total flight time of this autopilot. Lower 32 bits of the value. Flight time in microseconds = (LND_FLIGHT_T_HI << 32) | LND_FLIGHT_T_LO.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0`
- 单位：``


1195. LTEST_ACC_UNC (FLOAT)
- 名称：LTEST_ACC_UNC (FLOAT)
- 参数描述：Acceleration uncertainty Comment: Variance of acceleration measurement used for landing target position prediction. Higher values results in tighter following of the measurements and more lenient outlier rejection
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`10.0`
- 单位：`(m/s^2)^2`


1196. LTEST_MEAS_UNC (FLOAT)
- 名称：LTEST_MEAS_UNC (FLOAT)
- 参数描述：Landing target measurement uncertainty Comment: Variance of the landing target measurement from the driver. Higher values result in less aggressive following of the measurement and a smoother output as well as fewer rejected measurements.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.005`
- 单位：`tan(rad)^2`


1197. LTEST_MODE (INT32)
- 名称：LTEST_MODE (INT32)
- 参数描述：Landing target mode Comment: Configure the mode of the landing target. Depending on the mode, the landing target observations are used differently to aid position estimation. Mode Moving:     The landing target may be moving around while in the field of view of the vehicle. Landing target measurements are not used to aid positioning. Mode Stationary: The landing target is stationary. Measured velocity w.r.t. the landing target is used to aid velocity estimation. 参数对照:0: Moving 1: Stationary
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1198. LTEST_POS_UNC_IN (FLOAT)
- 名称：LTEST_POS_UNC_IN (FLOAT)
- 参数描述：Initial landing target position uncertainty Comment: Initial variance of the relative landing target position in x and y direction
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.001, ?]`
- 默认值：`0.1`
- 单位：`m^2`


1199. LTEST_SCALE_X (FLOAT)
- 名称：LTEST_SCALE_X (FLOAT)
- 参数描述：Scale factor for sensor measurements in sensor x axis Comment: Landing target x measurements are scaled by this factor before being used
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`1.0`
- 单位：``


1200. LTEST_SCALE_Y (FLOAT)
- 名称：LTEST_SCALE_Y (FLOAT)
- 参数描述：Scale factor for sensor measurements in sensor y axis Comment: Landing target y measurements are scaled by this factor before being used
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, ?]`
- 默认值：`1.0`
- 单位：``


1201. LTEST_SENS_POS_X (FLOAT)
- 名称：LTEST_SENS_POS_X (FLOAT)
- 参数描述：X Position of IRLOCK in body frame (forward)    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


1202. LTEST_SENS_POS_Y (FLOAT)
- 名称：LTEST_SENS_POS_Y (FLOAT)
- 参数描述：Y Position of IRLOCK in body frame (right)    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


1203. LTEST_SENS_POS_Z (FLOAT)
- 名称：LTEST_SENS_POS_Z (FLOAT)
- 参数描述：Z Position of IRLOCK in body frame (downward)    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0.0`
- 单位：`m`


1204. LTEST_SENS_ROT (INT32)
- 名称：LTEST_SENS_ROT (INT32)
- 参数描述：Rotation of IRLOCK sensor relative to airframe Comment: Default orientation of Yaw 90° 参数对照:0: No rotation 1: Yaw 45° 2: Yaw 90° 3: Yaw 135° 4: Yaw 180° 5: Yaw 225° 6: Yaw 270° 7: Yaw 315° Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 40]`
- 默认值：`2`
- 单位：``


1205. LTEST_VEL_UNC_IN (FLOAT)
- 名称：LTEST_VEL_UNC_IN (FLOAT)
- 参数描述：Initial landing target velocity uncertainty Comment: Initial variance of the relative landing target velocity in x and y directions
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.001, ?]`
- 默认值：`0.1`
- 单位：`(m/s)^2`


1206. LPE_ACC_XY (FLOAT)
- 名称：LPE_ACC_XY (FLOAT)
- 参数描述：Accelerometer xy noise density Comment: Data sheet noise density = 150ug/sqrt(Hz) = 0.0015 m/s^2/sqrt(Hz) Larger than data sheet to account for tilt error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.00001, 2]`
- 默认值：`0.012`
- 单位：`m/s^2/sqrt(Hz)`


1207. LPE_ACC_Z (FLOAT)
- 名称：LPE_ACC_Z (FLOAT)
- 参数描述：Accelerometer z noise density Comment: Data sheet noise density = 150ug/sqrt(Hz) = 0.0015 m/s^2/sqrt(Hz)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.00001, 2]`
- 默认值：`0.02`
- 单位：`m/s^2/sqrt(Hz)`


1208. LPE_BAR_Z (FLOAT)
- 名称：LPE_BAR_Z (FLOAT)
- 参数描述：Barometric presssure altitude z standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 100]`
- 默认值：`3.0`
- 单位：`m`


1209. LPE_EPH_MAX (FLOAT)
- 名称：LPE_EPH_MAX (FLOAT)
- 参数描述：Max EPH allowed for GPS initialization
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 5.0]`
- 默认值：`3.0`
- 单位：`m`


1210. LPE_EPV_MAX (FLOAT)
- 名称：LPE_EPV_MAX (FLOAT)
- 参数描述：Max EPV allowed for GPS initialization
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 5.0]`
- 默认值：`5.0`
- 单位：`m`


1211. LPE_FAKE_ORIGIN (INT32)
- 名称：LPE_FAKE_ORIGIN (INT32)
- 参数描述：Enable publishing of a fake global position (e.g for AUTO missions using Optical Flow) Comment: By initializing the estimator to the LPE_LAT/LON parameters when global information is unavailable
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1212. LPE_FGYRO_HP (FLOAT)
- 名称：LPE_FGYRO_HP (FLOAT)
- 参数描述：Flow gyro high pass filter cut off frequency
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0.001`
- 单位：`Hz`


1213. LPE_FLW_OFF_Z (FLOAT)
- 名称：LPE_FLW_OFF_Z (FLOAT)
- 参数描述：Optical flow z offset from center
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1]`
- 默认值：`0.0`
- 单位：`m`


1214. LPE_FLW_QMIN (INT32)
- 名称：LPE_FLW_QMIN (INT32)
- 参数描述：Optical flow minimum quality threshold
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`150`
- 单位：``


1215. LPE_FLW_R (FLOAT)
- 名称：LPE_FLW_R (FLOAT)
- 参数描述：Optical flow rotation (roll/pitch) noise gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10.0]`
- 默认值：`7.0`
- 单位：`m/s/rad`


1216. LPE_FLW_RR (FLOAT)
- 名称：LPE_FLW_RR (FLOAT)
- 参数描述：Optical flow angular velocity noise gain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10.0]`
- 默认值：`7.0`
- 单位：`m/rad`


1217. LPE_FLW_SCALE (FLOAT)
- 名称：LPE_FLW_SCALE (FLOAT)
- 参数描述：Optical flow scale
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10.0]`
- 默认值：`1.3`
- 单位：`m`


1218. LPE_FUSION (INT32)
- 名称：LPE_FUSION (INT32)
- 参数描述：Integer bitmask controlling data fusion Comment: Set bits in the following positions to enable: 0 : Set to true to fuse GPS data if available, also requires GPS for altitude init 1 : Set to true to fuse optical flow data if available 2 : Set to true to fuse vision position 3 : Set to true to enable landing target 4 : Set to true to fuse land detector 5 : Set to true to publish AGL as local position down component 6 : Set to true to enable flow gyro compensation 7 : Set to true to enable baro fusion default (145 - GPS, baro, land detector) Bitmask:0: fuse GPS, requires GPS for alt. init 1: fuse optical flow 2: fuse vision position 3: fuse landing target 4: fuse land detector 5: pub agl as lpos down 6: flow gyro compensation 7: fuse baro
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 255]`
- 默认值：`145`
- 单位：``


1219. LPE_GPS_DELAY (FLOAT)
- 名称：LPE_GPS_DELAY (FLOAT)
- 参数描述：GPS delay compensaton
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.4]`
- 默认值：`0.29`
- 单位：`s`


1220. LPE_GPS_VXY (FLOAT)
- 名称：LPE_GPS_VXY (FLOAT)
- 参数描述：GPS xy velocity standard deviation Comment: EPV used if greater than this value.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 2]`
- 默认值：`0.25`
- 单位：`m/s`


1221. LPE_GPS_VZ (FLOAT)
- 名称：LPE_GPS_VZ (FLOAT)
- 参数描述：GPS z velocity standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 2]`
- 默认值：`0.25`
- 单位：`m/s`


1222. LPE_GPS_XY (FLOAT)
- 名称：LPE_GPS_XY (FLOAT)
- 参数描述：Minimum GPS xy standard deviation, uses reported EPH if greater
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 5]`
- 默认值：`1.0`
- 单位：`m`


1223. LPE_GPS_Z (FLOAT)
- 名称：LPE_GPS_Z (FLOAT)
- 参数描述：Minimum GPS z standard deviation, uses reported EPV if greater
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 200]`
- 默认值：`3.0`
- 单位：`m`


1224. LPE_LAND_VXY (FLOAT)
- 名称：LPE_LAND_VXY (FLOAT)
- 参数描述：Land detector xy velocity standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 10.0]`
- 默认值：`0.05`
- 单位：`m/s`


1225. LPE_LAND_Z (FLOAT)
- 名称：LPE_LAND_Z (FLOAT)
- 参数描述：Land detector z standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.001, 10.0]`
- 默认值：`0.03`
- 单位：`m`


1226. LPE_LAT (FLOAT)
- 名称：LPE_LAT (FLOAT)
- 参数描述：Local origin latitude for nav w/o GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90, 90]`
- 默认值：`47.397742`
- 单位：`deg`


1227. LPE_LDR_OFF_Z (FLOAT)
- 名称：LPE_LDR_OFF_Z (FLOAT)
- 参数描述：Lidar z offset from center of vehicle +down
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1]`
- 默认值：`0.00`
- 单位：`m`


1228. LPE_LDR_Z (FLOAT)
- 名称：LPE_LDR_Z (FLOAT)
- 参数描述：Lidar z standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1]`
- 默认值：`0.03`
- 单位：`m`


1229. LPE_LON (FLOAT)
- 名称：LPE_LON (FLOAT)
- 参数描述：Local origin longitude for nav w/o GPS
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-180, 180]`
- 默认值：`8.545594`
- 单位：`deg`


1230. LPE_LT_COV (FLOAT)
- 名称：LPE_LT_COV (FLOAT)
- 参数描述：Minimum landing target standard covariance, uses reported covariance if greater
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10]`
- 默认值：`0.0001`
- 单位：`m^2`


1231. LPE_PN_B (FLOAT)
- 名称：LPE_PN_B (FLOAT)
- 参数描述：Accel bias propagation noise density
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`1e-3`
- 单位：`m/s^3/sqrt(Hz)`


1232. LPE_PN_P (FLOAT)
- 名称：LPE_PN_P (FLOAT)
- 参数描述：Position propagation noise density Comment: Increase to trust measurements more. Decrease to trust model more.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.1`
- 单位：`m/s/sqrt(Hz)`


1233. LPE_PN_T (FLOAT)
- 名称：LPE_PN_T (FLOAT)
- 参数描述：Terrain random walk noise density, hilly/outdoor (0.1), flat/Indoor (0.001)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.001`
- 单位：`m/s/sqrt(Hz)`


1234. LPE_PN_V (FLOAT)
- 名称：LPE_PN_V (FLOAT)
- 参数描述：Velocity propagation noise density Comment: Increase to trust measurements more. Decrease to trust model more.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.1`
- 单位：`m/s^2/sqrt(Hz)`


1235. LPE_SNR_OFF_Z (FLOAT)
- 名称：LPE_SNR_OFF_Z (FLOAT)
- 参数描述：Sonar z offset from center of vehicle +down
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1]`
- 默认值：`0.00`
- 单位：`m`


1236. LPE_SNR_Z (FLOAT)
- 名称：LPE_SNR_Z (FLOAT)
- 参数描述：Sonar z standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1]`
- 默认值：`0.05`
- 单位：`m`


1237. LPE_T_MAX_GRADE (FLOAT)
- 名称：LPE_T_MAX_GRADE (FLOAT)
- 参数描述：Terrain maximum percent grade, hilly/outdoor (100 = 45 deg), flat/Indoor (0 = 0 deg) Comment: Used to calculate increased terrain random walk nosie due to movement.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100]`
- 默认值：`1.0`
- 单位：`%`


1238. LPE_VIC_P (FLOAT)
- 名称：LPE_VIC_P (FLOAT)
- 参数描述：Vicon position standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0001, 1]`
- 默认值：`0.001`
- 单位：`m`


1239. LPE_VIS_DELAY (FLOAT)
- 名称：LPE_VIS_DELAY (FLOAT)
- 参数描述：Vision delay compensation Comment: Set to zero to enable automatic compensation from measurement timestamps
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.1]`
- 默认值：`0.1`
- 单位：`s`


1240. LPE_VIS_XY (FLOAT)
- 名称：LPE_VIS_XY (FLOAT)
- 参数描述：Vision xy standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1]`
- 默认值：`0.1`
- 单位：`m`


1241. LPE_VIS_Z (FLOAT)
- 名称：LPE_VIS_Z (FLOAT)
- 参数描述：Vision z standard deviation
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 100]`
- 默认值：`0.5`
- 单位：`m`


1242. LPE_VXY_PUB (FLOAT)
- 名称：LPE_VXY_PUB (FLOAT)
- 参数描述：Required velocity xy standard deviation to publish position
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 1.0]`
- 默认值：`0.3`
- 单位：`m/s`


1243. LPE_X_LP (FLOAT)
- 名称：LPE_X_LP (FLOAT)
- 参数描述：Cut frequency for state publication
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[5, 1000]`
- 默认值：`5.0`
- 单位：`Hz`


1244. LPE_Z_PUB (FLOAT)
- 名称：LPE_Z_PUB (FLOAT)
- 参数描述：Required z standard deviation to publish altitude/ terrain
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.3, 5.0]`
- 默认值：`1.0`
- 单位：`m`


1245. MAV_0_BROADCAST (INT32)
- 名称：MAV_0_BROADCAST (INT32)
- 参数描述：Broadcast heartbeats on local network for MAVLink instance 0 Comment: This allows a ground control station to automatically find the drone on the local network. 参数对照:0: Never broadcast 1: Always broadcast 2: Only multicast
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1246. MAV_0_CONFIG (INT32)
- 名称：MAV_0_CONFIG (INT32)
- 参数描述：Serial Configuration for MAVLink (instance 0) Comment: Configure on which serial port to run MAVLink. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 1000: Ethernet Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`101`
- 单位：``


1247. MAV_0_FLOW_CTRL (INT32)
- 名称：MAV_0_FLOW_CTRL (INT32)
- 参数描述：Enable serial flow control for instance 0 Comment: This is used to force flow control on or off for the the mavlink instance. By default it is auto detected. Use when auto detection fails. 参数对照:0: Force off 1: Force on 2: Auto-detected Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


1248. MAV_0_FORWARD (INT32)
- 名称：MAV_0_FORWARD (INT32)
- 参数描述：Enable MAVLink Message forwarding for instance 0 Comment: If enabled, forward incoming MAVLink messages to other MAVLink ports if the message is either broadcast or the target is not the autopilot. This allows for example a GCS to talk to a camera that is connected to the autopilot via MAVLink (on a different link than the GCS). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1249. MAV_0_MODE (INT32)
- 名称：MAV_0_MODE (INT32)
- 参数描述：MAVLink Mode for instance 0 Comment: The MAVLink Mode defines the set of streamed messages (for example the vehicle's attitude) and their sending rates. 参数对照:0: Normal 1: Custom 2: Onboard 3: OSD 4: Magic 5: Config 7: Minimal 8: External Vision 10: Gimbal 11: Onboard Low Bandwidth 12: uAvionix Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1250. MAV_0_RADIO_CTL (INT32)
- 名称：MAV_0_RADIO_CTL (INT32)
- 参数描述：Enable software throttling of mavlink on instance 0 Comment: If enabled, MAVLink messages will be throttled according to `txbuf` field reported by radio_status. Requires a radio to send the mavlink message RADIO_STATUS. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1251. MAV_0_RATE (INT32)
- 名称：MAV_0_RATE (INT32)
- 参数描述：Maximum MAVLink sending rate for instance 0 Comment: Configure the maximum sending rate for the MAVLink streams in Bytes/sec. If the configured streams exceed the maximum rate, the sending rate of each stream is automatically decreased. If this is set to 0 a value of half of the theoretical maximum bandwidth is used. This corresponds to baudrate/20 Bytes/s (baudrate/10 = maximum data rate on 8N1-configured links). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`1200`
- 单位：`B/s`


1252. MAV_0_REMOTE_PRT (INT32)
- 名称：MAV_0_REMOTE_PRT (INT32)
- 参数描述：MAVLink Remote Port for instance 0 Comment: If ethernet enabled and selected as configuration for MAVLink instance 0, selected remote port will be set and used in MAVLink instance 0. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`14550`
- 单位：``


1253. MAV_0_UDP_PRT (INT32)
- 名称：MAV_0_UDP_PRT (INT32)
- 参数描述：MAVLink Network Port for instance 0 Comment: If ethernet enabled and selected as configuration for MAVLink instance 0, selected udp port will be set and used in MAVLink instance 0. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`14556`
- 单位：``


1254. MAV_1_BROADCAST (INT32)
- 名称：MAV_1_BROADCAST (INT32)
- 参数描述：Broadcast heartbeats on local network for MAVLink instance 1 Comment: This allows a ground control station to automatically find the drone on the local network. 参数对照:0: Never broadcast 1: Always broadcast 2: Only multicast
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1255. MAV_1_CONFIG (INT32)
- 名称：MAV_1_CONFIG (INT32)
- 参数描述：Serial Configuration for MAVLink (instance 1) Comment: Configure on which serial port to run MAVLink. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 1000: Ethernet Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1256. MAV_1_FLOW_CTRL (INT32)
- 名称：MAV_1_FLOW_CTRL (INT32)
- 参数描述：Enable serial flow control for instance 1 Comment: This is used to force flow control on or off for the the mavlink instance. By default it is auto detected. Use when auto detection fails. 参数对照:0: Force off 1: Force on 2: Auto-detected Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


1257. MAV_1_FORWARD (INT32)
- 名称：MAV_1_FORWARD (INT32)
- 参数描述：Enable MAVLink Message forwarding for instance 1 Comment: If enabled, forward incoming MAVLink messages to other MAVLink ports if the message is either broadcast or the target is not the autopilot. This allows for example a GCS to talk to a camera that is connected to the autopilot via MAVLink (on a different link than the GCS). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1258. MAV_1_MODE (INT32)
- 名称：MAV_1_MODE (INT32)
- 参数描述：MAVLink Mode for instance 1 Comment: The MAVLink Mode defines the set of streamed messages (for example the vehicle's attitude) and their sending rates. 参数对照:0: Normal 1: Custom 2: Onboard 3: OSD 4: Magic 5: Config 7: Minimal 8: External Vision 10: Gimbal 11: Onboard Low Bandwidth 12: uAvionix Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


1259. MAV_1_RADIO_CTL (INT32)
- 名称：MAV_1_RADIO_CTL (INT32)
- 参数描述：Enable software throttling of mavlink on instance 1 Comment: If enabled, MAVLink messages will be throttled according to `txbuf` field reported by radio_status. Requires a radio to send the mavlink message RADIO_STATUS. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1260. MAV_1_RATE (INT32)
- 名称：MAV_1_RATE (INT32)
- 参数描述：Maximum MAVLink sending rate for instance 1 Comment: Configure the maximum sending rate for the MAVLink streams in Bytes/sec. If the configured streams exceed the maximum rate, the sending rate of each stream is automatically decreased. If this is set to 0 a value of half of the theoretical maximum bandwidth is used. This corresponds to baudrate/20 Bytes/s (baudrate/10 = maximum data rate on 8N1-configured links). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0`
- 单位：`B/s`


1261. MAV_1_REMOTE_PRT (INT32)
- 名称：MAV_1_REMOTE_PRT (INT32)
- 参数描述：MAVLink Remote Port for instance 1 Comment: If ethernet enabled and selected as configuration for MAVLink instance 1, selected remote port will be set and used in MAVLink instance 1. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1262. MAV_1_UDP_PRT (INT32)
- 名称：MAV_1_UDP_PRT (INT32)
- 参数描述：MAVLink Network Port for instance 1 Comment: If ethernet enabled and selected as configuration for MAVLink instance 1, selected udp port will be set and used in MAVLink instance 1. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1263. MAV_2_BROADCAST (INT32)
- 名称：MAV_2_BROADCAST (INT32)
- 参数描述：Broadcast heartbeats on local network for MAVLink instance 2 Comment: This allows a ground control station to automatically find the drone on the local network. 参数对照:0: Never broadcast 1: Always broadcast 2: Only multicast
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1264. MAV_2_CONFIG (INT32)
- 名称：MAV_2_CONFIG (INT32)
- 参数描述：Serial Configuration for MAVLink (instance 2) Comment: Configure on which serial port to run MAVLink. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 1000: Ethernet Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1265. MAV_2_FLOW_CTRL (INT32)
- 名称：MAV_2_FLOW_CTRL (INT32)
- 参数描述：Enable serial flow control for instance 2 Comment: This is used to force flow control on or off for the the mavlink instance. By default it is auto detected. Use when auto detection fails. 参数对照:0: Force off 1: Force on 2: Auto-detected Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`2`
- 单位：``


1266. MAV_2_FORWARD (INT32)
- 名称：MAV_2_FORWARD (INT32)
- 参数描述：Enable MAVLink Message forwarding for instance 2 Comment: If enabled, forward incoming MAVLink messages to other MAVLink ports if the message is either broadcast or the target is not the autopilot. This allows for example a GCS to talk to a camera that is connected to the autopilot via MAVLink (on a different link than the GCS). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1267. MAV_2_MODE (INT32)
- 名称：MAV_2_MODE (INT32)
- 参数描述：MAVLink Mode for instance 2 Comment: The MAVLink Mode defines the set of streamed messages (for example the vehicle's attitude) and their sending rates. 参数对照:0: Normal 1: Custom 2: Onboard 3: OSD 4: Magic 5: Config 7: Minimal 8: External Vision 10: Gimbal 11: Onboard Low Bandwidth 12: uAvionix Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1268. MAV_2_RADIO_CTL (INT32)
- 名称：MAV_2_RADIO_CTL (INT32)
- 参数描述：Enable software throttling of mavlink on instance 2 Comment: If enabled, MAVLink messages will be throttled according to `txbuf` field reported by radio_status. Requires a radio to send the mavlink message RADIO_STATUS. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1269. MAV_2_RATE (INT32)
- 名称：MAV_2_RATE (INT32)
- 参数描述：Maximum MAVLink sending rate for instance 2 Comment: Configure the maximum sending rate for the MAVLink streams in Bytes/sec. If the configured streams exceed the maximum rate, the sending rate of each stream is automatically decreased. If this is set to 0 a value of half of the theoretical maximum bandwidth is used. This corresponds to baudrate/20 Bytes/s (baudrate/10 = maximum data rate on 8N1-configured links). Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`0`
- 单位：`B/s`


1270. MAV_2_REMOTE_PRT (INT32)
- 名称：MAV_2_REMOTE_PRT (INT32)
- 参数描述：MAVLink Remote Port for instance 2 Comment: If ethernet enabled and selected as configuration for MAVLink instance 2, selected remote port will be set and used in MAVLink instance 2. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1271. MAV_2_UDP_PRT (INT32)
- 名称：MAV_2_UDP_PRT (INT32)
- 参数描述：MAVLink Network Port for instance 2 Comment: If ethernet enabled and selected as configuration for MAVLink instance 2, selected udp port will be set and used in MAVLink instance 2. Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1272. MAV_COMP_ID (INT32)
- 名称：MAV_COMP_ID (INT32)
- 参数描述：MAVLink component ID    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 250]`
- 默认值：`1`
- 单位：``


1273. MAV_FWDEXTSP (INT32)
- 名称：MAV_FWDEXTSP (INT32)
- 参数描述：Forward external setpoint messages Comment: If set to 1 incoming external setpoint messages will be directly forwarded to the controllers if in offboard control mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1274. MAV_HASH_CHK_EN (INT32)
- 名称：MAV_HASH_CHK_EN (INT32)
- 参数描述：Parameter hash check Comment: Disabling the parameter hash check functionality will make the mavlink instance stream parameters continuously.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1275. MAV_HB_FORW_EN (INT32)
- 名称：MAV_HB_FORW_EN (INT32)
- 参数描述：Heartbeat message forwarding Comment: The mavlink heartbeat message will not be forwarded if this parameter is set to 'disabled'. The main reason for disabling heartbeats to be forwarded is because they confuse dronekit.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1276. MAV_PROTO_VER (INT32)
- 名称：MAV_PROTO_VER (INT32)
- 参数描述：MAVLink protocol version  Values:0: Default to 1, switch to 2 if GCS sends version 2 1: Always use version 1 2: Always use version 2
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1277. MAV_RADIO_TOUT (INT32)
- 名称：MAV_RADIO_TOUT (INT32)
- 参数描述：Timeout in seconds for the RADIO_STATUS reports coming in Comment: If the connected radio stops reporting RADIO_STATUS for a certain time, a warning is triggered and, if MAV_X_RADIO_CTL is enabled, the software-flow control is reset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 250]`
- 默认值：`5`
- 单位：`s`


1278. MAV_SIK_RADIO_ID (INT32)
- 名称：MAV_SIK_RADIO_ID (INT32)
- 参数描述：MAVLink SiK Radio ID Comment: When non-zero the MAVLink app will attempt to configure the SiK radio to this ID and re-set the parameter to 0. If the value is negative it will reset the complete radio config to factory defaults. Only applies if this mavlink instance is going through a SiK radio
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 240]`
- 默认值：`0`
- 单位：``


1279. MAV_SYS_ID (INT32)
- 名称：MAV_SYS_ID (INT32)
- 参数描述：MAVLink system ID    Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 250]`
- 默认值：`1`
- 单位：``


1280. MAV_TYPE (INT32)
- 名称：MAV_TYPE (INT32)
- 参数描述：MAVLink airframe type  Values:0: Generic micro air vehicle 1: Fixed wing aircraft 2: Quadrotor 3: Coaxial helicopter 4: Normal helicopter with tail rotor 7: Airship, controlled 8: Free balloon, uncontrolled 10: Ground rover 11: Surface vessel, boat, ship 12: Submarine 13: Hexarotor 14: Octorotor 15: Tricopter 19: VTOL Two-rotor Tailsitter 20: VTOL Quad-rotor Tailsitter 21: VTOL Tiltrotor 22: VTOL Standard (separate fixed rotors for hover and cruise flight) 23: VTOL Tailsitter
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 22]`
- 默认值：`0`
- 单位：``


1281. MAV_USEHILGPS (INT32)
- 名称：MAV_USEHILGPS (INT32)
- 参数描述：Use/Accept HIL GPS message even if not in HIL mode Comment: If set to 1 incoming HIL GPS messages are parsed.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1282. MODAL_IO_BAUD (INT32)
- 名称：MODAL_IO_BAUD (INT32)
- 参数描述：UART ESC baud rate Comment: Default rate is 250Kbps, which is used in off-the-shelf MoadalAI ESC products.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`250000`
- 单位：`bit/s`


1283. MODAL_IO_CONFIG (INT32)
- 名称：MODAL_IO_CONFIG (INT32)
- 参数描述：UART ESC configuration Comment: Selects what type of UART ESC, if any, is being used. 参数对照:0: - Disabled 1: - VOXL ESC Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1284. MODAL_IO_MODE (INT32)
- 名称：MODAL_IO_MODE (INT32)
- 参数描述：UART ESC Mode Comment: Selects what type of mode is enabled, if any 参数对照:0: - None 1: - Turtle Mode enabled via AUX1 2: - Turtle Mode enabled via AUX2 3: - UART Passthrough Mode Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


1285. MODAL_IO_RPM_MAX (INT32)
- 名称：MODAL_IO_RPM_MAX (INT32)
- 参数描述：UART ESC RPM Max Comment: Maximum RPM for ESC
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`15000`
- 单位：`rpm`


1286. MODAL_IO_RPM_MIN (INT32)
- 名称：MODAL_IO_RPM_MIN (INT32)
- 参数描述：UART ESC RPM Min Comment: Minimum RPM for ESC
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`5500`
- 单位：`rpm`


1287. MODAL_IO_SDIR1 (INT32)
- 名称：MODAL_IO_SDIR1 (INT32)
- 参数描述：UART ESC ID 1 Spin Direction Flag  Values:0: - Default 1: - Reverse
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1288. MODAL_IO_SDIR2 (INT32)
- 名称：MODAL_IO_SDIR2 (INT32)
- 参数描述：UART ESC ID 2 Spin Direction Flag  Values:0: - Default 1: - Reverse
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1289. MODAL_IO_SDIR3 (INT32)
- 名称：MODAL_IO_SDIR3 (INT32)
- 参数描述：UART ESC ID 3 Spin Direction Flag  Values:0: - Default 1: - Reverse
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1290. MODAL_IO_SDIR4 (INT32)
- 名称：MODAL_IO_SDIR4 (INT32)
- 参数描述：UART ESC ID 4 Spin Direction Flag  Values:0: - Default 1: - Reverse
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1291. MODAL_IO_T_COSP (FLOAT)
- 名称：MODAL_IO_T_COSP (FLOAT)
- 参数描述：UART ESC Turtle Mode Cosphi
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.000, 1.000] (0.001)`
- 默认值：`0.990`
- 单位：``


1292. MODAL_IO_T_DEAD (INT32)
- 名称：MODAL_IO_T_DEAD (INT32)
- 参数描述：UART ESC Turtle Mode Crash Flip Motor Deadband
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`20`
- 单位：``


1293. MODAL_IO_T_EXPO (INT32)
- 名称：MODAL_IO_T_EXPO (INT32)
- 参数描述：UART ESC Turtle Mode Crash Flip Motor expo
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100] (1)`
- 默认值：`35`
- 单位：``


1294. MODAL_IO_T_MINF (FLOAT)
- 名称：MODAL_IO_T_MINF (FLOAT)
- 参数描述：UART ESC Turtle Mode Crash Flip Motor STICK_MINF
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0] (1.0)`
- 默认值：`0.15`
- 单位：``


1295. MODAL_IO_T_PERC (INT32)
- 名称：MODAL_IO_T_PERC (INT32)
- 参数描述：UART ESC Turtle Mode Crash Flip Motor Percent
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 100] (1)`
- 默认值：`90`
- 单位：``


1296. MODAL_IO_VLOG (INT32)
- 名称：MODAL_IO_VLOG (INT32)
- 参数描述：UART ESC verbose logging  Values:0: - Disabled 1: - Enabled Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1297. MBE_ENABLE (INT32)
- 名称：MBE_ENABLE (INT32)
- 参数描述：Enable online mag bias calibration Comment: This enables continuous calibration of the magnetometers before takeoff using gyro data. Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1298. MBE_LEARN_GAIN (FLOAT)
- 名称：MBE_LEARN_GAIN (FLOAT)
- 参数描述：Mag bias estimator learning gain Comment: Increase to make the estimator more responsive Decrease to make the estimator more robust to noise
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 100] (0.1)`
- 默认值：`18.`
- 单位：``


1299. MAN_ARM_GESTURE (INT32)
- 名称：MAN_ARM_GESTURE (INT32)
- 参数描述：Enable arm/disarm stick gesture Comment: This determines if moving the left stick to the lower right arms and to the lower left disarms the vehicle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1300. FW_GPSF_LT (INT32)
- 名称：FW_GPSF_LT (INT32)
- 参数描述：GPS failure loiter time Comment: The time in seconds the system should do open loop loiter and wait for GPS recovery before it starts descending. Set to 0 to disable. Roll angle is set to FW_GPSF_R. Does only apply for fixed-wing vehicles or VTOLs with NAV_FORCE_VT set to 0.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3600]`
- 默认值：`30`
- 单位：`s`


1301. FW_GPSF_R (FLOAT)
- 名称：FW_GPSF_R (FLOAT)
- 参数描述：GPS failure fixed roll angle Comment: Roll in degrees during the loiter after the vehicle has lost GPS in an auto mode (e.g. mission or loiter).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 30.0] (0.5)`
- 默认值：`15.0`
- 单位：`deg`


1302. MIS_DIST_1WP (FLOAT)
- 名称：MIS_DIST_1WP (FLOAT)
- 参数描述：Maximal horizontal distance from current position to first waypoint Comment: Failsafe check to prevent running mission stored from previous flight at a new takeoff location. Set a value of zero or less to disable. The mission will not be started if the current waypoint is more distant than MIS_DIST_1WP from the current position.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 10000] (100)`
- 默认值：`900`
- 单位：`m`


1303. MIS_LND_ABRT_ALT (INT32)
- 名称：MIS_LND_ABRT_ALT (INT32)
- 参数描述：Landing abort min altitude Comment: Minimum altitude above landing point that the vehicle will climb to after an aborted landing. Then vehicle will loiter in this altitude until further command is received. Only applies to fixed-wing vehicles.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`30`
- 单位：`m`


1304. MIS_MNT_YAW_CTL (INT32)
- 名称：MIS_MNT_YAW_CTL (INT32)
- 参数描述：Enable yaw control of the mount. (Only affects multicopters and ROI mission items) Comment: If enabled, yaw commands will be sent to the mount and the vehicle will follow its heading towards the flight direction. If disabled, the vehicle will yaw towards the ROI. 参数对照:0: Disable 1: Enable
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1305. MIS_PD_TO (FLOAT)
- 名称：MIS_PD_TO (FLOAT)
- 参数描述：Timeout for a successful payload deployment acknowledgement
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (1)`
- 默认值：`5.0`
- 单位：`s`


1306. MIS_TAKEOFF_ALT (FLOAT)
- 名称：MIS_TAKEOFF_ALT (FLOAT)
- 参数描述：Default take-off altitude Comment: This is the relative altitude the system will take off to if not otherwise specified.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (0.5)`
- 默认值：`2.5`
- 单位：`m`


1307. MIS_TKO_LAND_REQ (INT32)
- 名称：MIS_TKO_LAND_REQ (INT32)
- 参数描述：Mission takeoff/landing required Comment: Specifies if a mission has to contain a takeoff and/or mission landing. Validity of configured takeoffs/landings is checked independently of the setting here. 参数对照:0: No requirements 1: Require a takeoff 2: Require a landing 3: Require a takeoff and a landing 4: Require both a takeoff and a landing, or neither
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1308. MIS_YAW_ERR (FLOAT)
- 名称：MIS_YAW_ERR (FLOAT)
- 参数描述：Max yaw error in degrees needed for waypoint heading acceptance
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 90] (1)`
- 默认值：`12.0`
- 单位：`deg`


1309. MIS_YAW_TMT (FLOAT)
- 名称：MIS_YAW_TMT (FLOAT)
- 参数描述：Time in seconds we wait on reaching target heading at a waypoint if it is forced Comment: If set > 0 it will ignore the target heading for normal waypoint acceptance. If the waypoint forces the heading the timeout will matter. For example on VTOL forwards transition. Mainly useful for VTOLs that have less yaw authority and might not reach target yaw in wind. Disabled by default.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 20] (1)`
- 默认值：`-1.0`
- 单位：`s`


1310. MPC_YAW_MODE (INT32)
- 名称：MPC_YAW_MODE (INT32)
- 参数描述：Heading behavior in autonomous modes  Values:0: towards waypoint 1: towards home 2: away from home 3: along trajectory 4: towards waypoint (yaw first)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4]`
- 默认值：`0`
- 单位：``


1311. NAV_ACC_RAD (FLOAT)
- 名称：NAV_ACC_RAD (FLOAT)
- 参数描述：Acceptance Radius Comment: Default acceptance radius, overridden by acceptance radius of waypoint if set. For fixed wing the npfg switch distance is used for horizontal acceptance.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 200.0] (0.5)`
- 默认值：`10.0`
- 单位：`m`


1312. NAV_FORCE_VT (INT32)
- 名称：NAV_FORCE_VT (INT32)
- 参数描述：Force VTOL mode takeoff and land
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1313. NAV_FW_ALTL_RAD (FLOAT)
- 名称：NAV_FW_ALTL_RAD (FLOAT)
- 参数描述：FW Altitude Acceptance Radius before a landing Comment: Altitude acceptance used for the last waypoint before a fixed-wing landing. This is usually smaller than the standard vertical acceptance because close to the ground higher accuracy is required.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 200.0]`
- 默认值：`5.0`
- 单位：`m`


1314. NAV_FW_ALT_RAD (FLOAT)
- 名称：NAV_FW_ALT_RAD (FLOAT)
- 参数描述：FW Altitude Acceptance Radius Comment: Acceptance radius for fixedwing altitude.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 200.0] (0.5)`
- 默认值：`10.0`
- 单位：`m`


1315. NAV_LOITER_RAD (FLOAT)
- 名称：NAV_LOITER_RAD (FLOAT)
- 参数描述：Loiter radius (FW only) Comment: Default value of loiter radius in FW mode (e.g. for Loiter mode).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[25, 1000] (0.5)`
- 默认值：`80.0`
- 单位：`m`


1316. NAV_MC_ALT_RAD (FLOAT)
- 名称：NAV_MC_ALT_RAD (FLOAT)
- 参数描述：MC Altitude Acceptance Radius Comment: Acceptance radius for multicopter altitude.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 200.0] (0.5)`
- 默认值：`0.8`
- 单位：`m`


1317. NAV_MIN_LTR_ALT (FLOAT)
- 名称：NAV_MIN_LTR_ALT (FLOAT)
- 参数描述：Minimum Loiter altitude Comment: This is the minimum altitude above Home the system will always obey in Loiter (Hold) mode if switched into this mode without specifying an altitude (e.g. through Loiter switch on RC). Doesn't affect Loiters that are part of Missions or that are entered through a reposition setpoint ("Go to"). Set to a negative value to disable.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, ?] (0.5)`
- 默认值：`-1.`
- 单位：`m`


1318. NAV_TRAFF_AVOID (INT32)
- 名称：NAV_TRAFF_AVOID (INT32)
- 参数描述：Set traffic avoidance mode Comment: Enabling this will allow the system to respond to transponder data from e.g. ADSB transponders 参数对照:0: Disabled 1: Warn only 2: Return mode 3: Land mode 4: Position Hold mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1319. NAV_TRAFF_A_HOR (FLOAT)
- 名称：NAV_TRAFF_A_HOR (FLOAT)
- 参数描述：Set NAV TRAFFIC AVOID horizontal distance Comment: Defines a crosstrack horizontal distance
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[500, ?]`
- 默认值：`500`
- 单位：`m`


1320. NAV_TRAFF_A_VER (FLOAT)
- 名称：NAV_TRAFF_A_VER (FLOAT)
- 参数描述：Set NAV TRAFFIC AVOID vertical distance
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[10, 500]`
- 默认值：`500`
- 单位：`m`


1321. NAV_TRAFF_COLL_T (INT32)
- 名称：NAV_TRAFF_COLL_T (INT32)
- 参数描述：Estimated time until collision Comment: Minimum acceptable time until collsion. Assumes constant speed over 3d distance.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 900000000]`
- 默认值：`60`
- 单位：`s`


1322. WEIGHT_BASE (FLOAT)
- 名称：WEIGHT_BASE (FLOAT)
- 参数描述：Vehicle base weight Comment: This is the weight of the vehicle at which it's performance limits were derived. A zero or negative value disables trim throttle and minimum airspeed compensation based on weight.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.5)`
- 默认值：`-1.0`
- 单位：`kg`


1323. WEIGHT_GROSS (FLOAT)
- 名称：WEIGHT_GROSS (FLOAT)
- 参数描述：Vehicle gross weight Comment: This is the actual weight of the vehicle at any time. This value will differ from WEIGHT_BASE in case weight was added or removed from the base weight. Examples are the addition of payloads or larger batteries. A zero or negative value disables trim throttle and minimum airspeed compensation based on weight.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`(0.1)`
- 默认值：`-1.0`
- 单位：`kg`


1324. MC_AIRMODE (INT32)
- 名称：MC_AIRMODE (INT32)
- 参数描述：Multicopter air-mode Comment: The air-mode enables the mixer to increase the total thrust of the multirotor in order to keep attitude and rate control even at low and high throttle. This function should be disabled during tuning as it will help the controller to diverge if the closed-loop is unstable (i.e. the vehicle is not tuned yet). Enabling air-mode for yaw requires the use of an arming switch. 参数对照:0: Disabled 1: Roll/Pitch 2: Roll/Pitch/Yaw
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1325. MNT_DO_STAB (INT32)
- 名称：MNT_DO_STAB (INT32)
- 参数描述：Stabilize the mount Comment: Set to true for servo gimbal, false for passthrough. This is required for a gimbal which is not capable of stabilizing itself and relies on the IMU's attitude estimation. 参数对照:0: Disable 1: Stabilize all axis 2: Stabilize yaw for absolute/lock mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


1326. MNT_LND_P_MAX (FLOAT)
- 名称：MNT_LND_P_MAX (FLOAT)
- 参数描述：Pitch maximum when landed
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`90.0`
- 单位：`deg`


1327. MNT_LND_P_MIN (FLOAT)
- 名称：MNT_LND_P_MIN (FLOAT)
- 参数描述：Pitch minimum when landed
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-90.0, 90.0]`
- 默认值：`-90.0`
- 单位：`deg`


1328. MNT_MAN_PITCH (INT32)
- 名称：MNT_MAN_PITCH (INT32)
- 参数描述：Auxiliary channel to control pitch (in AUX input or manual mode)  Values:0: Disable 1: AUX1 2: AUX2 3: AUX3 4: AUX4 5: AUX5 6: AUX6
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


1329. MNT_MAN_ROLL (INT32)
- 名称：MNT_MAN_ROLL (INT32)
- 参数描述：Auxiliary channel to control roll (in AUX input or manual mode)  Values:0: Disable 1: AUX1 2: AUX2 3: AUX3 4: AUX4 5: AUX5 6: AUX6
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


1330. MNT_MAN_YAW (INT32)
- 名称：MNT_MAN_YAW (INT32)
- 参数描述：Auxiliary channel to control yaw (in AUX input or manual mode)  Values:0: Disable 1: AUX1 2: AUX2 3: AUX3 4: AUX4 5: AUX5 6: AUX6
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 6]`
- 默认值：`0`
- 单位：``


1331. MNT_MAV_COMPID (INT32)
- 名称：MNT_MAV_COMPID (INT32)
- 参数描述：Mavlink Component ID of the mount Comment: If MNT_MODE_OUT is MAVLink protocol v2, mount configure/control commands will be sent with this component ID.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`154`
- 单位：``


1332. MNT_MAV_SYSID (INT32)
- 名称：MNT_MAV_SYSID (INT32)
- 参数描述：Mavlink System ID of the mount Comment: If MNT_MODE_OUT is MAVLink gimbal protocol v1, mount configure/control commands will be sent with this target ID.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`1`
- 单位：``


1333. MNT_MODE_IN (INT32)
- 名称：MNT_MODE_IN (INT32)
- 参数描述：Mount input mode Comment: This is the protocol used between the ground station and the autopilot. Recommended is Auto, RC only or MAVLink gimbal protocol v2. The rest will be deprecated. 参数对照:-1: DISABLED 0: Auto (RC and MAVLink gimbal protocol v2) 1: RC 2: MAVLINK_ROI (protocol v1, to be deprecated) 3: MAVLINK_DO_MOUNT (protocol v1, to be deprecated) 4: MAVlink gimbal protocol v2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 4]`
- 默认值：`-1`
- 单位：``


1334. MNT_MODE_OUT (INT32)
- 名称：MNT_MODE_OUT (INT32)
- 参数描述：Mount output mode Comment: This is the protocol used between the autopilot and a connected gimbal. Recommended is the MAVLink gimbal protocol v2 if the gimbal supports it. 参数对照:0: AUX 1: MAVLink gimbal protocol v1 2: MAVLink gimbal protocol v2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


1335. MNT_OFF_PITCH (FLOAT)
- 名称：MNT_OFF_PITCH (FLOAT)
- 参数描述：Offset for pitch channel output in degrees
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-360.0, 360.0]`
- 默认值：`0.0`
- 单位：`deg`


1336. MNT_OFF_ROLL (FLOAT)
- 名称：MNT_OFF_ROLL (FLOAT)
- 参数描述：Offset for roll channel output in degrees
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-360.0, 360.0]`
- 默认值：`0.0`
- 单位：`deg`


1337. MNT_OFF_YAW (FLOAT)
- 名称：MNT_OFF_YAW (FLOAT)
- 参数描述：Offset for yaw channel output in degrees
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-360.0, 360.0]`
- 默认值：`0.0`
- 单位：`deg`


1338. MNT_RANGE_PITCH (FLOAT)
- 名称：MNT_RANGE_PITCH (FLOAT)
- 参数描述：Range of pitch channel output in degrees (only in AUX output mode)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 720.0]`
- 默认值：`90.0`
- 单位：`deg`


1339. MNT_RANGE_ROLL (FLOAT)
- 名称：MNT_RANGE_ROLL (FLOAT)
- 参数描述：Range of roll channel output in degrees (only in AUX output mode)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 720.0]`
- 默认值：`90.0`
- 单位：`deg`


1340. MNT_RANGE_YAW (FLOAT)
- 名称：MNT_RANGE_YAW (FLOAT)
- 参数描述：Range of yaw channel output in degrees (only in AUX output mode)
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 720.0]`
- 默认值：`360.0`
- 单位：`deg`


1341. MNT_RATE_PITCH (FLOAT)
- 名称：MNT_RATE_PITCH (FLOAT)
- 参数描述：Angular pitch rate for manual input in degrees/second Comment: Full stick input [-1..1] translats to [-pitch rate..pitch rate].
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 90.0]`
- 默认值：`30.0`
- 单位：`deg/s`


1342. MNT_RATE_YAW (FLOAT)
- 名称：MNT_RATE_YAW (FLOAT)
- 参数描述：Angular yaw rate for manual input in degrees/second Comment: Full stick input [-1..1] translats to [-yaw rate..yaw rate].
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.0, 90.0]`
- 默认值：`30.0`
- 单位：`deg/s`


1343. MNT_RC_IN_MODE (INT32)
- 名称：MNT_RC_IN_MODE (INT32)
- 参数描述：Input mode for RC gimbal input  Values:0: Angle 1: Angular rate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`1`
- 单位：``


1344. MC_ACRO_EXPO (FLOAT)
- 名称：MC_ACRO_EXPO (FLOAT)
- 参数描述：Acro mode roll, pitch expo factor Comment: Exponential factor for tuning the input curve shape. 0 Purely linear input curve 1 Purely cubic input curve
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.`
- 单位：``


1345. MC_ACRO_EXPO_Y (FLOAT)
- 名称：MC_ACRO_EXPO_Y (FLOAT)
- 参数描述：Acro mode yaw expo factor Comment: Exponential factor for tuning the input curve shape. 0 Purely linear input curve 1 Purely cubic input curve
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.`
- 单位：``


1346. MC_ACRO_P_MAX (FLOAT)
- 名称：MC_ACRO_P_MAX (FLOAT)
- 参数描述：Acro mode maximum pitch rate Comment: Full stick deflection leads to this rate.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`100.`
- 单位：`deg/s`


1347. MC_ACRO_R_MAX (FLOAT)
- 名称：MC_ACRO_R_MAX (FLOAT)
- 参数描述：Acro mode maximum roll rate Comment: Full stick deflection leads to this rate.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`100.`
- 单位：`deg/s`


1348. MC_ACRO_SUPEXPO (FLOAT)
- 名称：MC_ACRO_SUPEXPO (FLOAT)
- 参数描述：Acro mode roll, pitch super expo factor Comment: "Superexponential" factor for refining the input curve shape tuned using MC_ACRO_EXPO. 0 Pure Expo function 0.7 reasonable shape enhancement for intuitive stick feel 0.95 very strong bent input curve only near maxima have effect
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.95]`
- 默认值：`0.`
- 单位：``


1349. MC_ACRO_SUPEXPOY (FLOAT)
- 名称：MC_ACRO_SUPEXPOY (FLOAT)
- 参数描述：Acro mode yaw super expo factor Comment: "Superexponential" factor for refining the input curve shape tuned using MC_ACRO_EXPO_Y. 0 Pure Expo function 0.7 reasonable shape enhancement for intuitive stick feel 0.95 very strong bent input curve only near maxima have effect
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.95]`
- 默认值：`0.`
- 单位：``


1350. MC_ACRO_Y_MAX (FLOAT)
- 名称：MC_ACRO_Y_MAX (FLOAT)
- 参数描述：Acro mode maximum yaw rate Comment: Full stick deflection leads to this rate.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`100.`
- 单位：`deg/s`


1351. MC_PITCHRATE_MAX (FLOAT)
- 名称：MC_PITCHRATE_MAX (FLOAT)
- 参数描述：Max pitch rate Comment: Limit for pitch rate in manual and auto modes (except acro). Has effect for large rotations in autonomous mode, to avoid large control output and mixer saturation. This is not only limited by the vehicle's properties, but also by the maximum measurement rate of the gyro.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`220.0`
- 单位：`deg/s`


1352. MC_PITCH_P (FLOAT)
- 名称：MC_PITCH_P (FLOAT)
- 参数描述：Pitch P gain Comment: Pitch proportional gain, i.e. desired angular speed in rad/s for error 1 rad.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 12] (0.1)`
- 默认值：`6.5`
- 单位：``


1353. MC_ROLLRATE_MAX (FLOAT)
- 名称：MC_ROLLRATE_MAX (FLOAT)
- 参数描述：Max roll rate Comment: Limit for roll rate in manual and auto modes (except acro). Has effect for large rotations in autonomous mode, to avoid large control output and mixer saturation. This is not only limited by the vehicle's properties, but also by the maximum measurement rate of the gyro.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`220.0`
- 单位：`deg/s`


1354. MC_ROLL_P (FLOAT)
- 名称：MC_ROLL_P (FLOAT)
- 参数描述：Roll P gain Comment: Roll proportional gain, i.e. desired angular speed in rad/s for error 1 rad.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 12] (0.1)`
- 默认值：`6.5`
- 单位：``


1355. MC_YAWRATE_MAX (FLOAT)
- 名称：MC_YAWRATE_MAX (FLOAT)
- 参数描述：Max yaw rate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1800.0] (5)`
- 默认值：`200.0`
- 单位：`deg/s`


1356. MC_YAW_P (FLOAT)
- 名称：MC_YAW_P (FLOAT)
- 参数描述：Yaw P gain Comment: Yaw proportional gain, i.e. desired angular speed in rad/s for error 1 rad.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 5] (0.1)`
- 默认值：`2.8`
- 单位：``


1357. MC_YAW_WEIGHT (FLOAT)
- 名称：MC_YAW_WEIGHT (FLOAT)
- 参数描述：Yaw weight Comment: A fraction [0,1] deprioritizing yaw compared to roll and pitch in non-linear attitude control. Deprioritizing yaw is necessary because multicopters have much less control authority in yaw compared to the other axes and it makes sense because yaw is not critical for stable hovering or 3D navigation. For yaw control tuning use MC_YAW_P. This ratio has no impact on the yaw gain.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.1)`
- 默认值：`0.4`
- 单位：``


1358. MPC_YAWRAUTO_MAX (FLOAT)
- 名称：MPC_YAWRAUTO_MAX (FLOAT)
- 参数描述：Max yaw rate in autonomous modes Comment: Limits the rate of change of the yaw setpoint to avoid large control output and mixer saturation.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 360] (5)`
- 默认值：`45.`
- 单位：`deg/s`


1359. CP_DELAY (FLOAT)
- 名称：CP_DELAY (FLOAT)
- 参数描述：Average delay of the range sensor message plus the tracking delay of the position controller in seconds Comment: Only used in Position mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0.4`
- 单位：`s`


1360. CP_DIST (FLOAT)
- 名称：CP_DIST (FLOAT)
- 参数描述：Minimum distance the vehicle should keep to all obstacles Comment: Only used in Position mode. Collision avoidance is disabled by setting this parameter to a negative value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 15]`
- 默认值：`-1.0`
- 单位：`m`


1361. CP_GO_NO_DATA (INT32)
- 名称：CP_GO_NO_DATA (INT32)
- 参数描述：Boolean to allow moving into directions where there is no sensor data (outside FOV) Comment: Only used in Position mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1362. CP_GUIDE_ANG (FLOAT)
- 名称：CP_GUIDE_ANG (FLOAT)
- 参数描述：Angle left/right from the commanded setpoint by which the collision prevention algorithm can choose to change the setpoint direction Comment: Only used in Position mode.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 90]`
- 默认值：`30.`
- 单位：`deg`


1363. MC_MAN_TILT_TAU (FLOAT)
- 名称：MC_MAN_TILT_TAU (FLOAT)
- 参数描述：Manual tilt input filter time constant Comment: Setting this parameter to 0 disables the filter
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 2.0]`
- 默认值：`0.0`
- 单位：`s`


1364. MPC_ACC_DOWN_MAX (FLOAT)
- 名称：MPC_ACC_DOWN_MAX (FLOAT)
- 参数描述：Maximum downwards acceleration in climb rate controlled modes
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15] (1)`
- 默认值：`3.`
- 单位：`m/s^2`


1365. MPC_ACC_HOR (FLOAT)
- 名称：MPC_ACC_HOR (FLOAT)
- 参数描述：Acceleration for autonomous and for manual modes Comment: When piloting manually, this parameter is only used in MPC_POS_MODE 4.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15] (1)`
- 默认值：`3.`
- 单位：`m/s^2`


1366. MPC_ACC_HOR_MAX (FLOAT)
- 名称：MPC_ACC_HOR_MAX (FLOAT)
- 参数描述：Maximum horizontal acceleration Comment: MPC_POS_MODE 1 just deceleration 3 acceleration and deceleration 4 not used, use MPC_ACC_HOR instead
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15] (1)`
- 默认值：`5.`
- 单位：`m/s^2`


1367. MPC_ACC_UP_MAX (FLOAT)
- 名称：MPC_ACC_UP_MAX (FLOAT)
- 参数描述：Maximum upwards acceleration in climb rate controlled modes
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15] (1)`
- 默认值：`4.`
- 单位：`m/s^2`


1368. MPC_ALT_MODE (INT32)
- 名称：MPC_ALT_MODE (INT32)
- 参数描述：Altitude reference mode Comment: Set to 0 to control height relative to the earth frame origin. This origin may move up and down in flight due to sensor drift. Set to 1 to control height relative to estimated distance to ground. The vehicle will move up and down with terrain height variation. Requires a distance to ground sensor. The height controller will revert to using height above origin if the distance to ground estimate becomes invalid as indicated by the local_position.distance_bottom_valid message being false. Set to 2 to control height relative to ground (requires a distance sensor) when stationary and relative to earth frame origin when moving horizontally. The speed threshold is controlled by the MPC_HOLD_MAX_XY parameter. 参数对照:0: Altitude following 1: Terrain following 2: Terrain hold
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2]`
- 默认值：`0`
- 单位：``


1369. MPC_HOLD_DZ (FLOAT)
- 名称：MPC_HOLD_DZ (FLOAT)
- 参数描述：Deadzone for sticks in manual piloted modes Comment: Does not apply to manual throttle and direct attitude piloting by stick.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.1`
- 单位：``


1370. MPC_HOLD_MAX_XY (FLOAT)
- 名称：MPC_HOLD_MAX_XY (FLOAT)
- 参数描述：Maximum horizontal velocity for which position hold is enabled (use 0 to disable check) Comment: Only used with MPC_POS_MODE 0 or MPC_ALT_MODE 2
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0.8`
- 单位：`m/s`


1371. MPC_HOLD_MAX_Z (FLOAT)
- 名称：MPC_HOLD_MAX_Z (FLOAT)
- 参数描述：Maximum vertical velocity for which position hold is enabled (use 0 to disable check) Comment: Only used with MPC_ALT_MODE 1
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 3]`
- 默认值：`0.6`
- 单位：`m/s`


1372. MPC_JERK_AUTO (FLOAT)
- 名称：MPC_JERK_AUTO (FLOAT)
- 参数描述：Jerk limit in autonomous modes Comment: Limit the maximum jerk of the vehicle (how fast the acceleration can change). A lower value leads to smoother vehicle motions but also limited agility.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 80] (1)`
- 默认值：`4.`
- 单位：`m/s^3`


1373. MPC_JERK_MAX (FLOAT)
- 名称：MPC_JERK_MAX (FLOAT)
- 参数描述：Maximum horizontal and vertical jerk in Position/Altitude mode Comment: Limit the maximum jerk of the vehicle (how fast the acceleration can change). A lower value leads to smoother motions but limits agility (how fast it can change directions or break). Setting this to the maximum value essentially disables the limit. Only used with smooth MPC_POS_MODE 3 and 4.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 500] (1)`
- 默认值：`8.`
- 单位：`m/s^3`


1374. MPC_LAND_ALT1 (FLOAT)
- 名称：MPC_LAND_ALT1 (FLOAT)
- 参数描述：Altitude for 1. step of slow landing (descend) Comment: Below this altitude descending velocity gets limited to a value between "MPC_Z_VEL_MAX_DN" (or "MPC_Z_V_AUTO_DN") and "MPC_LAND_SPEED" Value needs to be higher than "MPC_LAND_ALT2"
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 122]`
- 默认值：`10.`
- 单位：`m`


1375. MPC_LAND_ALT2 (FLOAT)
- 名称：MPC_LAND_ALT2 (FLOAT)
- 参数描述：Altitude for 2. step of slow landing (landing) Comment: Below this altitude descending velocity gets limited to "MPC_LAND_SPEED" Value needs to be lower than "MPC_LAND_ALT1"
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 122]`
- 默认值：`5.`
- 单位：`m`


1376. MPC_LAND_ALT3 (FLOAT)
- 名称：MPC_LAND_ALT3 (FLOAT)
- 参数描述：Altitude for 3. step of slow landing Comment: Below this altitude descending velocity gets limited to "MPC_LAND_CRWL", if LIDAR available. No effect if LIDAR not available
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 122]`
- 默认值：`1.`
- 单位：`m`


1377. MPC_LAND_CRWL (FLOAT)
- 名称：MPC_LAND_CRWL (FLOAT)
- 参数描述：Land crawl descend rate Comment: Used below MPC_LAND_ALT3 if distance sensor data is availabe.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, ?]`
- 默认值：`0.3`
- 单位：`m/s`


1378. MPC_LAND_RADIUS (FLOAT)
- 名称：MPC_LAND_RADIUS (FLOAT)
- 参数描述：User assisted landing radius Comment: When nudging is enabled (see MPC_LAND_RC_HELP), this controls the maximum allowed horizontal displacement from the original landing point.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?] (1)`
- 默认值：`1000.`
- 单位：`m`


1379. MPC_LAND_RC_HELP (INT32)
- 名称：MPC_LAND_RC_HELP (INT32)
- 参数描述：Enable nudging based on user input during autonomous land routine Comment: Using stick input the vehicle can be moved horizontally and yawed. The descend speed is amended: stick full up - 0 stick centered - MPC_LAND_SPEED stick full down - 2 * MPC_LAND_SPEED Manual override during auto modes has to be disabled to use this feature (see COM_RC_OVERRIDE). 参数对照:0: Nudging disabled 1: Nudging enabled
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1]`
- 默认值：`0`
- 单位：``


1380. MPC_LAND_SPEED (FLOAT)
- 名称：MPC_LAND_SPEED (FLOAT)
- 参数描述：Landing descend rate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.6, ?]`
- 默认值：`0.7`
- 单位：`m/s`


1381. MPC_MANTHR_MIN (FLOAT)
- 名称：MPC_MANTHR_MIN (FLOAT)
- 参数描述：Minimum collective thrust in Stabilized mode Comment: The value is mapped to the lowest throttle stick position in Stabilized mode. Too low collective thrust leads to loss of roll/pitch/yaw torque control authority. Airmode is used to keep torque authority with zero thrust (see MC_AIRMODE).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.08`
- 单位：`norm`


1382. MPC_MAN_TILT_MAX (FLOAT)
- 名称：MPC_MAN_TILT_MAX (FLOAT)
- 参数描述：Maximal tilt angle in Stabilized or Altitude mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 90] (1)`
- 默认值：`35.`
- 单位：`deg`


1383. MPC_MAN_Y_MAX (FLOAT)
- 名称：MPC_MAN_Y_MAX (FLOAT)
- 参数描述：Max manual yaw rate for Stabilized, Altitude, Position mode
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 400] (10)`
- 默认值：`150.`
- 单位：`deg/s`


1384. MPC_MAN_Y_TAU (FLOAT)
- 名称：MPC_MAN_Y_TAU (FLOAT)
- 参数描述：Manual yaw rate input filter time constant Comment: Not used in Stabilized mode Setting this parameter to 0 disables the filter
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 5] (0.01)`
- 默认值：`0.08`
- 单位：`s`


1385. MPC_POS_MODE (INT32)
- 名称：MPC_POS_MODE (INT32)
- 参数描述：Position/Altitude mode variant Comment: The supported sub-modes are: 0 Sticks directly map to velocity setpoints without smoothing. Also applies to vertical direction and Altitude mode. Useful for velocity control tuning. 3 Sticks map to velocity but with maximum acceleration and jerk limits based on jerk optimized trajectory generator (different algorithm than 1). 4 Sticks map to acceleration and there's a virtual brake drag 参数对照:0: Direct velocity 3: Smoothed velocity 4: Acceleration based
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`4`
- 单位：``


1386. MPC_THR_CURVE (INT32)
- 名称：MPC_THR_CURVE (INT32)
- 参数描述：Thrust curve mapping in Stabilized Mode Comment: This parameter defines how the throttle stick input is mapped to collective thrust in Stabilized mode. In case the default is used ('Rescale to hover thrust'), the stick input is linearly rescaled, such that a centered stick corresponds to the hover throttle (see MPC_THR_HOVER). Select 'No Rescale' to directly map the stick 1:1 to the output. This can be useful in case the hover thrust is very low and the default would lead to too much distortion (e.g. if hover thrust is set to 20%, then 80% of the upper thrust range is squeezed into the upper half of the stick range). Note: In case MPC_THR_HOVER is set to 50%, the modes 0 and 1 are the same. 参数对照:0: Rescale to hover thrust 1: No Rescale
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1387. MPC_THR_HOVER (FLOAT)
- 名称：MPC_THR_HOVER (FLOAT)
- 参数描述：Vertical thrust required to hover Comment: Mapped to center throttle stick in Stabilized mode (see MPC_THR_CURVE). Used for initialization of the hover thrust estimator (see MPC_USE_HTE). The estimated hover thrust is used as base for zero vertical acceleration in altitude control. The hover thrust is important for land detection to work correctly.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 0.8] (0.01)`
- 默认值：`0.5`
- 单位：`norm`


1388. MPC_THR_MAX (FLOAT)
- 名称：MPC_THR_MAX (FLOAT)
- 参数描述：Maximum collective thrust in climb rate controlled modes Comment: Limit allowed thrust e.g. for indoor test of overpowered vehicle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.05)`
- 默认值：`1.`
- 单位：`norm`


1389. MPC_THR_MIN (FLOAT)
- 名称：MPC_THR_MIN (FLOAT)
- 参数描述：Minimum collective thrust in climb rate controlled modes Comment: Too low thrust leads to loss of roll/pitch/yaw torque control authority. With airmode enabled this parameters can be set to 0 while still keeping torque authority (see MC_AIRMODE).
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.05, 0.5] (0.01)`
- 默认值：`0.12`
- 单位：`norm`


1390. MPC_THR_XY_MARG (FLOAT)
- 名称：MPC_THR_XY_MARG (FLOAT)
- 参数描述：Horizontal thrust margin Comment: Margin that is kept for horizontal control when higher priority vertical thrust is saturated. To avoid completely starving horizontal control with high vertical error.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 0.5] (0.01)`
- 默认值：`0.3`
- 单位：`norm`


1391. MPC_TILTMAX_AIR (FLOAT)
- 名称：MPC_TILTMAX_AIR (FLOAT)
- 参数描述：Maximum tilt angle in air Comment: Absolute maximum for all velocity or acceleration controlled modes. Any higher value is truncated.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[20, 89] (1)`
- 默认值：`45.`
- 单位：`deg`


1392. MPC_TILTMAX_LND (FLOAT)
- 名称：MPC_TILTMAX_LND (FLOAT)
- 参数描述：Maximum tilt during inital takeoff ramp Comment: Tighter tilt limit during takeoff to avoid tip over.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[5, 89] (1)`
- 默认值：`12.`
- 单位：`deg`


1393. MPC_TKO_RAMP_T (FLOAT)
- 名称：MPC_TKO_RAMP_T (FLOAT)
- 参数描述：Smooth takeoff ramp time constant Comment: Increasing this value will make climb rate controlled takeoff slower. If it's too slow the drone might scratch the ground and tip over. A time constant of 0 disables the ramp
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 5]`
- 默认值：`3.`
- 单位：`s`


1394. MPC_TKO_SPEED (FLOAT)
- 名称：MPC_TKO_SPEED (FLOAT)
- 参数描述：Takeoff climb rate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1, 5]`
- 默认值：`1.5`
- 单位：`m/s`


1395. MPC_USE_HTE (INT32)
- 名称：MPC_USE_HTE (INT32)
- 参数描述：Hover thrust estimator Comment: Disable to use the fixed parameter MPC_THR_HOVER Enable to use the hover thrust estimator
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Enabled (1)`
- 单位：``


1396. MPC_VELD_LP (FLOAT)
- 名称：MPC_VELD_LP (FLOAT)
- 参数描述：Numerical velocity derivative low pass cutoff frequency
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 10] (0.5)`
- 默认值：`5.0`
- 单位：`Hz`


1397. MPC_VEL_MANUAL (FLOAT)
- 名称：MPC_VEL_MANUAL (FLOAT)
- 参数描述：Maximum horizontal velocity setpoint in Position mode Comment: Must be smaller than MPC_XY_VEL_MAX. The maximum sideways and backward speed can be set differently using MPC_VEL_MAN_SIDE and MPC_VEL_MAN_BACK, respectively.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[3, 20] (1)`
- 默认值：`10.`
- 单位：`m/s`


1398. MPC_VEL_MAN_BACK (FLOAT)
- 名称：MPC_VEL_MAN_BACK (FLOAT)
- 参数描述：Maximum backward velocity in Position mode Comment: If set to a negative value or larger than MPC_VEL_MANUAL then MPC_VEL_MANUAL is used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 20] (1)`
- 默认值：`-1.`
- 单位：`m/s`


1399. MPC_VEL_MAN_SIDE (FLOAT)
- 名称：MPC_VEL_MAN_SIDE (FLOAT)
- 参数描述：Maximum sideways velocity in Position mode Comment: If set to a negative value or larger than MPC_VEL_MANUAL then MPC_VEL_MANUAL is used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 20] (1)`
- 默认值：`-1.`
- 单位：`m/s`


1400. MPC_XY_CRUISE (FLOAT)
- 名称：MPC_XY_CRUISE (FLOAT)
- 参数描述：Default horizontal velocity in autonomous modes Comment: e.g. in Missions, RTL, Goto if the waypoint does not specify differently
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[3, 20] (1)`
- 默认值：`5.`
- 单位：`m/s`


1401. MPC_XY_ERR_MAX (FLOAT)
- 名称：MPC_XY_ERR_MAX (FLOAT)
- 参数描述：Maximum horizontal error allowed by the trajectory generator Comment: The integration speed of the trajectory setpoint is linearly reduced with the horizontal position tracking error. When the error is above this parameter, the integration of the trajectory is stopped to wait for the drone. This value can be adjusted depending on the tracking capabilities of the vehicle.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 10] (1)`
- 默认值：`2.`
- 单位：``


1402. MPC_XY_MAN_EXPO (FLOAT)
- 名称：MPC_XY_MAN_EXPO (FLOAT)
- 参数描述：Manual position control stick exponential curve sensitivity Comment: The higher the value the less sensitivity the stick has around zero while still reaching the maximum value with full stick deflection. 0 Purely linear input curve 1 Purely cubic input curve
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.6`
- 单位：``


1403. MPC_XY_P (FLOAT)
- 名称：MPC_XY_P (FLOAT)
- 参数描述：Proportional gain for horizontal position error Comment: Defined as corrective velocity in m/s per m position error
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2] (0.1)`
- 默认值：`0.95`
- 单位：``


1404. MPC_XY_TRAJ_P (FLOAT)
- 名称：MPC_XY_TRAJ_P (FLOAT)
- 参数描述：Proportional gain for horizontal trajectory position error
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1] (0.1)`
- 默认值：`0.5`
- 单位：``


1405. MPC_XY_VEL_ALL (FLOAT)
- 名称：MPC_XY_VEL_ALL (FLOAT)
- 参数描述：Overall Horizontal Velocity Limit Comment: If set to a value greater than zero, other parameters are automatically set (such as MPC_XY_VEL_MAX or MPC_VEL_MANUAL). If set to a negative value, the existing individual parameters are used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-20, 20] (1)`
- 默认值：`-10.`
- 单位：``


1406. MPC_XY_VEL_D_ACC (FLOAT)
- 名称：MPC_XY_VEL_D_ACC (FLOAT)
- 参数描述：Differential gain for horizontal velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s^2 velocity derivative
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 2] (0.02)`
- 默认值：`0.2`
- 单位：``


1407. MPC_XY_VEL_I_ACC (FLOAT)
- 名称：MPC_XY_VEL_I_ACC (FLOAT)
- 参数描述：Integral gain for horizontal velocity error Comment: Defined as correction acceleration in m/s^2 per m velocity integral Allows to eliminate steady state errors in disturbances like wind.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 60] (0.02)`
- 默认值：`0.4`
- 单位：``


1408. MPC_XY_VEL_MAX (FLOAT)
- 名称：MPC_XY_VEL_MAX (FLOAT)
- 参数描述：Maximum horizontal velocity Comment: Absolute maximum for all velocity controlled modes. Any higher value is truncated.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 20] (1)`
- 默认值：`12.`
- 单位：`m/s`


1409. MPC_XY_VEL_P_ACC (FLOAT)
- 名称：MPC_XY_VEL_P_ACC (FLOAT)
- 参数描述：Proportional gain for horizontal velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s velocity error
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1.2, 5] (0.1)`
- 默认值：`1.8`
- 单位：``


1410. MPC_YAW_EXPO (FLOAT)
- 名称：MPC_YAW_EXPO (FLOAT)
- 参数描述：Manual control stick yaw rotation exponential curve Comment: The higher the value the less sensitivity the stick has around zero while still reaching the maximum value with full stick deflection. 0 Purely linear input curve 1 Purely cubic input curve
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.6`
- 单位：``


1411. MPC_Z_MAN_EXPO (FLOAT)
- 名称：MPC_Z_MAN_EXPO (FLOAT)
- 参数描述：Manual control stick vertical exponential curve Comment: The higher the value the less sensitivity the stick has around zero while still reaching the maximum value with full stick deflection. 0 Purely linear input curve 1 Purely cubic input curve
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.6`
- 单位：``


1412. MPC_Z_P (FLOAT)
- 名称：MPC_Z_P (FLOAT)
- 参数描述：Proportional gain for vertical position error Comment: Defined as corrective velocity in m/s per m position error
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.1, 1.5] (0.1)`
- 默认值：`1.`
- 单位：``


1413. MPC_Z_VEL_ALL (FLOAT)
- 名称：MPC_Z_VEL_ALL (FLOAT)
- 参数描述：Overall Vertical Velocity Limit Comment: If set to a value greater than zero, other parameters are automatically set (such as MPC_Z_VEL_MAX_UP or MPC_LAND_SPEED). If set to a negative value, the existing individual parameters are used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-3, 8] (0.5)`
- 默认值：`-3.`
- 单位：``


1414. MPC_Z_VEL_D_ACC (FLOAT)
- 名称：MPC_Z_VEL_D_ACC (FLOAT)
- 参数描述：Differential gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s^2 velocity derivative
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 2] (0.02)`
- 默认值：`0.`
- 单位：``


1415. MPC_Z_VEL_I_ACC (FLOAT)
- 名称：MPC_Z_VEL_I_ACC (FLOAT)
- 参数描述：Integral gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m velocity integral
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.2, 3] (0.1)`
- 默认值：`2.`
- 单位：``


1416. MPC_Z_VEL_MAX_DN (FLOAT)
- 名称：MPC_Z_VEL_MAX_DN (FLOAT)
- 参数描述：Maximum descent velocity Comment: Absolute maximum for all climb rate controlled modes. In manually piloted modes full stick deflection commands this velocity. For default autonomous velocity see MPC_Z_V_AUTO_UP
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 4] (0.1)`
- 默认值：`1.5`
- 单位：`m/s`


1417. MPC_Z_VEL_MAX_UP (FLOAT)
- 名称：MPC_Z_VEL_MAX_UP (FLOAT)
- 参数描述：Maximum ascent velocity Comment: Absolute maximum for all climb rate controlled modes. In manually piloted modes full stick deflection commands this velocity. For default autonomous velocity see MPC_Z_V_AUTO_UP
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 8] (0.1)`
- 默认值：`3.`
- 单位：`m/s`


1418. MPC_Z_VEL_P_ACC (FLOAT)
- 名称：MPC_Z_VEL_P_ACC (FLOAT)
- 参数描述：Proportional gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s velocity error
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[2, 15] (0.1)`
- 默认值：`4.`
- 单位：``


1419. MPC_Z_V_AUTO_DN (FLOAT)
- 名称：MPC_Z_V_AUTO_DN (FLOAT)
- 参数描述：Descent velocity in autonomous modes Comment: For manual modes and offboard, see MPC_Z_VEL_MAX_DN
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 4] (0.5)`
- 默认值：`1.5`
- 单位：`m/s`


1420. MPC_Z_V_AUTO_UP (FLOAT)
- 名称：MPC_Z_V_AUTO_UP (FLOAT)
- 参数描述：Ascent velocity in autonomous modes Comment: For manually controlled modes and offboard see MPC_Z_VEL_MAX_UP
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.5, 8] (0.5)`
- 默认值：`3.`
- 单位：`m/s`


1421. SYS_VEHICLE_RESP (FLOAT)
- 名称：SYS_VEHICLE_RESP (FLOAT)
- 参数描述：Responsiveness Comment: Changes the overall responsiveness of the vehicle. The higher the value, the faster the vehicle will react. If set to a value greater than zero, other parameters are automatically set (such as the acceleration or jerk limits). If set to a negative value, the existing individual parameters are used.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 1] (0.05)`
- 默认值：`-0.4`
- 单位：``


1422. WV_EN (INT32)
- 名称：WV_EN (INT32)
- 参数描述：Enable weathervane
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1423. WV_ROLL_MIN (FLOAT)
- 名称：WV_ROLL_MIN (FLOAT)
- 参数描述：Minimum roll angle setpoint for weathervane controller to demand a yaw-rate
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 5]`
- 默认值：`1.0`
- 单位：`deg`


1424. WV_YRATE_MAX (FLOAT)
- 名称：WV_YRATE_MAX (FLOAT)
- 参数描述：Maximum yawrate the weathervane controller is allowed to demand
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 120]`
- 默认值：`90.0`
- 单位：`deg/s`


1425. MC_BAT_SCALE_EN (INT32)
- 名称：MC_BAT_SCALE_EN (INT32)
- 参数描述：Battery power level scaler Comment: This compensates for voltage drop of the battery over time by attempting to normalize performance across the operating range of the battery. The copter should constantly behave as if it was fully charged with reduced max acceleration at lower battery percentages. i.e. if hover is at 0.5 throttle at 100% battery, it will still be 0.5 at 60% battery.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1426. MC_PITCHRATE_D (FLOAT)
- 名称：MC_PITCHRATE_D (FLOAT)
- 参数描述：Pitch rate D gain Comment: Pitch rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.0005)`
- 默认值：`0.003`
- 单位：``


1427. MC_PITCHRATE_FF (FLOAT)
- 名称：MC_PITCHRATE_FF (FLOAT)
- 参数描述：Pitch rate feedforward Comment: Improves tracking performance.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：``


1428. MC_PITCHRATE_I (FLOAT)
- 名称：MC_PITCHRATE_I (FLOAT)
- 参数描述：Pitch rate I gain Comment: Pitch rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.2`
- 单位：``


1429. MC_PITCHRATE_K (FLOAT)
- 名称：MC_PITCHRATE_K (FLOAT)
- 参数描述：Pitch rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_PITCHRATE_K * (MC_PITCHRATE_P * error + MC_PITCHRATE_I * error_integral + MC_PITCHRATE_D * error_derivative) Set MC_PITCHRATE_P=1 to implement a PID in the ideal form. Set MC_PITCHRATE_K=1 to implement a PID in the parallel form.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1430. MC_PITCHRATE_P (FLOAT)
- 名称：MC_PITCHRATE_P (FLOAT)
- 参数描述：Pitch rate P gain Comment: Pitch rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 0.6] (0.01)`
- 默认值：`0.15`
- 单位：``


1431. MC_PR_INT_LIM (FLOAT)
- 名称：MC_PR_INT_LIM (FLOAT)
- 参数描述：Pitch rate integrator limit Comment: Pitch rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large pitch moment trim changes.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1432. MC_ROLLRATE_D (FLOAT)
- 名称：MC_ROLLRATE_D (FLOAT)
- 参数描述：Roll rate D gain Comment: Roll rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.01] (0.0005)`
- 默认值：`0.003`
- 单位：``


1433. MC_ROLLRATE_FF (FLOAT)
- 名称：MC_ROLLRATE_FF (FLOAT)
- 参数描述：Roll rate feedforward Comment: Improves tracking performance.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：``


1434. MC_ROLLRATE_I (FLOAT)
- 名称：MC_ROLLRATE_I (FLOAT)
- 参数描述：Roll rate I gain Comment: Roll rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.2`
- 单位：``


1435. MC_ROLLRATE_K (FLOAT)
- 名称：MC_ROLLRATE_K (FLOAT)
- 参数描述：Roll rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_ROLLRATE_K * (MC_ROLLRATE_P * error + MC_ROLLRATE_I * error_integral + MC_ROLLRATE_D * error_derivative) Set MC_ROLLRATE_P=1 to implement a PID in the ideal form. Set MC_ROLLRATE_K=1 to implement a PID in the parallel form.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1436. MC_ROLLRATE_P (FLOAT)
- 名称：MC_ROLLRATE_P (FLOAT)
- 参数描述：Roll rate P gain Comment: Roll rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.01, 0.5] (0.01)`
- 默认值：`0.15`
- 单位：``


1437. MC_RR_INT_LIM (FLOAT)
- 名称：MC_RR_INT_LIM (FLOAT)
- 参数描述：Roll rate integrator limit Comment: Roll rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large roll moment trim changes.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1438. MC_YAWRATE_D (FLOAT)
- 名称：MC_YAWRATE_D (FLOAT)
- 参数描述：Yaw rate D gain Comment: Yaw rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.0`
- 单位：``


1439. MC_YAWRATE_FF (FLOAT)
- 名称：MC_YAWRATE_FF (FLOAT)
- 参数描述：Yaw rate feedforward Comment: Improves tracking performance.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.0`
- 单位：``


1440. MC_YAWRATE_I (FLOAT)
- 名称：MC_YAWRATE_I (FLOAT)
- 参数描述：Yaw rate I gain Comment: Yaw rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.1`
- 单位：``


1441. MC_YAWRATE_K (FLOAT)
- 名称：MC_YAWRATE_K (FLOAT)
- 参数描述：Yaw rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_YAWRATE_K * (MC_YAWRATE_P * error + MC_YAWRATE_I * error_integral + MC_YAWRATE_D * error_derivative) Set MC_YAWRATE_P=1 to implement a PID in the ideal form. Set MC_YAWRATE_K=1 to implement a PID in the parallel form.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1442. MC_YAWRATE_P (FLOAT)
- 名称：MC_YAWRATE_P (FLOAT)
- 参数描述：Yaw rate P gain Comment: Yaw rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 0.6] (0.01)`
- 默认值：`0.2`
- 单位：``


1443. MC_YR_INT_LIM (FLOAT)
- 名称：MC_YR_INT_LIM (FLOAT)
- 参数描述：Yaw rate integrator limit Comment: Yaw rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large yaw moment trim changes.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1444. MSP_OSD_CONFIG (INT32)
- 名称：MSP_OSD_CONFIG (INT32)
- 参数描述：Serial Configuration for MSP OSD Comment: Configure on which serial port to run MSP OSD. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1445. OSD_ATXXXX_CFG (INT32)
- 名称：OSD_ATXXXX_CFG (INT32)
- 参数描述：Enable/Disable the ATXXX OSD Chip Comment: Configure the ATXXXX OSD Chip (mounted on the OmnibusF4SD board) and select the transmission standard. 参数对照:0: Disabled 1: NTSC 2: PAL Reboot required: true
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1446. OSD_CH_HEIGHT (INT32)
- 名称：OSD_CH_HEIGHT (INT32)
- 参数描述：OSD Crosshairs Height Comment: Controls the vertical position of the crosshair display. Resolution is limited by OSD to 15 discrete values. Negative values will display the crosshairs below the horizon
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-8, 8]`
- 默认值：`0`
- 单位：``


1447. OSD_DWELL_TIME (INT32)
- 名称：OSD_DWELL_TIME (INT32)
- 参数描述：OSD Dwell Time (ms) Comment: Amount of time in milliseconds to dwell at the beginning of the display, when scrolling.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[100, 10000]`
- 默认值：`500`
- 单位：``


1448. OSD_LOG_LEVEL (INT32)
- 名称：OSD_LOG_LEVEL (INT32)
- 参数描述：OSD Warning Level Comment: Minimum security of log level to display on the OSD.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`3`
- 单位：``


1449. OSD_SCROLL_RATE (INT32)
- 名称：OSD_SCROLL_RATE (INT32)
- 参数描述：OSD Scroll Rate (ms) Comment: Scroll rate in milliseconds for OSD messages longer than available character width. This is lower-bounded by the nominal loop rate of this module.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[100, 1000]`
- 默认值：`125`
- 单位：``


1450. OSD_SYMBOLS (INT32)
- 名称：OSD_SYMBOLS (INT32)
- 参数描述：OSD Symbol Selection Comment: Configure / toggle support display options. Bitmask:0: CRAFT_NAME 1: DISARMED 2: GPS_LAT 3: GPS_LON 4: GPS_SATS 5: GPS_SPEED 6: HOME_DIST 7: HOME_DIR 8: MAIN_BATT_VOLTAGE 9: CURRENT_DRAW 10: MAH_DRAWN 11: RSSI_VALUE 12: ALTITUDE 13: NUMERICAL_VARIO 14: (unused) FLYMODE 15: (unused) ESC_TMP 16: (unused) PITCH_ANGLE 17: (unused) ROLL_ANGLE 18: CROSSHAIRS 19: AVG_CELL_VOLTAGE 20: (unused) HORIZON_SIDEBARS 21: POWER
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 4194303]`
- 默认值：`16383`
- 单位：``


1451. MOT_SLEW_MAX (FLOAT)
- 名称：MOT_SLEW_MAX (FLOAT)
- 参数描述：Minimum motor rise time (slew rate limit) Comment: Minimum time allowed for the motor input signal to pass through a range of 1000 PWM units. A value x means that the motor signal can only go from 1000 to 2000 PWM in minimum x seconds. Zero means that slew rate limiting is disabled.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：`s/(1000*PWM)`


1452. PWM_SBUS_MODE (INT32)
- 名称：PWM_SBUS_MODE (INT32)
- 参数描述：S.BUS out Comment: Set to 1 to enable S.BUS version 1 output instead of RSSI.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1453. THR_MDL_FAC (FLOAT)
- 名称：THR_MDL_FAC (FLOAT)
- 参数描述：Thrust to motor control signal model parameter Comment: Parameter used to model the nonlinear relationship between motor control signal (e.g. PWM) and static thrust. The model is: rel_thrust = factor * rel_signal^2 + (1-factor) * rel_signal, where rel_thrust is the normalized thrust between 0 and 1, and rel_signal is the relative motor control signal between 0 and 1.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 1.0] (0.1)`
- 默认值：`0.0`
- 单位：``


1454. PD_GRIPPER_EN (INT32)
- 名称：PD_GRIPPER_EN (INT32)
- 参数描述：Enable Gripper actuation in Payload Deliverer    Reboot required: True
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1455. PD_GRIPPER_TO (FLOAT)
- 名称：PD_GRIPPER_TO (FLOAT)
- 参数描述：Timeout for successful gripper actuation acknowledgement Comment: Maximum time Gripper will wait while the successful griper actuation isn't recognised. If the gripper has no feedback sensor, it will simply wait for this time before considering gripper actuation successful and publish a 'VehicleCommandAck' signaling successful gripper action
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, ?]`
- 默认值：`3`
- 单位：`s`


1456. PD_GRIPPER_TYPE (INT32)
- 名称：PD_GRIPPER_TYPE (INT32)
- 参数描述：Type of Gripper (Servo, etc.)  Values:-1: Undefined 0: Servo
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 0]`
- 默认值：`0`
- 单位：``


1457. PLD_BTOUT (FLOAT)
- 名称：PLD_BTOUT (FLOAT)
- 参数描述：Landing Target Timeout Comment: Time after which the landing target is considered lost without any new measurements.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 50] (0.5)`
- 默认值：`5.0`
- 单位：`s`


1458. PLD_FAPPR_ALT (FLOAT)
- 名称：PLD_FAPPR_ALT (FLOAT)
- 参数描述：Final approach altitude Comment: Allow final approach (without horizontal positioning) if losing landing target closer than this to the ground.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.1)`
- 默认值：`0.1`
- 单位：`m`


1459. PLD_HACC_RAD (FLOAT)
- 名称：PLD_HACC_RAD (FLOAT)
- 参数描述：Horizontal acceptance radius Comment: Start descending if closer above landing target than this.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 10] (0.1)`
- 默认值：`0.2`
- 单位：`m`


1460. PLD_MAX_SRCH (INT32)
- 名称：PLD_MAX_SRCH (INT32)
- 参数描述：Maximum number of search attempts Comment: Maximum number of times to search for the landing target if it is lost during the precision landing.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0, 100]`
- 默认值：`3`
- 单位：``


1461. PLD_SRCH_ALT (FLOAT)
- 名称：PLD_SRCH_ALT (FLOAT)
- 参数描述：Search altitude Comment: Altitude above home to which to climb when searching for the landing target.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100] (0.1)`
- 默认值：`10.0`
- 单位：`m`


1462. PLD_SRCH_TOUT (FLOAT)
- 名称：PLD_SRCH_TOUT (FLOAT)
- 参数描述：Search timeout Comment: Time allowed to search for the landing target before falling back to normal landing.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100] (0.1)`
- 默认值：`10.0`
- 单位：`s`


1463. RC_CRSF_TEL_EN (INT32)
- 名称：RC_CRSF_TEL_EN (INT32)
- 参数描述：Crossfire RC telemetry enable Comment: Crossfire telemetry enable
  - 翻译：
  - gpt注解：
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1464. RC_INPUT_PROTO (INT32)
- 名称：RC_INPUT_PROTO (INT32)
- 参数描述：RC input protocol Comment: Select your RC input protocol or auto to scan. 参数对照:-1: Auto 0: None 1: PPM 2: SBUS 3: DSM 4: ST24 5: SUMD 6: CRSF 7: GHST
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1, 7]`
- 默认值：`-1`
- 单位：``


1465. RC10_DZ (FLOAT)
- 名称：RC10_DZ (FLOAT)
- 参数描述：RC channel 10 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1466. RC10_MAX (FLOAT)
- 名称：RC10_MAX (FLOAT)
- 参数描述：RC channel 10 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1467. RC10_MIN (FLOAT)
- 名称：RC10_MIN (FLOAT)
- 参数描述：RC channel 10 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1468. RC10_REV (FLOAT)
- 名称：RC10_REV (FLOAT)
- 参数描述：RC channel 10 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1469. RC10_TRIM (FLOAT)
- 名称：RC10_TRIM (FLOAT)
- 参数描述：RC channel 10 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1470. RC11_DZ (FLOAT)
- 名称：RC11_DZ (FLOAT)
- 参数描述：RC channel 11 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1471. RC11_MAX (FLOAT)
- 名称：RC11_MAX (FLOAT)
- 参数描述：RC channel 11 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1472. RC11_MIN (FLOAT)
- 名称：RC11_MIN (FLOAT)
- 参数描述：RC channel 11 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1473. RC11_REV (FLOAT)
- 名称：RC11_REV (FLOAT)
- 参数描述：RC channel 11 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1474. RC11_TRIM (FLOAT)
- 名称：RC11_TRIM (FLOAT)
- 参数描述：RC channel 11 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1475. RC12_DZ (FLOAT)
- 名称：RC12_DZ (FLOAT)
- 参数描述：RC channel 12 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1476. RC12_MAX (FLOAT)
- 名称：RC12_MAX (FLOAT)
- 参数描述：RC channel 12 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1477. RC12_MIN (FLOAT)
- 名称：RC12_MIN (FLOAT)
- 参数描述：RC channel 12 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1478. RC12_REV (FLOAT)
- 名称：RC12_REV (FLOAT)
- 参数描述：RC channel 12 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1479. RC12_TRIM (FLOAT)
- 名称：RC12_TRIM (FLOAT)
- 参数描述：RC channel 12 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1480. RC13_DZ (FLOAT)
- 名称：RC13_DZ (FLOAT)
- 参数描述：RC channel 13 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1481. RC13_MAX (FLOAT)
- 名称：RC13_MAX (FLOAT)
- 参数描述：RC channel 13 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1482. RC13_MIN (FLOAT)
- 名称：RC13_MIN (FLOAT)
- 参数描述：RC channel 13 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1483. RC13_REV (FLOAT)
- 名称：RC13_REV (FLOAT)
- 参数描述：RC channel 13 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1484. RC13_TRIM (FLOAT)
- 名称：RC13_TRIM (FLOAT)
- 参数描述：RC channel 13 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1485. RC14_DZ (FLOAT)
- 名称：RC14_DZ (FLOAT)
- 参数描述：RC channel 14 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1486. RC14_MAX (FLOAT)
- 名称：RC14_MAX (FLOAT)
- 参数描述：RC channel 14 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1487. RC14_MIN (FLOAT)
- 名称：RC14_MIN (FLOAT)
- 参数描述：RC channel 14 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1488. RC14_REV (FLOAT)
- 名称：RC14_REV (FLOAT)
- 参数描述：RC channel 14 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1489. RC14_TRIM (FLOAT)
- 名称：RC14_TRIM (FLOAT)
- 参数描述：RC channel 14 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1490. RC15_DZ (FLOAT)
- 名称：RC15_DZ (FLOAT)
- 参数描述：RC channel 15 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1491. RC15_MAX (FLOAT)
- 名称：RC15_MAX (FLOAT)
- 参数描述：RC channel 15 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1492. RC15_MIN (FLOAT)
- 名称：RC15_MIN (FLOAT)
- 参数描述：RC channel 15 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1493. RC15_REV (FLOAT)
- 名称：RC15_REV (FLOAT)
- 参数描述：RC channel 15 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1494. RC15_TRIM (FLOAT)
- 名称：RC15_TRIM (FLOAT)
- 参数描述：RC channel 15 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1495. RC16_DZ (FLOAT)
- 名称：RC16_DZ (FLOAT)
- 参数描述：RC channel 16 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


1496. RC16_MAX (FLOAT)
- 名称：RC16_MAX (FLOAT)
- 参数描述：RC channel 16 maximum Comment: Maximum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[1500.0, 2200.0]`
- 默认值：`2000`
- 单位：`µs`


1497. RC16_MIN (FLOAT)
- 名称：RC16_MIN (FLOAT)
- 参数描述：RC channel 16 minimum Comment: Minimum value for this channel.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 1500.0]`
- 默认值：`1000`
- 单位：`µs`


1498. RC16_REV (FLOAT)
- 名称：RC16_REV (FLOAT)
- 参数描述：RC channel 16 reverse Comment: Set to -1 to reverse channel. 参数对照:-1.0: Reverse 1.0: Normal
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[-1.0, 1.0]`
- 默认值：`1.0`
- 单位：``


1499. RC16_TRIM (FLOAT)
- 名称：RC16_TRIM (FLOAT)
- 参数描述：RC channel 16 trim Comment: Mid point value
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[800.0, 2200.0]`
- 默认值：`1500`
- 单位：`µs`


1500. RC17_DZ (FLOAT)
- 名称：RC17_DZ (FLOAT)
- 参数描述：RC channel 17 dead zone Comment: The +- range of this value around the trim value will be considered as zero.
  - 翻译：
  - gpt注解：
- `[Min, Max]`：`[0.0, 100.0]`
- 默认值：`0.0`
- 单位：``


