# pix4_parameter_reference
> 使用gpt翻译pix4的参数，并且加上gpt的解释

> https://docs.px4.io/main/zh/advanced_config/parameter_reference.html

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
  - 翻译：云台的Mavlink组件ID Comment: 如果MNT_MODE_OUT为MAVLink协议v2，云台的配置/控制命令将使用此组件ID发送。
  - gpt注解：MNT_MAV_COMPID参数用于设置云台的Mavlink组件ID。如果MNT_MODE_OUT使用MAVLink协议v2，云台的配置和控制命令将使用此组件ID进行发送。通常情况下，您可以根据通信协议和系统配置来调整此参数。
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
  - 翻译：手动控制杆垂直指数曲线 Comment: 数值越高，控制杆在零附近的灵敏度越低，同时仍然可以通过全杆偏转达到最大值。 0 纯线性输入曲线 1 纯立方输入曲线
  - gpt注解：MPC_Z_MAN_EXPO参数用于调整手动控制杆的垂直指数曲线。数值越高，控制杆在零附近的灵敏度越低，即在零点附近的控制输入更不敏感，但仍能在全杆偏转时达到最大值。0代表纯线性输入曲线，1代表纯立方输入曲线。通常情况下，您可以根据操纵杆的灵敏度需求来调整此参数。
- `[Min, Max]`：`[0, 1] (0.01)`
- 默认值：`0.6`
- 单位：``


1412. MPC_Z_P (FLOAT)
- 名称：MPC_Z_P (FLOAT)
- 参数描述：Proportional gain for vertical position error Comment: Defined as corrective velocity in m/s per m position error
  - 翻译：垂直位置误差的比例增益 Comment: 定义为每m位置误差的校正速度
  - gpt注解：MPC_Z_P参数用于调整垂直位置误差的比例增益。它被定义为每m位置误差的校正速度，用于控制垂直位置的响应。通常情况下，通过调整此参数，可以影响飞行器对垂直位置误差的响应速度。增大此值将增加响应速度，减小则减小响应速度。请根据飞行任务和性能需求来调整此参数。
- `[Min, Max]`：`[0.1, 1.5] (0.1)`
- 默认值：`1.`
- 单位：``


1413. MPC_Z_VEL_ALL (FLOAT)
- 名称：MPC_Z_VEL_ALL (FLOAT)
- 参数描述：Overall Vertical Velocity Limit Comment: If set to a value greater than zero, other parameters are automatically set (such as MPC_Z_VEL_MAX_UP or MPC_LAND_SPEED). If set to a negative value, the existing individual parameters are used.
  - 翻译：总体垂直速度限制 Comment: 如果设置为大于零的值，将自动设置其他参数（如MPC_Z_VEL_MAX_UP或MPC_LAND_SPEED）。如果设置为负值，将使用现有的各个参数。
  - gpt注解：MPC_Z_VEL_ALL参数用于设置飞行器的总体垂直速度限制。如果将其设置为大于零的值，系统将自动调整其他相关参数，如MPC_Z_VEL_MAX_UP或MPC_LAND_SPEED，以匹配所需的垂直速度限制。如果将其设置为负值，将使用现有的各个参数，而不进行自动调整。通常情况下，您可以根据飞行任务和性能需求来调整此参数，以确保所需的垂直速度限制。
- `[Min, Max]`：`[-3, 8] (0.5)`
- 默认值：`-3.`
- 单位：``


1414. MPC_Z_VEL_D_ACC (FLOAT)
- 名称：MPC_Z_VEL_D_ACC (FLOAT)
- 参数描述：Differential gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s^2 velocity derivative
  - 翻译：垂直速度误差的微分增益 Comment: 定义为每m/s^2速度导数的校正加速度
  - gpt注解：MPC_Z_VEL_D_ACC参数用于调整垂直速度误差的微分增益。它被定义为每m/s^2速度导数的校正加速度，用于控制垂直速度的导数误差。通常情况下，通过调整此参数，可以影响飞行器对垂直速度导数误差的响应速度。增大此值将增加响应速度，减小则减小响应速度。请根据飞行任务和性能需求来调整此参数。
