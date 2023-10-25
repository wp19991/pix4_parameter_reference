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