- `[Min, Max]`：`[0, 2] (0.02)`
- 默认值：`0.`
- 单位：``


1415. MPC_Z_VEL_I_ACC (FLOAT)
- 名称：MPC_Z_VEL_I_ACC (FLOAT)
- 参数描述：Integral gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m velocity integral
  - 翻译：垂直速度误差的积分增益 Comment: 定义为每m速度积分的校正加速度
  - gpt注解：MPC_Z_VEL_I_ACC参数用于调整垂直速度误差的积分增益。它被定义为每m速度积分的校正加速度，用于控制垂直速度的积分误差。通常情况下，通过调整此参数，可以影响飞行器对垂直速度积分误差的响应速度。增大此值将增加响应速度，减小则减小响应速度。请根据飞行任务和性能需求来调整此参数。
- `[Min, Max]`：`[0.2, 3] (0.1)`
- 默认值：`2.`
- 单位：``


1416. MPC_Z_VEL_MAX_DN (FLOAT)
- 名称：MPC_Z_VEL_MAX_DN (FLOAT)
- 参数描述：Maximum descent velocity Comment: Absolute maximum for all climb rate controlled modes. In manually piloted modes full stick deflection commands this velocity. For default autonomous velocity see MPC_Z_V_AUTO_UP
  - 翻译：最大下降速度 Comment: 所有爬升速率受控模式的绝对最大值。在手动驾驶模式中，全杆偏转会指令此速度。有关默认的自主模式速度，请参阅MPC_Z_V_AUTO_UP。
  - gpt注解：MPC_Z_VEL_MAX_DN参数用于设置飞行器的最大下降速度。这个值代表了所有爬升速率受控模式的绝对最大速度。在手动驾驶模式下，全杆偏转将命令飞行器以此速度下降。有关默认的自主模式速度，请参阅MPC_Z_V_AUTO_UP参数。通常情况下，您可以根据飞行任务和性能需求来调整此参数，以确保所需的下降速度。
- `[Min, Max]`：`[0.5, 4] (0.1)`
- 默认值：`1.5`
- 单位：`m/s`


1417. MPC_Z_VEL_MAX_UP (FLOAT)
- 名称：MPC_Z_VEL_MAX_UP (FLOAT)
- 参数描述：Maximum ascent velocity Comment: Absolute maximum for all climb rate controlled modes. In manually piloted modes full stick deflection commands this velocity. For default autonomous velocity see MPC_Z_V_AUTO_UP
  - 翻译：最大上升速度 Comment: 所有爬升速率受控模式的绝对最大值。在手动驾驶模式中，全杆偏转会指令此速度。有关默认的自主模式速度，请参阅MPC_Z_V_AUTO_UP。
  - gpt注解：MPC_Z_VEL_MAX_UP参数用于设置飞行器的最大上升速度。这个值代表了所有爬升速率受控模式的绝对最大速度。在手动驾驶模式下，全杆偏转将命令飞行器以此速度上升。有关默认的自主模式速度，请参阅MPC_Z_V_AUTO_UP参数。通常情况下，您可以根据飞行任务和性能需求来调整此参数，以确保所需的上升速度。
- `[Min, Max]`：`[0.5, 8] (0.1)`
- 默认值：`3.`
- 单位：`m/s`


1418. MPC_Z_VEL_P_ACC (FLOAT)
- 名称：MPC_Z_VEL_P_ACC (FLOAT)
- 参数描述：Proportional gain for vertical velocity error Comment: Defined as corrective acceleration in m/s^2 per m/s velocity error
  - 翻译：垂直速度误差的比例增益 Comment: 定义为每m/s速度误差的校正加速度
  - gpt注解：MPC_Z_VEL_P_ACC参数用于调整垂直速度误差的比例增益。它被定义为每m/s速度误差的校正加速度，用于控制垂直速度的响应。通常情况下，通过调整此参数，可以影响飞行器对垂直速度误差的响应速度。增大此值将增加响应速度，减小则减小响应速度。请根据飞行任务和性能需求来调整此参数。
- `[Min, Max]`：`[2, 15] (0.1)`
- 默认值：`4.`
- 单位：``


1419. MPC_Z_V_AUTO_DN (FLOAT)
- 名称：MPC_Z_V_AUTO_DN (FLOAT)
- 参数描述：Descent velocity in autonomous modes Comment: For manual modes and offboard, see MPC_Z_VEL_MAX_DN
  - 翻译：自主模式下的下降速度 Comment: 对于手动模式和离线模式，请参考MPC_Z_VEL_MAX_DN
  - gpt注解：MPC_Z_V_AUTO_DN参数用于设置自主飞行模式下的下降速度。这个速度指定了飞行器在自主模式下向下运动的最大速度。对于手动控制模式和离线模式，请参考MPC_Z_VEL_MAX_DN参数。通常情况下，您可以根据飞行任务和性能需求来调整此参数，以实现所需的下降速度。
- `[Min, Max]`：`[0.5, 4] (0.5)`
- 默认值：`1.5`
- 单位：`m/s`


1420. MPC_Z_V_AUTO_UP (FLOAT)
- 名称：MPC_Z_V_AUTO_UP (FLOAT)
- 参数描述：Ascent velocity in autonomous modes Comment: For manually controlled modes and offboard see MPC_Z_VEL_MAX_UP
  - 翻译：自主模式下的上升速度 Comment: 对于手动控制模式和离线模式，请参考MPC_Z_VEL_MAX_UP
  - gpt注解：MPC_Z_V_AUTO_UP参数用于设置自主飞行模式下的上升速度。这个速度指定了飞行器在自主模式下向上运动的最大速度。对于手动控制模式和离线模式，请参考MPC_Z_VEL_MAX_UP参数。通常情况下，您可以根据飞行任务和性能需求来调整此参数，以实现所需的上升速度。
- `[Min, Max]`：`[0.5, 8] (0.5)`
- 默认值：`3.`
- 单位：`m/s`


1421. SYS_VEHICLE_RESP (FLOAT)
- 名称：SYS_VEHICLE_RESP (FLOAT)
- 参数描述：Responsiveness Comment: Changes the overall responsiveness of the vehicle. The higher the value, the faster the vehicle will react. If set to a value greater than zero, other parameters are automatically set (such as the acceleration or jerk limits). If set to a negative value, the existing individual parameters are used.
  - 翻译：响应性 Comment: 改变飞行器的整体响应性。数值越大，飞行器的反应速度越快。如果设置为大于零的值，将自动设置其他参数（如加速度或跃度限制）。如果设置为负值，将使用现有的各个参数。
  - gpt注解：SYS_VEHICLE_RESP参数用于调整飞行器的整体响应性。通过改变这个值，可以调整飞行器的整体响应速度。较大的值将导致飞行器更快地响应控制输入。如果将其设置为大于零的值，系统将自动调整其他相关参数，如加速度或跃度限制，以匹配所需的响应性。如果将其设置为负值，将使用现有的各个参数，而不进行自动调整。您可以根据飞行任务和性能需求来调整此参数。
- `[Min, Max]`：`[-1, 1] (0.05)`
- 默认值：`-0.4`
- 单位：``


1422. WV_EN (INT32)
- 名称：WV_EN (INT32)
- 参数描述：Enable weathervane
  - 翻译：启用气象尾翼
  - gpt注解：WV_EN参数用于启用或禁用气象尾翼控制功能。气象尾翼是一种用于在风向变化时保持飞行器朝向的控制功能。当启用气象尾翼时，飞行器将根据风向来调整其姿态，以保持稳定的朝向。通常情况下，您可以根据飞行任务和飞行条件来启用或禁用此功能。
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1423. WV_ROLL_MIN (FLOAT)
- 名称：WV_ROLL_MIN (FLOAT)
- 参数描述：Minimum roll angle setpoint for weathervane controller to demand a yaw-rate
  - 翻译：气象尾翼控制器要求偏航速率的最小横摇角设定点
  - gpt注解：WV_ROLL_MIN参数用于设置气象尾翼控制器要求偏航速率的最小横摇角。当横摇角达到此最小值时，气象尾翼控制器才会要求偏航速率来实现所需的控制。通常情况下，您可以根据飞行器的性能要求和环境条件来调整此参数，以确保适当的控制响应。
- `[Min, Max]`：`[0, 5]`
- 默认值：`1.0`
- 单位：`deg`


1424. WV_YRATE_MAX (FLOAT)
- 名称：WV_YRATE_MAX (FLOAT)
- 参数描述：Maximum yawrate the weathervane controller is allowed to demand
  - 翻译：气象尾翼控制器允许要求的最大偏航速率
  - gpt注解：WV_YRATE_MAX参数用于限制气象尾翼控制器可以要求的最大偏航速率。这有助于确保在强风等恶劣气象条件下，飞行器的偏航稳定性。通常情况下，您可以根据飞行器的需求和环境条件来调整此参数，以确保适当的控制。
- `[Min, Max]`：`[0, 120]`
- 默认值：`90.0`
- 单位：`deg/s`


1425. MC_BAT_SCALE_EN (INT32)
- 名称：MC_BAT_SCALE_EN (INT32)
- 参数描述：Battery power level scaler Comment: This compensates for voltage drop of the battery over time by attempting to normalize performance across the operating range of the battery. The copter should constantly behave as if it was fully charged with reduced max acceleration at lower battery percentages. i.e. if hover is at 0.5 throttle at 100% battery, it will still be 0.5 at 60% battery.
  - 翻译：电池电量缩放器 Comment: 通过尝试规范化电池的工作范围，以弥补电池随时间的电压下降。直升机应始终表现得好像它是充满电的，在较低电池百分比下减小最大加速度。即，如果悬停在100%电池时为0.5油门，那么在60%电池时仍将为0.5。
  - gpt注解：MC_BAT_SCALE_EN参数用于调整电池电量对飞行性能的影响。它通过规范化电池的工作范围，以弥补电池随时间的电压下降。这样，飞行器在不同电池电量下仍能保持相对稳定的性能。通常情况下，它使飞行器在较低电池百分比下降低最大加速度，以确保飞行性能不会因电量下降而急剧下降。您可以根据电池的性能和需求来调整此参数。
- `[Min, Max]`：``
- 默认值：`Disabled (0)`
- 单位：``


1426. MC_PITCHRATE_D (FLOAT)
- 名称：MC_PITCHRATE_D (FLOAT)
- 参数描述：Pitch rate D gain Comment: Pitch rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：俯仰速率D增益 Comment: 俯仰速率微分增益。小值有助于减小快速振荡。如果值太大，振荡将再次出现。
  - gpt注解：MC_PITCHRATE_D参数用于调整飞行器的俯仰稳定性，特别是对于控制系统的微分项。小的D增益有助于减少快速振荡，从而提高稳定性。然而，如果D增益值过大，可能会引发振荡问题。请根据实际需求和飞行器性能来调整此参数。
- `[Min, Max]`：`[0.0, ?] (0.0005)`
- 默认值：`0.003`
- 单位：``


1427. MC_PITCHRATE_FF (FLOAT)
- 名称：MC_PITCHRATE_FF (FLOAT)
- 参数描述：Pitch rate feedforward Comment: Improves tracking performance.
  - 翻译：俯仰速率前馈 Comment: 提高跟踪性能。
  - gpt注解：MC_PITCHRATE_FF参数用于改进飞行器的俯仰速率跟踪性能。通过添加前馈项，可以提高控制系统对速度误差的响应，从而改善跟踪性能。通常情况下，将此参数设置为零，以实现基本的反馈控制。但在一些情况下，特别是需要更高性能的飞行任务中，增加前馈可以提高控制的精度和响应速度。请根据实际需求来调整此参数。
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：``


1428. MC_PITCHRATE_I (FLOAT)
- 名称：MC_PITCHRATE_I (FLOAT)
- 参数描述：Pitch rate I gain Comment: Pitch rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：俯仰速率I增益 Comment: 俯仰速率积分增益。可以设置用来补偿静态推力差异或重心偏移。
  - gpt注解：MC_PITCHRATE_I参数用于调整飞行器的俯仰稳定性，特别是对抵消静态推力差异或重心偏移非常有用。增加此值将增加积分响应，以更好地消除稳定性误差。然而，过高的积分增益可能导致积分项过度响应，引入振荡或其他问题。请根据实际需求和飞行器性能来调整此参数。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.2`
- 单位：``


1429. MC_PITCHRATE_K (FLOAT)
- 名称：MC_PITCHRATE_K (FLOAT)
- 参数描述：Pitch rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_PITCHRATE_K * (MC_PITCHRATE_P * error + MC_PITCHRATE_I * error_integral + MC_PITCHRATE_D * error_derivative) Set MC_PITCHRATE_P=1 to implement a PID in the ideal form. Set MC_PITCHRATE_K=1 to implement a PID in the parallel form.
  - 翻译：俯仰速率控制器增益 Comment: 控制器的全局增益。该增益缩放控制器的P、I和D项：output = MC_PITCHRATE_K * (MC_PITCHRATE_P * error + MC_PITCHRATE_I * error_integral + MC_PITCHRATE_D * error_derivative) 设置MC_PITCHRATE_P=1以实现理想形式的PID。设置MC_PITCHRATE_K=1以实现并联形式的PID。
  - gpt注解：MC_PITCHRATE_K参数是控制器的全局增益，它用于缩放控制器的P、I和D项。通过调整此参数，您可以控制控制器的输出响应。通常情况下，将MC_PITCHRATE_P设置为1可实现理想形式的PID控制，而将MC_PITCHRATE_K设置为1可实现并联形式的PID控制。您可以根据您的系统需求来调整这个参数，以实现所需的控制行为。
- `[Min, Max]`：`[0.01, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1430. MC_PITCHRATE_P (FLOAT)
- 名称：MC_PITCHRATE_P (FLOAT)
- 参数描述：Pitch rate P gain Comment: Pitch rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：俯仰速率P增益 Comment: Pitch rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - gpt注解：MC_PITCHRATE_P参数用于调整飞行器的俯仰稳定性。增加此值将增加俯仰速率的响应，降低则减小响应。通常，您可以根据飞行器的性能要求和实际需求来调整此值。较高的值可能导致更敏感的俯仰响应，但也可能引入振荡。
- `[Min, Max]`：`[0.01, 0.6] (0.01)`
- 默认值：`0.15`
- 单位：``


1431. MC_PR_INT_LIM (FLOAT)
- 名称：MC_PR_INT_LIM (FLOAT)
- 参数描述：Pitch rate integrator limit Comment: Pitch rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large pitch moment trim changes.
  - 翻译：俯仰速率积分限制 Comment: 俯仰速率积分限制。可以设置以增加可用积分来对抗干扰，或减少以提高在大俯仰力矩修正后的稳定时间。
  - gpt注解：MC_PR_INT_LIM参数代表俯仰速率的积分限制。您可以调整此值以增加可用的积分来抵消干扰，或减小它以提高在大俯仰力矩修正后的稳定时间。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1432. MC_ROLLRATE_D (FLOAT)
- 名称：MC_ROLLRATE_D (FLOAT)
- 参数描述：Roll rate D gain Comment: Roll rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：横滚速率D增益 Comment: 横滚速率微分增益。较小的值有助于减小快速振荡。如果值过大，振荡将再次出现。
  - gpt注解：MC_ROLLRATE_D参数代表横滚速率的微分增益。较小的值有助于减小快速振荡。如果值过大，振荡将再次出现。
- `[Min, Max]`：`[0.0, 0.01] (0.0005)`
- 默认值：`0.003`
- 单位：``


1433. MC_ROLLRATE_FF (FLOAT)
- 名称：MC_ROLLRATE_FF (FLOAT)
- 参数描述：Roll rate feedforward Comment: Improves tracking performance.
  - 翻译：横滚速率前馈 Comment: 提高跟踪性能。
  - gpt注解：MC_ROLLRATE_FF参数代表横滚速率的前馈项。它用于提高控制系统的跟踪性能。
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：``


1434. MC_ROLLRATE_I (FLOAT)
- 名称：MC_ROLLRATE_I (FLOAT)
- 参数描述：Roll rate I gain Comment: Roll rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：横滚速率I增益 Comment: 横滚速率积分增益。可设置以补偿静态推力差异或重心偏移。
  - gpt注解：MC_ROLLRATE_I参数代表横滚速率的积分增益。您可以调整此值以补偿静态推力差异或重心偏移。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.2`
- 单位：``


1435. MC_ROLLRATE_K (FLOAT)
- 名称：MC_ROLLRATE_K (FLOAT)
- 参数描述：Roll rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_ROLLRATE_K * (MC_ROLLRATE_P * error + MC_ROLLRATE_I * error_integral + MC_ROLLRATE_D * error_derivative) Set MC_ROLLRATE_P=1 to implement a PID in the ideal form. Set MC_ROLLRATE_K=1 to implement a PID in the parallel form.
  - 翻译：横滚速率控制器增益 Comment: 控制器的全局增益。该增益缩放控制器的P、I和D项：输出 = MC_ROLLRATE_K * (MC_ROLLRATE_P * 误差 + MC_ROLLRATE_I * 误差积分 + MC_ROLLRATE_D * 误差导数) 将MC_ROLLRATE_P设置为1以实现理想形式的PID。将MC_ROLLRATE_K设置为1以实现并联形式的PID。
  - gpt注解：MC_ROLLRATE_K参数代表横滚速率控制器的全局增益。该值用于缩放控制器的P、I和D项，从而影响控制输出。您可以将MC_ROLLRATE_P设置为1以实现理想形式的PID控制，将MC_ROLLRATE_K设置为1以实现并联形式的PID控制。
- `[Min, Max]`：`[0.01, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1436. MC_ROLLRATE_P (FLOAT)
- 名称：MC_ROLLRATE_P (FLOAT)
- 参数描述：Roll rate P gain Comment: Roll rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：横滚速率P增益 Comment: 横滚速率比例增益，即角速度误差1弧度/秒的控制输出。
  - gpt注解：MC_ROLLRATE_P参数代表横滚速率的比例增益，也就是角速度误差1弧度/秒时的控制输出。
- `[Min, Max]`：`[0.01, 0.5] (0.01)`
- 默认值：`0.15`
- 单位：``


1437. MC_RR_INT_LIM (FLOAT)
- 名称：MC_RR_INT_LIM (FLOAT)
- 参数描述：Roll rate integrator limit Comment: Roll rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large roll moment trim changes.
  - 翻译：横滚速率积分限制 Comment: 横滚速率积分限制。可以设置以增加可用积分来对抗干扰，或减少以提高在大横滚力矩修正后的稳定时间。
  - gpt注解：MC_RR_INT_LIM参数代表横滚速率的积分限制。您可以调整此值以增加可用的积分来抵消干扰，或减小它以提高在大横滚力矩修正后的稳定时间。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1438. MC_YAWRATE_D (FLOAT)
- 名称：MC_YAWRATE_D (FLOAT)
- 参数描述：Yaw rate D gain Comment: Yaw rate differential gain. Small values help reduce fast oscillations. If value is too big oscillations will appear again.
  - 翻译：偏航速率D增益 Comment: 偏航速率微分增益。较小的值有助于减小快速振荡。如果值过大，振荡将再次出现。
  - gpt注解：MC_YAWRATE_D参数代表偏航速率的微分增益。较小的值有助于减小快速振荡。如果值过大，振荡将再次出现。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.0`
- 单位：``


1439. MC_YAWRATE_FF (FLOAT)
- 名称：MC_YAWRATE_FF (FLOAT)
- 参数描述：Yaw rate feedforward Comment: Improves tracking performance.
  - 翻译：偏航速率前馈 Comment: 提高跟踪性能。
  - gpt注解：MC_YAWRATE_FF参数代表偏航速率的前馈项。它用于提高控制系统的跟踪性能。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.0`
- 单位：``


1440. MC_YAWRATE_I (FLOAT)
- 名称：MC_YAWRATE_I (FLOAT)
- 参数描述：Yaw rate I gain Comment: Yaw rate integral gain. Can be set to compensate static thrust difference or gravity center offset.
  - 翻译：偏航速率I增益 Comment: 偏航速率积分增益。可以设置以补偿静态推力差异或重心偏移。
  - gpt注解：MC_YAWRATE_I参数代表偏航速率的积分增益。您可以调整此值以补偿静态推力差异或重心偏移。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.1`
- 单位：``


1441. MC_YAWRATE_K (FLOAT)
- 名称：MC_YAWRATE_K (FLOAT)
- 参数描述：Yaw rate controller gain Comment: Global gain of the controller. This gain scales the P, I and D terms of the controller: output = MC_YAWRATE_K * (MC_YAWRATE_P * error + MC_YAWRATE_I * error_integral + MC_YAWRATE_D * error_derivative) Set MC_YAWRATE_P=1 to implement a PID in the ideal form. Set MC_YAWRATE_K=1 to implement a PID in the parallel form.
  - 翻译：偏航速率控制增益 Comment: 控制器的全局增益。该增益缩放控制器的P、I和D项：输出 = MC_YAWRATE_K * (MC_YAWRATE_P * 误差 + MC_YAWRATE_I * 误差积分 + MC_YAWRATE_D * 误差导数) 将MC_YAWRATE_P设置为1以实现理想形式的PID。将MC_YAWRATE_K设置为1以实现并联形式的PID。
  - gpt注解：MC_YAWRATE_K参数代表偏航速率控制器的全局增益。该值用于缩放控制器的P、I和D项，从而影响控制输出。您可以将MC_YAWRATE_P设置为1以实现理想形式的PID控制，将MC_YAWRATE_K设置为1以实现并联形式的PID控制。
- `[Min, Max]`：`[0.0, 5.0] (0.0005)`
- 默认值：`1.0`
- 单位：``


1442. MC_YAWRATE_P (FLOAT)
- 名称：MC_YAWRATE_P (FLOAT)
- 参数描述：Yaw rate P gain Comment: Yaw rate proportional gain, i.e. control output for angular speed error 1 rad/s.
  - 翻译：偏航速率P增益 Comment: 偏航速率比例增益，即角速度误差1弧度/秒的控制输出。
  - gpt注解：MC_YAWRATE_P参数代表偏航速率的比例增益，也就是角速度误差1弧度/秒时的控制输出。
- `[Min, Max]`：`[0.0, 0.6] (0.01)`
- 默认值：`0.2`
- 单位：``


1443. MC_YR_INT_LIM (FLOAT)
- 名称：MC_YR_INT_LIM (FLOAT)
- 参数描述：Yaw rate integrator limit Comment: Yaw rate integrator limit. Can be set to increase the amount of integrator available to counteract disturbances or reduced to improve settling time after large yaw moment trim changes.
  - 翻译：偏航速率积分限制 Comment: 偏航速率积分限制。可以设置以增加可用积分来对抗干扰，或减少以提高在大偏航力矩修正后的稳定时间。
  - gpt注解：MC_YR_INT_LIM参数代表偏航速率积分的限制。您可以调整此值以增加可用的积分来抵消干扰，或减小它以提高在大偏航力矩修正后的稳定时间。
- `[Min, Max]`：`[0.0, ?] (0.01)`
- 默认值：`0.30`
- 单位：``


1444. MSP_OSD_CONFIG (INT32)
- 名称：MSP_OSD_CONFIG (INT32)
- 参数描述：Serial Configuration for MSP OSD Comment: Configure on which serial port to run MSP OSD. 参数对照:0: Disabled 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: Radio Controller 301: Wifi Port 401: EXT2 Reboot required: true
  - 翻译：MSP OSD串口配置 Comment: 配置MSP OSD运行在哪个串口上。 参数对照: 0: 禁用 6: UART 6 101: TELEM 1 102: TELEM 2 103: TELEM 3 104: TELEM/SERIAL 4 201: GPS 1 202: GPS 2 203: GPS 3 300: 无线电遥控器 301: Wifi 串口 401: EXT2 需要重新启动: true
  - gpt注解：MSP_OSD_CONFIG参数用于配置MSP OSD运行的串口。可以根据需要选择不同的串口。参数对照中列出了各选项的含义。在更改此参数后，需要重新启动系统生效。
- `[Min, Max]`：``
- 默认值：`0`
- 单位：``


1445. OSD_ATXXXX_CFG (INT32)
- 名称：OSD_ATXXXX_CFG (INT32)
- 参数描述：Enable/Disable the ATXXX OSD Chip Comment: Configure the ATXXXX OSD Chip (mounted on the OmnibusF4SD board) and select the transmission standard. 参数对照: 0: Disabled 1: NTSC 2: PAL Reboot required: true
  - 翻译：启用/禁用ATXXX OSD芯片 Comment: 配置安装在OmnibusF4SD板上的ATXXX OSD芯片，并选择传输标准。 参数对照: 0: 禁用 1: NTSC 2: PAL 需要重新启动: true
  - gpt注解：OSD_ATXXXX_CFG参数用于启用或禁用ATXXX OSD芯片，以及配置其传输标准。该芯片通常安装在OmnibusF4SD板上。参数对照列出了不同选项的含义。在更改此参数后，需要重新启动系统生效。
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
  - 翻译：电机最小上升时间（斜升速率限制） Comment: 允许电机输入信号通过1000 PWM单位范围所需的最短时间。值x表示电机信号至少需要x秒从1000 PWM上升到2000 PWM。零表示斜升速率限制已禁用。
  - gpt注解：MOT_SLEW_MAX参数代表电机的最小上升时间，即允许电机输入信号在1000 PWM单位范围内的最短时间。值x表示电机信号至少需要x秒从1000 PWM上升到2000 PWM。零表示斜升速率限制已禁用。
- `[Min, Max]`：`[0.0, ?]`
- 默认值：`0.0`
- 单位：`s/(1000*PWM)`


1452. PWM_SBUS_MODE (INT32)
- 名称：PWM_SBUS_MODE (INT32)
- 参数描述：S.BUS out Comment: Set to 1 to enable S.BUS version 1 output instead of RSSI.
  - 翻译：S.BUS输出 Comment: 设置为1以启用S.BUS版本1输出，而不是RSSI。
  - gpt注解：PWM_SBUS_MODE参数用于控制S.BUS输出。将其设置为1以启用S.BUS版本1输出，而不是RSSI。
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


