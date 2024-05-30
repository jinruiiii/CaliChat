
# LLM 1 prompt
system_message_key_components_prompt = """
**Task:** Your task is to analyze the given text information and extract a list of information.

**Instructions**
    1. The input text will be about a calibration certificate. Your job would be to extract the following information in the exact format, without any other information.
        1a. Name of the instrument calibrated.
        1b. Model Number of the instrument calibrated.
        1c. Serial number of the instrument calibrated.
        1d. Calibration date of the instrument calibrated.
        1e. Device used to calibrate the instrument.
        1f. Model number of the device used to calibrate the instrument.
        1g. Serial number of the device used to calibrate the instrument.
        1h. Due Date of the device used to calibrate the instrument.
    2. Always give a reply in the exact format.
    3. If unsure about some information, just put "Not Mentioned" for that information.
    4. Can be assumed that the due date of the calibration instrument is exactly 1 year after the calibration date of the calibration instrument.
    5. Strictly only extract the above information. Do not extract other information that are not mentioned and do not add additional notes.
    6. Please note: when referring to the date of calibration, specify the day on which the instrument itself is calibrated, not the day on which the calibrated device is calibrated.
    7. The input text originated from a PDF file and was processed line by line, possibly resulting in inaccuracies. Please do your best to interpret and provide the most accurate output.
    8. Below is a list of examples. Strictly follow the format of the examples provided.
    
**Text Information Example 1**

    23 Tagore Lane, #04-08/09/10/11 Tagore 23 Warehouse, Si 787601 vada ~
    
    'agore Lane, fagore farehouse, Singapore . ue
    
    Tol: (65) 6452 0300 | Fax: (65) 6452 0500 Name: MAUR ce. cam www.caltekgroup.com | info@caltekgruop.com
    
    CALIBRATION CERTIFICATE
    
    CERTIFICATE NUMBER : CTE 2299M-23 JOB NUMBER : CTJ 23-4275 DATE RECEIVED > 13-Jun-23 ISSUE DATE : 21-Jun-23 Instrument : DC POWER SUPPLY Ambient Temperature : (23+5)°C Manufacturer : Ti Relative Humidity : (65+ 10) % rh. Model No. > QL355T Date Calibrated : 21-Jun-23 Part No. to Recommended Due Date: 21-Jun-24 Serial No. > 243382 Customer : DSO NATIONAL LABORATORIES Range i
    
    12 Science Park Drive ( Tag No. ) : DO 3701-056(15)
    
    Singapore 118225 Page : 1of 3
    
    Status : As Found
    
    a
    The described instrument has been calibrated at Caltek Laboratory under the ambient conditions stated above.
    
    This certificate provides traceability of measurement to the International System of Units (SI) and/or to units of measurement realised at the National Metrology Centre (NMC) , Singapore or other recognized national metrology institutes.
    
    METHOD : The calibration method was carried out according to In-house Technical Calibration Procedure CTTM - E06:2007 as a guide.
    
    REFERENCE INSTRUMENT(S) SERIAL NO DUE DATE 4. Digital Precision Multimeter 3501005 15-Sep-23 RESULTS OF CALIBRATION
    
    1. The results of calibration are given on the attached calibration data sheet(s). 2. The expanded uncertainty of measurement associated with the calibration is
    estimated at a level of confidence of approximately 95 % with a coverage factor of k=2.00. 3. | The user should determine the suitability of the instrument for its intended use.
    
    Calibrated by : Approved by : SHAHID é APPANNA. N. R EMP ID : 1258 EMP ID : 1024
    
    This certificate may not be reproduced other than in full, except with the prior written approval of the issuing Laboratory
    
    CERTIFICATE NUMBER
    
    ISSUE DATE
    
    Function Test/ Instrument Readin
    
    Range
    
    OUTPUT 1 15V/5A DC VOLTAGE TEST 15 15 15 DC CURRENT TEST 5 5 5 35V/3A DC VOLTAGE TEST 35 35 35 DC CURRENT TEST 3 3 3 35V / 500mA DC VOLTAGE TEST 35 35 35 DC CURRENT TEST 500 500 500
    
    1.500 7.500 13.500
    
    0.500 2.500 4.500
    
    3.500 17.500 31.500
    
    0.300 1.500 2.700
    
    3.500 17.500 31.500
    
    50.0 250.0 450.0
    
    : CTE 2299M-23 2 21-Jun-23
    
    Unit
    
    <
    mA mA mA
    
    Mean Reference Reading
    
    1.5020 7.5042 13.5064
    
    0.5000 2.4995 4.4992
    
    3.5028 17.5076 31.5118
    
    0.3000 1.4997 2.6994
    
    3.5030 17.5083 31.5129
    
    50.01 249.91 449.79
    
    CALIBRATION CERTIFICATE
    
    JOB NUMBER : CTJ 23-4275
    
    PAGE : 2 of 3 Low Limit High Limit
    
    1.4946 1.5055 7.4928 7.5073 13.4910 13.5091 0.4940 0.5060 2.4900 2.5100 4.4860 4.5140 3.4940 3.5061 17.4898 17.5103 31.4856 31.5145 0.2944 0.3056 1.4920 1.5080 2.6896 2.7104 3.4940 3.5061 17.4898 17.5103 31.4856 31.5145
    
    49.40 50.60 249.00 251.00 448.60 451.40
    
    CALIBRATION CERTIFICATE
    
    CERTIFICATE NUMBER : CTE 2299M-23 JOB NUMBER: CTV 23-4275 ISSUE DATE 2 21-Jun-23 PAGE : 3 of 3
    
    Function Test/ Instrument
    Range Readin Unit Mean Reference Reading Low Limit High Limit OUTPUT 2 15V/5A OC VOLTAGE TEST 15 1.500 Vv 1.4975 1.4946 1.5055 15 7.500 Vv 7.4989 7.4928 7.5073 15 13.500 Vv 13.5009 13.4910 13.5091 DC CURRENT TEST 5 0.500 A 0.4986 0.4940 0.5060 5 2.500 A 2.4962 2.4900 2.5100 5 4.500 A 4.4941 4.4860 4.5140 35V/3A DC VOLTAGE TEST 35 3.500 Vv 3.4981 3.4940 3.5061 35 17.500 Vv 17.5020 17.4898 17.5103 35 31.500 Vv 31.5057 31.4856 31.5145 DC CURRENT TEST 3 0.300 A 0.2988 0.2944 0.3056 3 1.500 A 1.4974 1.4920 1.5080 3 2.700 A 2.6960 2.6896 2.7104 35V / 500mA DC VOLTAGE TEST 35 3.500 Vv 3.4984 3.4940 3.5061 35 17.500 Vv 17.5028 17.4898 17.5103 35 31.500 Vv 31.5070 31.4856 31.5145 DC CURRENT TEST 500 50.0 mA 50.01 49.40 50.60 500 250.0 mA 249.96 249.00 251.00 500 450.0 mA 449.88 448.60 451.40
    FUNCTION TEST RANGE EXPANDED UNCERTAINTY DC Voltage 15V 0.0001 V (3.5 - 31.5) V 0.0006 V DC Current (50 - 450) mA 0.30 mA
    (0.3-5)A 0.007 A

**Output Format Example 1**
    --Information of Instrument Calibrated--
    Instrument Calibrated: DC Power Supply
    Model Number of Calibrated Instrument: QL355T
    Serial Number of Calibrated Instrument: 243382
    Date of Calibration: June 21st, 2023

    --Information of Calibration Device 1--
    Calibration Device: Digital Precision Multimeter
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: 3501005
    Due Date of Calibration Device: September 15th, 2023

**Example Output Explanation 1**
    - The instrument calibrated is the DC Power Supply.
    - The model number of the DC Power Supply is QL355T.
    - The serial number of the DC Power Supply is 243382.
    - The date of calibration of the DC Power Supply is on June 21st, 2023.
    - The device used to calibrated the DC Power Supply is the Digital Precision Multimeter.
    - The model number of the Digital Precision Multimeter is not mentioned.
    - The serial number of the Digital Precision Multimeter is 3501005.
    - The due date of the Digital Precision Multimeter is September 15th, 2023.
    - The Digital Precision Multimeter is th only calibration device present for the DC Power Supply.

**Text Information Example 2**

    1 Sunview Road #04-06 Eco-Tech @ Sunview Singapore 627615
    
    Tel: (65) 6262 3707
    
    Fax: (65) 6254 4388
    
    Email: pbiztech@singnet.com.sg
    
    Website: www.probiz.com.sg
    
    ProBiz Technology Pte Ltd Reg No: 200000582N
    
    Accredited Laboratory SAC-SINGLAS CALIBRATION REPORT SINGLAS Report No. : 23SC-PBT 3835 Page 1 of 4 Calibrated For : DSO National Laboratories Date: 03 May 2023 12 Science Park Drive Singapore 118225 Attention : Mr. Edison Seah (Tel: 64504404) Chamber Type : MMM Oven Ambient Temperature : (2341) °C Model :VC 111 ECO Relative Humidity 2 (63 +3) %rh Serial No. > H190449
    
    Date of calibration: 02 May 2023 Location of Calibration : On-site
    DESCRIPTION OF CALIBRATION The enclosure was calibrated using 10 temperature sensors together with a temperature recorder. The locations of the 10 temperature
    
    sensors are shown in Fig.1 on page 2. The enclosure was tested without load at a given set points of +125 °C, +150 °C & +200 °C. The test results were then recorded via the
    
    temperature recorder when the temperature has stabilized at its' set temperature. The method of calibration was carried out as per our Work Instruction (WI-01/Rev 5). The equipment used to calibrate the enclosure is traceable to national standards through National Metrology Center, Singapore and recognized accredited laboratories and the details are as follows.
    1) Yokogawa Recorder with TC Sensors Model : FX1012-7-2-L SIN: S5W211878 CERTIFIED CORRECT Probe S/N : 1 to 10
    
    Report No : CM-216306/10/1 MAY Date Calibrated : 17 Jun 2022 (Sign & Date)
    
    Name:__MAURICE KAM
    
    RESULTS OF CALIBRATION
    
    The results reported herein have been performed in accordance with the laboratory's terms of accreditation under the Singapore
    
    Accreditation Council.
    
    The results of calibration are shown on pages 3 to 4 of this report. The end user should determine the suitability of this equipment for its intended use. The expanded uncertainties of measurement associated with this calibration are estimated at a level of confidence of approximately 95%, which is associated with Overall Average Temperature readings. The re-calibration interval should be determined
    based on the user's requirements.
    
    Calibrated By / Approved By / Ong Lai Heng Mark Poh
    
    Calibration Officer Product Manager
    
    This report shall not be reproduced wholly or in part and no reference shall be made by the Clients to ProBiz Technology Pte Ltd or to the reports or results furnished by ProBiz Technology Pte Ltd in any advertisement or sales promotion,
    
    CONFIDENTIAL
    
    1 Sunview Road #04-06 Eco-Tech @ Sunview Singapore 627615
    
    Tel: (65) 6262 3707
    
    Fax: (65) 6254 4388
    
    Email: pbiztech@singnet.com.sg
    
    Website: www.probiz.com.sg
    
    ProBiz Technology Pte Ltd Reg No: 200000582N
    
    Report No.: 23SC-PBT 3835 Page 2 of 4
    
    q2L AIA
    
    4b
    
    Tp 1 to 9 - Temperature sensors (CH 1~9) L= length Tp 10 - Place near control sensor (CH 10) w=width h=height
    Figure 1. Location of Temperature sensors in the enclosure
    
    be
    
    Calibrated By / Ong Lai Heng Calibration Officer
    
    CONFIDENTIAL
    
    Pro iz Technology Pte Ltd
    
    1 Sunview Road #04-06 Eco-Tech @ Sunview Singapore 627615
    
    Tel: (65) 6262 3707
    
    Fax: (65) 6254 4388
    
    Email: pbiztech@singnet.com.sg
    
    Website: www.probiz.com.sg
    
    Reg No: 200000582N
    Report No.: 23SC-PBT 3835 Page 4 of 4 Calibration Result int when oven had stabilized at +200 °C Sensor No. Max. Temperature (°C) Min. Temperature (°C) Differences (°C) Averaae Temperature Value (°C) To 4 203.8 203.3 0.5 203.6 To2 202.0 201.3 0.7 201.7 To3 201.4 200.9 0.5 201.1 To 4 204.4 203.7 0.7 204.1 Tod 202.9 202.5 0.4 202.7 To 6 201.7 201.1 0.6 201.5 Te7 203.1 202.5 06 202.7 Tos 204.5 203.7 0.8 204.1 To9 203.5 202.8 0.7 203.0 To 10 202.8 202.2 0.6 202.5 Temperature Average Indicated Overall Average Temperature Expanded Uncertainty Coverage Setting Temperature Reading § Temperature Reading Gradient of Measurement Factor CC) (°C) (°C) (CC) (°C) (k) 200.0 200.0 202.7 3.0 2.9 2.25
    
    The average of the 9 averages of 30 readings of each temperature sensor
    The highest average temperature values minus the lowest average temperature values
    
    (based on sensors' distribution shown in Fig 1).
    
    “
    
    Calibrated By / Ong Lai Heng Calibration Officer CONFIDENTIAL
    
    Pro iz Technology Pte Ltd
    
    1 Sunview Road #04-06 Eco-Tech @ Sunview Singapore 627615
    
    Tel: (65) 6262 3707
    
    Fax: (65) 6254 4388
    
    Email: pbiztech@singnet.com.sg
    
    Website: www.probiz.com.sg
    
    Reg No: 200000582N
    Report No.: 23SC-PBT 3835 Page 4 of 4 Calibration Result int when oven had stabilized at +200 °C Sensor No. Max. Temperature (°C) Min. Temperature (°C) Differences (°C) Averaae Temperature Value (°C) To 4 203.8 203.3 0.5 203.6 To2 202.0 201.3 0.7 201.7 To3 201.4 200.9 0.5 201.1 To 4 204.4 203.7 0.7 204.1 Tod 202.9 202.5 0.4 202.7 To 6 201.7 201.1 0.6 201.5 Te7 203.1 202.5 06 202.7 Tos 204.5 203.7 0.8 204.1 To9 203.5 202.8 0.7 203.0 To 10 202.8 202.2 0.6 202.5 Temperature Average Indicated Overall Average Temperature Expanded Uncertainty Coverage Setting Temperature Reading § Temperature Reading Gradient of Measurement Factor CC) (°C) (°C) (CC) (°C) (k) 200.0 200.0 202.7 3.0 2.9 2.25
    
    The average of the 9 averages of 30 readings of each temperature sensor
    The highest average temperature values minus the lowest average temperature values
    
    (based on sensors' distribution shown in Fig 1).
    
    “
    
    Calibrated By / Ong Lai Heng Calibration Officer CONFIDENTIAL

**Output Format Example 2**
    --Information of Instrument Calibrated--
    Instrument Calibrated: MMM Oven
    Model Number of Calibrated Instrument: VC 111 ECO
    Serial Number of Calibrated Instrument: H190449
    Date of Calibration: May 2nd, 2023

    --Information of Calibration Device 1--
    Calibration Device: Yokogawa Recorder with TC Sensors
    Model Number of Calibration Device: FX1012-7-2-L
    Serial Number of Calibration Device: S5W211878
    Due Date of Calibration Device: June 17, 2023

**Example Output Explanation 2**
    - The instrument calibrated is the MMM Oven.
    - The model number of the MMM Oven is VC 111 ECO.
    - The serial number of the MMM Oven is H190449.
    - The date of calibration of the MMM Oven is on May 2nd, 2023.
    - The device used to calibrated the MM Oven is the Yokogawa Recorder with TC Sensors.
    - The model number of the Yokogawa Recorder with TC Sensors is FX1012-7-2-L.
    - The serial number of the Yokogawa Recorder with TC Sensors is S5W211878.
    - The calibration date of Yokogawa Recorder with TC Sensors is June 17, 2022, so it can be inferred that the due date is 1 year later which is June 17 2023.
    - The Yokogawa Recorder with TC Sensors is the only calibration device present for the MMM Oven.

**Text Information 3**
    Certificate of Calibration ISO/IEC 17025:2005 and ANSI/NCSL Z540.3-2006
    Certificate Number 1-6681416900-1
    Model Number Manufacturer Description Serial Number Customer Asset No.
    34401A Keysight Technologies Inc Digital multimeter, 6.5 digit MY44007940 34401A07940
    Customer
    Keysight Technologies (China) Co Ltd No 3 North Wangjing Rd SSU BEIJING 100102, China
    Date of Calibration Procedure Temperature Humidity
    13 Mar 2015 STE-50111013-D.01.01 (23 ± 5) °C (45 ± 25) %RH
    Location of Calibration
    Keysight Technologies (China) Co., Ltd. Shanghai Calibration Laboratory 16F Litong Plaza No.1350 North Sichuan Road Hongkou District Shanghai 200080, China
    This certifies that the equipment has been calibrated using applicable Keysight Technologies procedures and in compliance with ISO/IEC 17025:2005 and ANSI/NCSL Z540.3-2006. The quality management system is registered to ISO 9001:2015. This calibration report is composed of a certificate of calibration, performance test results and/or certificate appendices. Each report section is numbered separately.
    As Received Conditions The measured values of the equipment were observed in specification at the points tested. Additionally, the expanded measurement uncertainty intervals about the measured values were in specification.
    Action Taken - No corrective actions were necessary.
    As Completed Conditions The measured values of the equipment were observed in specification at the points tested. Additionally, the expanded measurement uncertainty intervals about the measured values were in specification.
    Remarks or Special Requirements
    This calibration certificate may refer to instruments manufactured by HP, Agilent and Keysight as being manufactured by Keysight Technologies, Inc.
    The test limits stated in the report correspond to the published specifications of the equipment, at the points tested.
    Based on the customer's request, the next calibration is due on 13 Mar 2016.
    Keysight Technologies (China) Co., Ltd. Shanghai Calibration Laboratory 16F Litong Plaza No.1350 North Sichuan Road Hongkou District Shanghai 200080, China
    Yao Yu - Authorized Signatory
    Issue Date 27 Feb 2016
    Page 1 of 9
    Certificate of Calibration ISO/IEC 17025:2005 and ANSI/NCSL Z540.3-2006
    Certificate Number 1-6681416900-1
    Traceability Information
    Technician ID Number 00828878
    Measurements are traceable to the International System of Units (SI) via national metrology institutes (www.keysight.com/find/NMI) that are signatories to the CIPM Mutual Recognition Arrangement.
    This certificate shall not be reproduced, except in full, without prior written approval of the laboratory.
    Calibration Equipment Used
    Model Number Model Description 33250A 5720A 5725A
    Function/Arbitrary Waveform Generator, 80 MHz Calibrator Amplifier
    Equipment ID 33250A30313 5720A9265204 5725A9248007
    Cal Due Date 31 Oct 2015 19 Apr 2015 19 Apr 2015
    Certificate Number 1-6300833966-1 1-5893705364-1 1-5893705728-1
    Traceability Table
    Model
    W 33250A
    R 1395B-0.4
    R 5700A R E8257D
    W,R 5720A
    W,R 5725A
    Model Description Function/Arbitrary Waveform Generator, 80 MHz THERMAL VOLTAGE CONVERTER AC DC Calibrator PSG Analog Signal Generator Calibrator
    Amplifier
    Equipment ID 33250A30313
    Certificate Number
    1-6300833966-1
    Trace Value
    1395B19477
    1-5893737356-1-ACLASS:AC-1813 AC Voltage
    5700A5550002 1-6032189977-1-CNAS:L0628 E8257D30137 1-4507320100-1-CNAS:L0640 5720A9265204 1-5893705364-1-CNAS:L0628
    5725A9248007 1-5893705728-1-CNAS:L0628
    DC Voltage Frequency AC Current AC Voltage DC Current DC Voltage Resistance AC Current AC Voltage DC Current
    Legend
    W - Working Standard The calibration equipment used for the calibration of the Model indicated on the first page of the Certificate of calibration. R - Reference Standard The Reference Standard (Accredited or NMI-calibrated ETE) used to provide traceability to the SI-Units for the calibration parameters listed.
    Page 2 of 9
    Certificate of Calibration ISO/IEC 17025:2005 and ANSI/NCSL Z540.3-2006
    Certificate Number 1-6681416900-1
    Compliance with Specification
    The uncertainty of measurement has been taken into account when determining compliance with specification, as per ILAC-G8:03/2009. If the expanded measurement uncertainty intervals centered about one or more measured values were both in as well as out of specification (upper or lower), it is not possible to state compliance or non-compliance based on a 95% coverage probability for the expanded measurement uncertainty.
    An overall statement of compliance for all tests performed as received, and as completed (if any adjustments / repairs were performed) is included at the beginning of this report. Statements of compliance apply only to warranted specifications. When functional verification tests are performed, results are reported in the “Functional Test” section, and do not affect these statements of compliance. The status summaries relate to the tested item only. A final decision about whether the item's performance actually satisfies requirements of the user can only be made by the user.
    Measurement results are reported as:
    Passed ( ) - The measured values of the equipment were observed in specification at the points tested. Additionally, the expanded measurement uncertainty intervals about the measured values were in specification.
    Undetermined (U) - The expanded measurement uncertainty intervals about one or more measured values were in as well as out of specification. Consequently, neither compliance nor non-compliance with specification can be declared based on the stated coverage probability.
    Failed (F) - One or more measured values of the equipment were observed out of specification at the points tested. Additionally, the expanded measurement uncertainty intervals about one or more measured values were entirely outside the specification.
    Upper Specification
    Nominal
    Lower Specification
    Measurement Result
    Passed ( )
    Undetermined (U)
    Undetermined (U)
    Failed (F)
    ( ) This result is indicated on the measurement report as a blank space in the column labeled “Status” or “Sts”. MU = 95% expanded measurement uncertainty.
    Acceptance Limit
    The "Keysight Cal + Uncertainties + Guardbanding" service employs a guard band in the amount of the 95% expanded measurement uncertainty (MU). The resulting acceptance limit applied for Pass or Fail decisions, and for performing adjustments, is the difference of the specification and the guard band.
    Uncertainty of Measurement
    The uncertainty evaluation has been performed in accordance with ISO/IEC Guide 98-3:2008 (GUM). The reported expanded measurement uncertainty, which corresponds to a coverage probability of approximately 95%, is the standard uncertainty multiplied by the coverage factor k=2. Where this is not the case, coverage factor (k), effective degrees of freedom (veff) and coverage probability (p) are stated.
    Page 3 of 9
    Certificate of Calibration ISO/IEC 17025:2005 and ANSI/NCSL Z540.3-2006
    Certificate Number 1-6681416900-1
    Performance Test Results Summary
    Test Name
    ZERO OFFSET - FRONT TERMINALS ZERO OFFSET - REAR TERMINALS DC VOLTS AC VOLTS FREQUENCY OHMS DC CURRENT AC CURRENT
    As Received Status Passed Passed Passed Passed Passed Passed Passed Passed
    Page 4 of 9
    Measurement Report Certificate Number 1-6681416900-1
    Model 34401A Options Tested
    Serial MY44007940
    Firmware Rev
    ZERO OFFSET - FRONT TERMINALS
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    Range Input (Front) ------- ------- DC Volts Zero Offset 100 mV 0 V 1 V 0 V 10 V 0 V 100 V 0 V 1000 V 0 V
    –3.5 uV –7 uV –0.05 mV –0.6 mV –10 mV
    0.6 uV 1 uV 0.00 mV 0.0 mV 0 mV
    3.5 uV 7 uV 0.05 mV 0.6 mV 10 mV
    Range Input (Front) -------- ------- 4-Wire Ohms Zero Offset 100 Ohm 0 Ohm 1 kOhm 0 Ohm 10 kOhm 0 Ohm 100 kOhm 0 Ohm 1 MOhm 0 Ohm 10 MOhm 0 Ohm 100 MOhm 0 Ohm
    –4.0 mOhm –10 mOhm –0.10 Ohm –1.0 Ohm –10 Ohm –0.10 kOhm –10.0 kOhm
    0.5 mOhm 1 mOhm 0.01 Ohm 0.1 Ohm 0 Ohm 0.00 kOhm 0.0 kOhm
    4.0 mOhm 10 mOhm 0.10 Ohm 1.0 Ohm 10 Ohm 0.10 kOhm 10.0 kOhm
    Range Input (Front) -------- ------- 2-Wire Ohms Zero Offset 100 Ohm 0 Ohm 1 kOhm 0 Ohm 10 kOhm 0 Ohm 100 kOhm 0 Ohm 1 MOhm 0 Ohm 10 MOhm 0 Ohm 100 MOhm 0 Ohm
    –204.0 mOhm –210 mOhm –0.30 Ohm –1.2 Ohm –10 Ohm –0.10 kOhm –10.0 kOhm
    9.6 mOhm 10 mOhm 0.02 Ohm 0.1 Ohm 0 Ohm 0.00 kOhm 0.0 kOhm
    204.0 mOhm 210 mOhm 0.30 Ohm 1.2 Ohm 10 Ohm 0.10 kOhm 10.0 kOhm
    Range Input (Front) -------- ------- DC Current Zero Offset 10 mA 0 A 100 mA 0 A 1 A 0 A 3 A 0 A
    –2.00 uA –5.0 uA –100 uA –600 uA
    0.03 uA 0.0 uA 0 uA –1 uA
    2.00 uA 5.0 uA 100 uA 600 uA
    Test Date 13 Mar 2015 Condition As Received
    Passed
    UNCERT.
    Status
    1.1 uV 1.2 uV 6.6 uV 0.17 mV 0.74 mV
    1.2 mOhm 1.2 mOhm 0.014 Ohm 0.13 Ohm 0.68 Ohm 0.011 kOhm 0.058 kOhm
    3.0 mOhm 3.3 mOhm 8.4 mOhm 0.068 Ohm 1.3 Ohm 7.8 Ohm 0.058 kOhm
    0.16 uA 0.21 uA 7.0 uA 11 uA
    Page 5 of 9
    Measurement Report Certificate Number 1-6681416900-1
    Model 34401A Options Tested
    Serial MY44007940
    Firmware Rev
    Test Date 13 Mar 2015 Condition As Received
    ZERO OFFSET - REAR TERMINALS
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    UNCERT.
    Sts
    Range Input (Rear) ------- ------- DC Volts Zero Offset 100 mV 0 V 1 V 0 V 10 V 0 V 100 V 0 V 1000 V 0 V
    –3.5 uV –7 uV –0.05 mV –0.6 mV –10 mV
    –1.3 uV –1 uV 0.00 mV 0.0 mV 0 mV
    3.5 uV 7 uV 0.05 mV 0.6 mV 10 mV
    0.88 uV 0.91 uV 6.1 uV 0.074 mV 0.61 mV
    Range Input (Rear) -------- ------- 4-Wire Ohms Zero Offset 100 Ohm 0 Ohm 1 kOhm 0 Ohm 10 kOhm 0 Ohm 100 kOhm 0 Ohm 1 MOhm 0 Ohm 10 MOhm 0 Ohm 100 MOhm 0 Ohm
    –4.0 mOhm –10 mOhm –0.10 Ohm –1.0 Ohm –10 Ohm –0.10 kOhm –10.0 kOhm
    0.3 mOhm 0 mOhm 0.00 Ohm 0.1 Ohm 1 Ohm 0.00 kOhm 0.1 kOhm
    4.0 mOhm 10 mOhm 0.10 Ohm 1.0 Ohm 10 Ohm 0.10 kOhm 10.0 kOhm
    1.1 mOhm 0.82 mOhm 8.3 mOhm 0.16 Ohm 0.98 Ohm 6.3 Ohm 0.058 kOhm
    Range Input (Rear) -------- ------- 2-Wire Ohms Zero Offset 100 Ohm 0 Ohm 1 kOhm 0 Ohm 10 kOhm 0 Ohm 100 kOhm 0 Ohm 1 MOhm 0 Ohm 10 MOhm 0 Ohm 100 MOhm 0 Ohm
    –204.0 mOhm –210 mOhm –0.30 Ohm –1.2 Ohm –10 Ohm –0.10 kOhm –10.0 kOhm
    7.3 mOhm 7 mOhm 0.00 Ohm –0.1 Ohm 0 Ohm 0.00 kOhm 0.0 kOhm
    204.0 mOhm 210 mOhm 0.30 Ohm 1.2 Ohm 10 Ohm 0.10 kOhm 10.0 kOhm
    6.1 mOhm 5.8 mOhm 7.2 mOhm 0.068 Ohm 0.60 Ohm 0.0097 kOhm 0.058 kOhm
    Range Input (Rear) -------- ------- DC Current Zero Offset 10 mA 0 A 100 mA 0 A 1 A 0 A 3 A 0 A
    –2.00 uA –5.0 uA –100 uA –600 uA
    0.04 uA 0.0 uA 1 uA 1 uA
    2.00 uA 5.0 uA 100 uA 600 uA
    5.8 nA 0.21 uA 4.7 uA 8.7 uA
    DC VOLTS
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    UNCERT.
    Status
    Range Input(Front) 100 mV 100 mV 1 V 1 V
    99.9915 mV 0.999953 V
    99.9975 mV 0.999996 V
    100.0085 mV 1.000047 V
    0.0029 mV 0.0000070 V
    Page 6 of 9
    Measurement Report Certificate Number 1-6681416900-1
    Model 34401A Options Tested
    Serial MY44007940
    Firmware Rev
    DC VOLTS (cont.) TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    10 V 10 V 10 V -10 V 100 V 100 V 1000 V 1000 V
    9.99960 V –10.00040 V 99.9949 V 999.945 V
    10.00000 V –10.00001 V 99.9984 V 999.987 V
    10.00040 V –9.99960 V 100.0051 V 1000.055 V
    AC VOLTS
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    Input Freq. (Front) ------- ------- 100 mV Range 10 mV 1 kHz 100 mV 1 kHz 100 mV 50 kHz
    9.9540 mV 99.9000 mV 99.8300 mV
    10.0029 mV 99.9902 mV 100.0389 mV
    10.0460 mV 100.1000 mV 100.1700 mV
    Input Freq. (Front) ------- ------- 1 V Range 1 V 20 Hz 1 V 1 kHz 1 V 20 kHz 1 V 50 kHz 1 V 100 kHz 1 V 300 kHz
    0.999100 V 0.999100 V 0.999100 V 0.998300 V 0.993200 V 0.955000 V
    0.999657 V 0.999921 V 0.999967 V 1.000147 V 1.000079 V 0.994971 V
    1.000900 V 1.000900 V 1.000900 V 1.001700 V 1.006800 V 1.045000 V
    Input Freq. (Front) ------- ------- 10 V Range 100 mV 1 kHz 1 V 1 kHz 10 V 10 Hz 10 V 1 kHz 10 V 50 kHz
    86.94 mV 0.99640 V 9.99100 V 9.99100 V 9.98300 V
    100.86 mV 0.99991 V 9.99741 V 9.99892 V 10.00418 V
    113.06 mV 1.00360 V 10.00900 V 10.00900 V 10.01700 V
    Input Freq. (Front) ------- ------- 100 V Range 100 V 1 kHz 100 V 50 kHz
    99.9100 V 99.8300 V
    100.0064 V 100.0400 V
    100.0900 V 100.1700 V
    Input Freq. (Front) ------- ------- 750 V Range 700 V 1 kHz 700 V 50 kHz 700 V 45 Hz
    699.355 V 698.785 V 699.355 V
    699.970 V 699.968 V 699.864 V
    700.645 V 701.215 V 700.645 V
    Test Date 13 Mar 2015 Condition As Received
    UNCERT. 0.000043 V 0.000041 V 0.00058 V 0.0084 V
    Status
    Passed
    UNCERT.
    Status
    0.0056 mV 0.021 mV 0.035 mV
    0.00012 V 0.000063 V 0.000065 V 0.00016 V 0.00030 V 0.00063 V
    0.20 mV 0.00019 V 0.0029 V 0.00059 V 0.0016 V
    0.0079 V 0.015 V
    0.073 V 0.45 V 0.12 V
    Page 7 of 9
    Measurement Report Certificate Number 1-6681416900-1
    Model 34401A Options Tested
    Serial MY44007940
    Firmware Rev
    Test Date 13 Mar 2015 Condition As Received
    FREQUENCY
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    UNCERT.
    Status
    Input Freq. (Front) ------- ------- 100 mV Range 10 mV 100 Hz
    99.9000 Hz
    99.9949 Hz
    100.1000 Hz
    0.0048 Hz
    1 V Range 1 V 100 kHz
    99.9900 kHz
    100.0008 kHz
    100.0100 kHz
    0.00065 kHz
    OHMS
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    UNCERT.
    Sts
    4-Wire Ohms Range Input(Front) 100 Ohm 100 Ohm 1 kOhm 1 kOhm 10 kOhm 10 kOhm 100 kOhm 100 kOhm 1 MOhm 1 MOhm 10 MOhm 10 MOhm 100 MOhm 100 MOhm
    99.9860 Ohm 0.999890 kOhm 9.99890 kOhm 99.9890 kOhm 0.999890 MOhm 9.99590 MOhm 99.1900 MOhm
    100.0010 Ohm 1.000001 kOhm 9.99997 kOhm 100.0008 kOhm 1.000024 MOhm 10.00000 MOhm 99.7442 MOhm
    100.0140 Ohm 1.000110 kOhm 10.00110 kOhm 100.0110 kOhm 1.000110 MOhm 10.00410 MOhm 100.8100 MOhm
    0.0028 Ohm 0.000012 kOhm 0.00011 kOhm 0.0014 kOhm 0.000022 MOhm 0.00043 MOhm 0.14 MOhm
    DC CURRENT
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM
    UNCERT.
    Status
    Range Input(Front) 10 mA 10 mA 100 mA 100 mA 1 A 1 A 3 A 2 A
    9.99300 mA 99.9450 mA 0.998900 A 1.99700 A
    10.00010 mA 100.0027 mA 0.999972 A 1.99993 A
    10.00700 mA 100.0550 mA 1.001100 A 2.00300 A
    0.00042 mA 0.0054 mA 0.000097 A 0.00026 A
    AC CURRENT
    Passed
    TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM UNCERT.
    Status
    Input Freq. (Front) -------- -------- 1 Amp Range 10 mA 1 kHz 1 A 1 kHz
    8.590 mA 0.998600 A
    10.143 mA 0.999956 A
    11.410 mA 0.032 mA 0.00033 A 1.001400 A
    Page 8 of 9
    Measurement Report Certificate Number 1-6681416900-1
    Model 34401A Options Tested
    Serial MY44007940
    Firmware Rev
    AC CURRENT (cont.) TEST CONDITIONS
    MINIMUM
    MEASURED
    MAXIMUM UNCERT.
    3 Amp Range 2 A 1 kHz
    1.99520 A
    1.99941 A
    2.00480 A
    0.00065 A
    Test Date 13 Mar 2015 Condition As Received
    Status
    Page 9 of 9
    
**Output Format Example 3**
    --Information of Instrument Calibrated--
    Instrument Calibrated: Digital multimeter, 6.5 digit
    Model Number of Calibrated Instrument: 34401A
    Serial Number of Calibrated Instrument: MY44007940
    Date of Calibration: 13 Mar 2015

    --Information of Calibration Device 1--
    Calibration Device: Function/Arbitrary Waveform Generator, 80 MHz
    Model Number of Calibration Device: 33250A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 31 Oct 2015

    --Information of Calibration Device 2--
    Calibration Device: Calibrator
    Model Number of Calibration Device: 5720A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 19 Apr 2015

    --Information of Calibration Device 3--
    Calibration Device: Amplifier
    Model Number of Calibration Device: 5725A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 19 Apr 2015

**Text Information Example 4**
    (Agenetron
    PARTIAL CALIBRATION CERTIFICATE
    MODEL:
    SERIAL NO:
    DESCRIPTION:
    CUSTOMER:
    DATE OF CAL:
    CAL DUE DATE:
    Teledyne LeCroy Singapore Pte Ltd hereby certifies that the unit describe above met its
    WP96002064
    DIGITAL STORAGE OSCILLOSCOPE
    DSO NATIONAL LABORATORIES
    08 MAR 2018
    08 MAR 2019
    published specification(except Channel 3 failed Calibration Bandwidth, Linearity and
    Noise Tests) at the time of calibration. The accuracy and calibration of this instrument
    are traceable to National Institute of Standards and Technology. Supporting documentation relative to traceability is available for verification upon request.
    CERTIFIED CORRECT sjonetue(Dater Ch 16 fue 16
    WP96002064_perf on 03-08-2018 at_18;14:34.htm Report #9600206403082018181434 page 1 of 5
    TELEDYNE LECROY
    y/ Everywhereyoulook’
    Calibration Certificate
    Certificate Number: 9600206403082018181434 Date Calibrated: 3/8/2018 1:10:12 PM Model Number: WP960 Calibration Site: Singapore
    Serial Number: WP96002064 Calibration Station: CALSOFTSTD Software version: 09.3.0 Temperature (°C): 23
    Procedure used: WOE-VC-TRO0-013 Humidity (% RH): 50
    Test Version: 4.28 Technician: HT
    Limits version 4.2.8 for WP960 Report Date 3/8/2018 18:14:34 Instrument ID #:
    Customer: Calibration Due Date*: —__
    LeCroy-recommended Calibration interval*: 12 months
    Certified Calibration Equipment Used
    Instrument Make Model Serial number_ Cal. date Recal. duedate_ Reference for
    RF Signal Generator Agilent 8648C 4037U03156 Mar. 09,2016 = Mar. 09, 2018 frequency
    ARB Sig. Gen, Agilent 33120A US36034100 Feb. 13,2018 Feb. 13, 2019
    Digital Multimeter Keithley 2000 0724308 Jun. 30,2017 — Jun. 30, 2018 voltage, resistance Power supply Agilent 6633A 3505A05512 Feb. 13,2018 — Feb. 13, 2019
    Scanner Keithley 7001 0620769 Feb. 12,2018 — Feb. 12, 2019
    LeCroy hereby certifies that the instrument listed above has been measured and calibrated against our working standards which are traceable to NIST, and using applicable LeCroy procedures documented in a quality system registered to ISO
    9001:2000. At the time of calibration, the equipment met or exceeded the specifications published in the applicable product documentation. Supporting documentation relative to specific traceability paths is available for review upon request. This certificate shall not be reproduced except in full, without prior written consent from LeCroy.
    Approved By: S€@__
    The recommended calibration interval is based on the LeCroy experience with this product. Your application may require a different calibration interval. The calibration interval should begin on the date the instrument is placed in service. Proper storage prior to being placed in service will not affect the recommended calibration interval.
    WP96002064_perf_on_03-08-2018 at_18;14:34.htm Report #9600206403082018181434 page 2 of 5
    Bandwidth and Flatness
    Input coupling and range\Channel CH! CH2 CH3 CH4 Specification DS50, 100mV -1.75 -2.48 1.11 -2.15 at 2001.0 MHz > -3 dB DIM, 20mV 2.20 0.81 1.39 2.09 at 501.0 MHz >-3dB
    The specifications of frequency-dependent gain relative to a reference frequency of 0.5MHz are denoted A,B,D,E,F,G,H (F and G for typical bandwidth):
    Limit Lower limit on channel gain Upper limit on channel gain Unit
    A -1.2 +12 dB B -2 +2 dB D 3 +25 dB E none +2.5 dB F -3 43.5 dB G none +3.5 dB H none -3 dB
    The following limits are verified, at room temperature:
    Channel Setup Applicable frequencies Sufficient margin, dB -3dB BW, MHz MHz C1 C2 C3 C4Cl C2 C3 C4
    DS502mV_ A:50.B:100 D:200 E:800 of wf -22.6@51 wf 246 244 -14 250 DS505mV_ A:150 B:300 D:540 E:1400 ¥ w 14.7@541 wv 938 993 -407 1045 D50 10mV_A:300 B:500 D:2000 E:2300 Ww w 5.4@1501 2030201062 2028 DS0 99mV wv wv 114@1601 ~ 2016 1962 2030 DS0 100mV vv -3.9@301 ww 2034 2015 -60 2031 DS0 200mV wv v 15.7@1501 “ 2027 2008 2015 DS50 500mV vv 11.5@1601 ¥ 2018 2005 2028 D50 1V wv ¥ 11.0@1601 w 2021 2012 2027 10mV (W) A:300 B:500 D:1500 E:1900 4 -3.0@301 ww 1744 1727 -231 1717 50 mV (W) vv wv 96@1501 wv 1783 1751 1742 DIM 2mV_ A:50B:100F:150G:550 Yv¥w wv 358 321 357 329 DIM 5mV_A:100 B:140 F:300G:900 ¥ ¥ wv wv’ 631 554 584 619 DIM 1J0mV_ A:100B:140 F:500G:600 ¥ wv w w’ 580 560 572 580 DIM 20mV vw wv’ 583 562 577 583 D1M 200mV vv v 542
    The applied signal had a peak-to-peak amplitude of 50% of the full scale, except 25% for 1V/div. The (W) symbol stands for the BWL 1500 effectively applied when the sampling rate is less than 8 GS/s
    If highlighted, a positive Sufficient margin indicates by how much the upper test limit for the response was violated at the point where this violation was maximum, and a negative one indicates by how much the lower test limit for the response was violated.
    WP96002064_perf_on_03-08-2018_at_18;14;34.htm Report #9600206403082018181434
    Linearity Tests
    Input Impedance Measurements
    Input coupling and range\Channel CH] CH2 CH3 CH4 EXT Specification
    D50, 20mV and EXT 50.27 50.34 50.69 50.40 50.39 50.02+£1.5% DS50, 200mV and EXT/5 49.82 49.78 50.25 50.01 50.39 50.02+1.5% AIM, 20mV 1.027 1.026 1.027 1.027 - 1.026MQ +£1.5% DIM, 20 mV and EXT 0.999 0.999 0.999 0.999 0.997 1.000MO+1.5%
    DIM, 200 mV/div and EXT/5 1.000 1.000 1.001 1.000 1.016 1.000MQ+1.5% (EXT/5:1.014MQ)
    Measurements of voltage produced by input
    Input coupling and range\Channel CH1 CH2 CH3 CH4 EXT Specification
    DS0, 20mV and EXT -0.33 -0.15 -0,07 -0.12 0.00 +42 mV DS50, 200mV and EXT/5 -0.33 -0.18 -0.12 -0.10 -0.00
    AIM -0.09 -0.03 -0.01 -0.00 -
    DIM, 20 mV and EXT -0.12 -0.04 0.01 -0.01 -0.41
    DIM, 200 mV/div and EXT/5S 0.15 0.07 0.02 -0.01 -0.10
    Input Accuracy Measurement
    Input coupling and range\Channel CH! CH2 CH3 CH4 Specification
    DS50, 2mV 2.91 1.38 -91.34 1.47 +£5% full scale D50, SmV 1.14 0.41 -90.74 0.67 +3% full scale D50, 10mV 0.65 0.30 -56.69 0.51 +2% full scale DS50, 100mV 0.61 0.20 -56.71 0.47 DS50, 1V 0.43 0.26 -52.17 0.50 DIM, 2mV ~1.00 -1.27 -3.16 1.32 +5% full scale D1M, 5 mV -0.63 -0.75 -3.95 -0.55 £3% full scale DIM, 10 mV -0.39 -0.40 -4.14 -0.37 2% full scale DIM, 102 mV -1.23 0.68 -4.43 0.93 DIM, 200 mV 0.42 -0.34 -4.13 0.43 DIM, 2V 0.41 0.38 -4.03 0.49
    Applying a signal of (up to) 17.5 divisions, and the corresponding offset, the accuracy is verified to: Input coupling and range\Channel CH! CH2 CH3 CH4 Specification
    D50, 50mV -0.32 0.53 -40.24 0.88 £2% full scale
    DIM, 50mV 0.67 0.64 -1.25 0.86 +2% full scale
    page 3 of 5
    WP96002064_perf_on_03-08-2018_at_18;14;34.htm Report #9600206403082018181434 page 4 of 5
    Noise Tests
    Root mean square noise and width of the range of values measured with open inputs
    Input coupling and range\Channel CH1 CH2 CH3 CH4 Specification tm.s. Pk-Pk r.m.s. Pk-Pk r.m.s. Pk-Pk r.m.s. Pk-Pk rms. Pk-Pk
    DIM, 2mV 0.25 2.19 0.25 2.01 0.26 2.06 0.25 2.00 0.32mV 3.2mV
    DS50, 2mV 0.15 137 0.17 138 0.79 11.44 0.16 1.32 0.32mV 3.2mV
    DIM, 10mV 0.44 3.80 042 3.50 042 3.70 043 4.10 0.64mV 6.4mV
    DS50, 10mV 0.30 2.40 0.29 2.50 10,24 43.40 0.30 2.80 0.64mV 6.4mV
    DIM, 102mvV 6.30 58.00 6.00 51.00 6.10 58.00 6.50 61.00 7.6mV 68mV
    Trigger Tests
    Trigger efficiency
    Input frequency and amplitude\Channel CH1 CH2 CH3 CH4 ~—_ EXT (1 div = 300 mV)
    10 MHz, 0.5 div, DC coupling, finite trig. lev. Triggers Triggers Triggers Triggers Triggers
    500 MHz, | div, DC trigger coupling Triggers Triggers Triggers Triggers Triggers
    1 GHz, 2 div, HFDIV trigger coupling Triggers Triggers Triggers Triggers Triggers
    Trigger Hysteresis Measurement
    Hysteresis type\Channel CH1 CH2 CH3 CH4 Specification EXT Specification Triggering on channel 0.29 0.28 0.26 0.29 [0.20,+0.40] DIV 0.088 [0.06,0.12] V Qualifying on channel 0,27 0.30 0.25 0.28 [0.20,+0.40] DIV 0.091 [0.06,0.12] V
    WP96002064_perf_on_03-08-2018_at_18;14;34.htm
    Sinefit Tests
    Table of measured effective bits of the instrument
    Report #960020640308201 8181434
    >5.6 effective bits >5.6 effective bits >5.6 effective bits >5.1 effective bits
    Condition\Channel CH1 CH2 CH3 CH4 Specification Frequency of signal Sampling Frequency
    24 MHz 4 GS/s 6.28 6.18 6.13
    24 MHz 2 GS/s 6.29 621 6.16
    24 MHz, 95%FS 4 GS/s 6.25 6.14 612
    108 MHz 4 GS/s 6.10 6.07 6.00
    Time measurement accuracy
    page 5 of 5
    Ata frequency of 99500000Hz, the timebase is 0.01p.p.m. ; At a frequency of 100500000Hz, the timebase is 0.40p.p.m. . The specified
    tolerance is 10 ppm.
    Calibrator output
    Calibrator high level 0.996V, low level 0.006V
    Overall Test Status:
    WP96002064 Tests failing/missing regarding verification of published specifications.
    a genetron DELIVERY ORDER
    DONO. TERMS P.O. NO. ORDER BY 14-Mar-18 PO61713892 Yeo Teck Hwee John
    DO18-320 BILL TO DELIVER TO: DSO NATIONAL LABORATORIES DSO NATIONAL LABORATORIES 14 Science Park Drive #06-23/28 12 Science Park Drive Singapore 118226 Singapore 118225 ATTN: LIM HONG HIAN (DSO/Finance) Requisition Officer: Tan Tian Hock Richard/ John Yeo Tel.: +65 6308 1068 Hp: 9791 5771.Tel: 6450 4434/ Hp: 9457 7886
    PLEASE RECEIVE THE UNDERMENTIONED GOODS IN GOOD ORDER AND CONDITIONS
    Genetron Singapore Pte Ltd
    | Calibration of 2GHZ DIGITAL OSCILLOSCOPE (VEN: 200924152M)
    (WAVEPRO 960) 178 Paya Lebar Road, #04-06, Singapore 409030 Tel: (65) 67460406 Fax: (65) 67456990
    S/N:2064
    Part No. WAVEPRO 960 OEM/ Brand Name: LeCroy
    with Calibration Certificate & Report
    RECEIVED THE ABOVE MENTIONED GOODS IN GOOD ORDER AND CONDITION
    hae
    COMPANY'S CHOP AND SIGNATURE

**Output Format Exampl 4**
    --Information of Instrument Calibrated--
    Instrument Calibrated: Digital Storage Oscilloscope
    Model Number of Calibrated Instrument: WP960
    Serial Number of Calibrated Instrument: WP96002064
    Date of Calibration: March 8th, 2018
    
    --Information of Calibration Device 1--
    Calibration Device: RF Signal Generator
    Model Number of Calibration Device: 8648C
    Serial Number of Calibration Device: 4037U03156
    Due Date of Calibration Device: March 9th, 2018
    
    --Information of Calibration Device 2--
    Calibration Device: ARB Sig. Gen
    Model Number of Calibration Device: 33120A
    Serial Number of Calibration Device: US36034100
    Due Date of Calibration Device: February 13th, 2019

    --Information of Calibration Device 3--
    Calibration Device: Digital Multimeter
    Model Number of Calibration Device: 2000
    Serial Number of Calibration Device: 0724308
    Due Date of Calibration Device: June 30th, 2018

    --Information of Calibration Device 4--
    Calibration Device: Power Supply
    Model Number of Calibration Device: 6633A
    Serial Number of Calibration Device: 3505A05512
    Due Date of Calibration Device: February 13th, 2019

    --Information of Calibration Device 5--
    Calibration Device: Scanner
    Model Number of Calibration Device: 7001
    Serial Number of Calibration Device: 0620
    Due Date of Calibration Device: February 12th, 2019

**Text Information Example 5**
    e a . Tektronix 2 cumnaere us CERTIFICATE OF TRACEABLE No 1 Cement Loop CALIBRATION 129808 SINGAPORE
    Phone: 6563563900 Fax: 6563564483
    Certificate No: 1899156-1-MSO70404C-C301182-1 Contract/PO No: AGC
    Customer:
    DSO National Laboratories (199701777M) 12 Science Park Drive Singapore Science Park
    118225 SINGAPORE
    Model: MSO70404C
    Serial No.: C301182 Manufacturer: Tektronix, Inc Description: 4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels Site of Calibration: Service Center Calibration Interval Source: Tektronix recommended Cal Date: 05-Nov-2018
    Due Date: 05-Nov-2019 Calibration Interval: 12 Months Temperature(£2°C): 23°C Humidity(£10%RH): 55%
    Tektronix Southeast Asia Pte Ltd certifies that this instrument has been calibrated under the stated environmental conditions using instruments that are traceable to National Institute of Standards and Technology (NIST), National Physical Laboratory or to NMC Singapore. .
    The report shall not be reproduced wholly or in parts without the prior written approval of Tektronix.
    Page 1 of 2
    Tektronix
    Certificate No:
    Contract/PO No: AGC
    INSTRUMENT CONDITION:
    Received:
    Returned:
    Calibration
    CALIBRATION EQUIPMENT USED:
    Model:
    K241C MG3694C 9530 9530 9530
    In tolerance
    Procedure:
    1899156-1-MSO70404C-C301182-1
    CERTIFICATE OF TRACEABLE CALIBRATION
    MANIFEST:Product_Oscilloscopes_DPO70000C-HF~2012_Full VERSION:98
    MANIFEST:Product_Oscilloscopes_DPO70000C-LF-2012_Full VERSION: 103
    Serial No.:
    1301244 152403 43146 43158  43160
    Manufacturer:
    ANRITSU
    ANRITSU
    FLUKE
    FLUKE
    FLUKE
    Rohde and Schwarz Rohde and Schwarz WAVETEK CORP
    o~
    Service Manager: Raul Alenton
    Page
    2 of 2
    Due Date:
    22-Dec-2019 15-May-2020 26-Mar-2019 26-Mar-2019 26-Mar-2019
    Calibrated By: Sea Heng (Sea Heng) Soh Date Issued: 07-Nov-2018

**Output Format Example 5**
    --Information of Instrument Calibrated--
    Instrument Calibrated: 4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels
    Model Number of Calibrated Instrument: MSO70404C
    Serial Number of Calibrated Instrument: C301182
    Date of Calibration: November 5th, 2018
    
    --Information of Calibration Device 1--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: K241C
    Serial Number of Calibration Device: 1301244
    Due Date of Calibration Device: December 22nd, 2019
    
    --Information of Calibration Device 2--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: MG3694C
    Serial Number of Calibration Device: 152403
    Due Date of Calibration Device: May 15th, 2020
    
    --Information of Calibration Device 3--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: 9530
    Serial Number of Calibration Device: 43146
    Due Date of Calibration Device: March 26th, 2019
    
    --Information of Calibration Device 4--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: 9530
    Serial Number of Calibration Device: 43158
    Due Date of Calibration Device: March 26th, 2019
    
    --Information of Calibration Device 5--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: 9530
    Serial Number of Calibration Device: 43160
    Due Date of Calibration Device: March 26th, 2019

**Text Information Example 6**
    02401-06501)
    ale es . == 91 Electronics Ae esuath
    A company of ST Engineering l «| }} 2 4
    Certificate of Calibration no:¢ 55009
    JOB NO 5000001 48241
    CUSTOMER -DSO NATIONAL LABORATORTES
    INSTRUMENT STRUE RMS MULTIMETER
    MANUFACTURER =: FLUKE MODEL = 75
    CUSTOMER REF = -: POG1414164 SERIALNO 294669002
    DATE OF CALIBRATION . 09.12.2014 AMBIENT TEMPERATURE : 25 NEXT CALIBRATION DATE: 09.12.2015 RELATIVE HUMIDITY: 59 %
    Singapore Technologies Electronics Limited hereby certifies that the above instrument calibrated meets the specifications stated in the manufacturer's manual at the time of calibration unless otherwise stated. Records of calibration and traceability are maintained by Singapore Technologies Electronics Limited.
    Calibration of this instrument has been accomplished using standards maintained by the Instrument Calibration Centre of Singapore Technologies Electronics Limited. These standards are traceable to the standards maintained by NMC (SINGAPORE), NIST (USA), NPL (UK}} or other national metrology institutes
    The management systems of our Instrument Calibration Centre are certified to ISO 9001:2008, ISO 14001:2004 and OHSAS 18001:2007. Our laboratory practices are consistent with the ISO/IEC 17025:2005, ISO 10012:2003 and the ANSI/NCSL 2540-1.
    The next calibration date provided in this Certificate serves only as reference and should be determined based on user's requirements
    Remarks
    Calibrated after repair.
    Special calibration, please refer to Test Results.
    YONS KAR MAY QUALITY ASSURANCE
    Singapore Technologies Electronics Limited * 24 Ang Mo Kio Street 65, Singapore 569061 © Tel: (65) 6413 1907 © Fax: (65) 6484 5357 Email: cal@juzclickcal com © www.stee.stengg.com * www.juzclickcal.com » (Regn. No.: 196900084E }} This report shall not be reproduced except in full, without the written approval of the laboratory
    INSTRUMENT CALIBRATION CENTRE
    Job No.: 500000143241
    Model Number » 175 Description : True RMS Multimeter Serial Number : 94660003 Calibration Procedure : Technical Manual Condition : [YZ] InTolerance [[] Outof Tolerance [-] Operational Failure Status : As Found AS FOUND TEST RESULTS Nominal Measured Calibration Tolerances Function Tested Value Value Lower Limit Upper Limit Status
    AC Voltage Test 600mV Range
    600 300.0mV @ 45Hz 300.0 296.7 303.3 PASS 6V Range
    6 5.000V @ 500Hz 4,995 4.947 5.053 PASS 6 5.000V @ 1kHz 4.954 4.897 5.103 PASS 60V Range
    60 50.00V @ 1kHz 50.09 48.97 51.03 PASS 60 50.00V @ 45Hz 49.97 49.47 50.53 PASS 600V Range
    600 300.0V @ 45Hz 300.0 296.7 303.3 PASS 600 100.0V @ 500Hz 100.3 98.7 101.3 PASS 600 100.0V @ 1kHz 100.2 97,7 102.3 PASS 600 600.0V @ 500Hz 601.0 593.7 606.3 PASS 1000V Range
    1000 1000V @ 45Hz 997 987 1013 PASS
    DC Voltage Test 600mV Range
    600 30.0mvV 30.0 29.8 30.2 PASS 600 -300.0mVv -299.9 -300.7 -299.3 PASS 600 600. 0mV 599.7 598.9 601.1 PASS 6V Range
    6 3.000V 3,000 2.993 3.007 PASS 600V Range
    600 300.0V 300.0 299.3 300.7 PASS 1000V Range
    1000 1000V 1000 996 1004 PASS 1000 -1000V -1000 -1004 -996 PASS
    Frequency Test
    99.99Hz Range
    100 45.00Hz @ lv 45.00 44.96 45.04 PASS 9.999kHz Range 10 2.000kHz @ lv 2.000 1.997 2.003 PASS 99.99kHz Range 100 20.00kHz @ 1.5V 20.00 19.97 20.03 PASS
    QA/A1254 REVO JUN2005 Page 1 of 3
    INSTRUMENT CALIBRATION CENTRE Job No.: 500000143241
    AS FOUND TEST RESULTS Nominal Measured Calibration Tolerances
    Function Tested Value Value Lower Limit Upper Limit Status
    100 50.00kHz @ SV 50.00 49.95 50.05 PASS Resistance Test
    6000hm Range
    600 19.00hm 19.0 18.6 19.4 PASS
    50MOhm Range
    50 19.00MOhm 19.01 18.69 19.31 PASS Continuity Test
    6000hm Range
    250hm Input
    Beeper On PASS
    2500hm Input
    Beeper Off PASS Diode Test
    2.4V Range
    2.4 2.000V 2.000 1.978 2.022 PASS Capacitance Test
    1000nF Range
    1000 900nF 901 887 913 PASS AC Current Test
    60mA Range
    60 3.00mA @ 45Hz 3.02 2.93 3.07 PASS
    60 50.00mA @ 1kHz 50.00 49.22 50.78 PASS
    600mA Range
    600 400.0mA @ 1kHz 399.7 393.7 406.3 PASS
    6A Range
    6 4.000A @ 45Hz 4.001 3.937 4.063 PASS
    10A Range
    10 9,00A @ 1kHz 8.99 8.84 9.16 PASS DC Current Test
    6A Range
    6 4.000A 4.000 3.957 4.043 PASS
    10A Range
    10 -9.00A -8.99 ao. 12 -8.88 PASS
    60mA Range
    60 3.00mA 3.03 2.94 3.06 PASS
    60 50.00mA 50.01 49.47 50.53 PASS
    600mA Range
    600 -400.0mA -400.0 -404.3 -395.7 PASS
    QA/A1254 REVO JUN2005 Page 2 of 3
    INSTRUMENT CALIBRATION CENTRE
    Job No.: 500000143241 AS FOUND TEST RESULTS
    End of Test Data
    Calibrated By : Kam Nyit Sai on QC Inspector : | ~
    Date: 99 DEC 2014
    QA/A1254 REVO JUN2005 Page 3 of 3
    INSTRUMENT CALIBRATION CENTRE Job No.: 500000143241
    Model Number : 175 Description : TRUE RMS MULTIMETER Serial Number : 94660003 CALIBRATION EQUIPMENT USED LIST No. Equipment No. Description Serial No. Cal Due Date 1 TE/50/00742 CALIBRATOR 6485011 01/07/2015
    Page 1 of 4

**Output Format Example 6**
    --Information of Instrument Calibrated--
    Instrument Calibrated: TRUE RMS MULTIMETER
    Model Number of Calibrated Instrument: 175
    Serial Number of Calibrated Instrument: 94660003
    Date of Calibration: December 9th, 2014
    
    --Information of Calibration Device 1--
    Calibration Device: CALIBRATOR
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: 6485011
    Due Date of Calibration Device: July 1st, 2015

**Text Information Example 7**
    Jan 13, 2015
    PREMIUM CAL. QUALITY CONTROL CHECK LIST
    Model
    WA-7100
    Serial
    0015374
    Technician
    Description
    Quality Control Aspect
    Item match order (Option & Connector) Selected Service International Voltage Test/Label Calibration sticker ( front panel, left upper corner ) Cal Date & Cal Due identical (Certificate vs Sticker) Serial # is accurate ( certificate vs report vs sticker vs unit ) Tamper proof seals Cleanliness of equipment Dust cap Key taped above ( if applicable ) All feet present (or spacer for venting holes)
    Esthetical
    Report # matching on certificate & on page 2 Customer name & address Manufacturer, model, serial & description Procedure # Report Cal Date & Due Date T*, RH % Quality Control Manager
    Technical
    Page header with model & serial Equipment listing with Valid Due Date Action taken ( if conformance with spec = N and repair or adjustment = Y, a remarks note is needed)
    Data check against specs All status PASSED (*) linked to related comment Pagination ( page # of ## ; if applicable ) Technician name & signature Quality Control Manager on last page Report saved in pdf format (Renamed *_QC.pdf by ->) Certificate & page 2 printed on special paper
    Technician signature
    Technical quality manager signature
    Esthetical quality manager signature
    Calibration report no. 1362471501130936
    616 Rue Auguste-Mondoux Gatineau (Quebec) J9J 3K3 Canada
    Tel. (819)-770-7771 Fax (819)-770-7772
    Certificate of Premium Calibration
    Asset Information Customer Address Manufacturer Model Serial Number Description Options Procedure Number Calibration Date Calibration Due
    Burleigh WA-7100
    Multi Wavelength Meter N/A 11CPO1842D
    Environmental Conditions 22.1 °C 38 %RH
    Temperature Relative Humidity
    This document certifies that the above product was calibrated in compliance with Simbol Test Systems Inc. quality systems and in accordance with applicable procedures. These procedures are designed to assure the product listed above meets or exceeds the general manufacturer published specifications.
    Simbol Test Systems Inc. certifies that the measurement standards and instruments used during calibration are traceable to the National Institute of Standard and Technology, the National Research Council of Canada or equipments that are NIST or NRC traceable. Some measurements are traceable to natural physical constants consensus standards or ratio type measurements.
    Patrick Leduc Quality Control Manager
    Calibration report no. 1362471501130936
    616 Rue Auguste-Mondoux Gatineau (Quebec) J9J 3K3 Canada
    Tel. (819)-770-7771 Fax (819)-770-7772
    Traceable standards and equipment used in calibration
    Item Description Lightwave Measurement System Tunable Laser Source Optical Head Interface Module InGaAs Optical Head InGaAs Optical Head 
    Serial Number DE40706941 DE39400720 DE38701065 DE41100359 DE38200270 
    Manufacturer/Model
    Agilent 8164A Agilent 81640A Agilent 81619A Agilent 81624B Agilent 81625A
    Cal. Date 6-Jan-15 24-Feb-14 Not reqrd. 22-Mar-13 29-Oct-14 
    Cal. due 6-Jan-16 24-Feb-16 Not reqrd. 22-Mar-15 29-Oct-16

**Output Format Exammple 7**
    --Information of Instrument Calibrated--
    Instrument Calibrated: Multi Wavelength Meter
    Model Number of Calibrated Instrument: WA-7100
    Serial Number of Calibrated Instrument: 0015374
    Date of Calibration: Not Mentioned
    
    --Information of Calibration Device 1--
    Calibration Device: Lightwave Measurement System
    Model Number of Calibration Device: 8164A
    Serial Number of Calibration Device: DE40706941
    Due Date of Calibration Device: January 6th, 2016
    
    --Information of Calibration Device 2--
    Calibration Device: Tunable Laser Source
    Model Number of Calibration Device: 81640A
    Serial Number of Calibration Device: DE39400720
    Due Date of Calibration Device: February 24th, 2016
    
    --Information of Calibration Device 3--
    Calibration Device: Optical Head Interface Module
    Model Number of Calibration Device: 81619A
    Serial Number of Calibration Device: DE38701065
    Due Date of Calibration Device: Not Required
    
    --Information of Calibration Device 4--
    Calibration Device: InGaAs Optical Head
    Model Number of Calibration Device: 81624B
    Serial Number of Calibration Device: DE41100359
    Due Date of Calibration Device: March 22nd, 2015
    
    --Information of Calibration Device 5--
    Calibration Device: InGaAs Optical Head
    Model Number of Calibration Device: 81625A
    Serial Number of Calibration Device: DE38200270
    Due Date of Calibration Device: October 29th, 2016

**Text Information Example 8**
    ROHDE&SCHWARZ
    Calibration Certificate Certificate Number 0001-300495030 Kalibrierschein Zertifikatsnummer
    Unit Data This callbration certificate documents, item 2V-Z129 CALIBRATION KIT Meesured soca aie Gegenstand 2.92MM(F) specifications.
    Measurement results are located usually In the corresponding Interval
    with a probability of approx. 95% Manufacturer © ROHDE & SCHWARZ (coverage factorka 2 Hersteller Calibration Is performed with test equipment and standards directly or Type ZV-Z129 Indirectly traceable by means of Typ approved callbration techniques to the PTB/DKD or other natlonal / Materlal Number 1322.7471KO3 SerialNumber 101243 iomatond eran which a e physical un! measureme! Materialnummer Seriennummer according to the International System Asset Number of Units (Sl). Inventarnummer In all cases where no standards are
    available, measurements are referenced to standards of the R&S.
    Order Data laboratories. | Aas Fiedler . . Principles and methods of callbration Customer DSO National Laboratories correspond and are conformant with Auftraggeber i i EN ISO/EG 17025, ANSINCSL 99 Science Park Drive 20 2540.1-1994 and ANSI/NCSL 118230 Singapore Z540.3-2006. The applied quality SG system Is certifled to EN ISO 9001.
    This callbratlon certificate may not be reproduced other than in full. Callbration certificates without signatures are not valid.
    The user Is obliged to have the object Tecallbrated at appropriate Intervals.
    Dieser Kalibrierschein dokumentiert, dass
    OrderNumber 4971512066 der genannte Gegenstand nach Bestellnummer festgelegten Vorgaben geprift und gemessen wurde. Die Messwerte lagen Im Date of Receipt 2019-01-23 Regelfall mit elner Wahrschelnilchkelt von Eingangsdatum annahernd 95% im zugeordneten gang Wertelntervall (Erweiterte Messunsicherheit mt k = 2). Performance Die parung ee wy Searle : und Normalen, dle direkt oder Indirekt Place and Date of Callbration Werk Memmingen, 2019-01-31 durch Ableltung mittels anerkannter Ort und Datum der Kalibrierung Kalibriertechniken riickgefiuhrt sind auf . Normale der PTB/DKD oder anderer Scope of Callbration Standard Calibration natlonaler/internationaler Standards zur Umfang der Kalibrierung Darstellung der physikalischen Einhelten in enenmiund mit dem (sh i Internationalen Einheitensystem
    (SI). Statement of Compliance All measured values are within Wenn kelne Normale existieren, erfolgt (Incoming) the data sheet specifications. die Rickfihrung auf Bezugsnormale der Konformitatsaussage R&S-Laboratorien. (Anileferung) Grundsatze und Verfahren der
    Kalibrlerung beziehen sich auf und entsprechen EN ISO/IEC 17025,
    Statement of Compliance All measured values are within ANSINCSL 2540.1-1994 und ANSUNCSL (Outgoing) . 2540.3-2006. ( 9 the data sheet specifications. Das angewandte Konformitatsaussage Qualitétsmanagement-System ist (Auslieferung) zertifiziert nach EN ISO 9001. Dieser Kalibrierscheln darf nur vollstandig Extent of Calibration Documents 2 Pages Calibration Certificate Polinocetaine caescutitcemmen. Umfang des Kallbrierdokuments "1 Pages Outgoing Results sind ungiiltlg. ; Fir dle Einhaltung einer angemessenen 11 Pages Incoming Results Frist zur Wiederholung der Kalibrierung ist der Benutzer verantwortlich.
    Rohde & Schwarz Messgeratebau GmbH
    Date of Issue Head of Laboratory Person Responsible Ausstellungsdatum | éborleitung Bearbeiter [ile Vie 2019-01-31 Miladin Misic Page 1/2
    ver9815/MB0707,
    Rohde & Schwarz Messgeratebau GmbH - Postfach 16520-87686 Memmingen - Rohde-und-Schwarz-Str. 1 D-87700 Memmingen Telefon national: 08331/10-80; international: 0049 8331/10-80; Fax: 08331/10-811 24 Geschaftsfihrer: Jiirgen Steigmiiller - Aufsichtsratsvorsitzender: Dr. Marc Sesterhenn Sitz der Gesellschaft: Miinchen - Registereintrag: Amisgericht Miinchen HRB 1059
    Materlal Number 1322.7471K03 Serial Number 101243 Certificate Number 0001-300495030
    Callbratlon Method 1317.7683.01-PB-08.00 Relative Humidity = 20%-60% Kalibrieranweisung Relative Luftfeuchte Amblent Temperature (23 . y°c
    Umgebungstemperatur
    Working standards used (having a significant effect on the accuracy) Verwendete Gebrauchsnormale (mit signifikantem Einfluss auf die Genauigkeit)
    tem Type Serlal Number Callbration Certificate Number Cal. Due Gegenstand Typ Seriennummer Kallbrierscheinnummer Kallbr. bis Digital Multimeter UDSS 879700/058 481596 D-K-15195-01-01 2018-09 2021-09-30 Vector Network Analyzer 4-Port ZVA40 100380 475295 D-K-15195-01-01 2018-08 2019-08-31 Callbration Kit 2,92mm (f}} ZV-Z129 101108 474429-D-K-15195-01-01 2018-07 2019-07-31 Callbratlon Kit 2,92mm ZV-Z129 101108 474430-D-K-15195-01-01 2018-07 2019-07-31
    UGB1 A compliance statement may be possible where a confidence level of less than 95 % Is acceptable. Die Bestatigung der Konformitat ist méglich, sofern ein Grad des Vertrauens von wenlger als 95 % akzeptabel ist.
    UGB2 A non-compliance statement may be possible where a confidence level of less than 95 % is acceptable. Die Bestatigung der Nicht-Konformitat ist méglich, sofern ein Grad des Vertrauens von weniger als 95 % akzeptabel ist.
    Ref.; ILAC-G8;03/2009 ‘Guidelines on the Reporting of Compliance with Specification’
    Notes Anmerkungen
    Recommended calibration interval: 12 Months
    Installed options are included in calibration. Depending on installed options, numbers of pages of the record are not consecutive.
    Page 2/2
    ROHDE&SCHWARZ
    Rohde & Schwarz Regional Headquarters Singapore Pte Ltd , 4 Loyang Way 2, Singapore 507100 DSO National Laboratories
    20 Science Park Drive
    Singapore Science Park
    Rohde & Schwarz
    Regional Headquarters Singapore Pte Ltd 4 Loyang Way 2
    Singapore 507100
    Singapore 118230 Service reference Your order / Date Contact Singapore, 08-Feb-19 308024588 service.sg@rohde-schwarz.com
    Service Report _ Service reference no. (RMA) 308024588
    Type Material no. Serial no. ZV-Z129 CALIBRATION KIT 2.92MM(F) 1322.7471K03 101243
    Work performed:
    r Check if Replacement
    r Repair ‘e Relevant modifications checked and Vi R&S-Manufacturer-Calibration performed
    rm R&S-Accredited-Calibration Vv: elsaning
    rm Multi-Vendor Performance Calibration = Electrical Safety Test
    mo Multi-Vendor Accredited Calibration Virus and Malware Check:
    ir Res Peronnanes "Calibration rm Performed, no Virus-/Malware found ~ Adjustment re Performed, Virus-/Malware found! See rm Special Calibration Ea details below
    [Performance Check Vv Not applicable
    me Upgrade (HW/SW)
    ™ Firmware update
    Report:
    Unit sent to Germany for calibration.
    All measured values within specifications.

**Output Format Example 8**
    **Information of Instrument Calibrated**
    Instrument Calibrated: 2.92MM(F) CALIBRATION KIT
    Model Number of Calibrated Instrument: ZV-Z129
    Serial Number of Calibrated Instrument: 101243
    Date of Calibration: January 31st, 2019
    
    **Information of Calibration Device 1**
    Calibration Device: Digital Multimeter
    Model Number of Calibration Device: UDSS
    Serial Number of Calibration Device: 879700/058
    Due Date of Calibration Device: September 30th, 2021
    
    **Information of Calibration Device 2**
    Calibration Device: Vector Network Analyzer 4-Port
    Model Number of Calibration Device: ZVA40
    Serial Number of Calibration Device: 100380
    Due Date of Calibration Device: August 31st, 2019
    
    **Information of Calibration Device 3**
    Calibration Device: Calibration Kit 2.92mm (f)
    Model Number of Calibration Device: ZV-Z129
    Serial Number of Calibration Device: 101108
    Due Date of Calibration Device: July 31st, 2019
    
    **Information of Calibration Device 4**
    Calibration Device: Calibration Kit 2.92mm
    Model Number of Calibration Device: ZV-Z129
    Serial Number of Calibration Device: 101108 
    Due Date of Calibration Device: July 31st, 2019

    
**Text Information Example 9**
    Title: QUANTUM TECHNOLOGIES GLOBAL PTE LTO
    Title: | U MI Company Reg.:2009241 49W
    UncategorizedText: Q U A N 237 PANDAN LOOP #08-11 TECHNOLOGIES GLOBAL WESTECH BUILDING SINGAPORE 128424
    UncategorizedText: Tel: +65 6778 3655 Fax: +65 6777 7169 www. quantumsg.com
    Title: Certificate of Calibration
    UncategorizedText: Customer : JOHNSON & JOHNSON ASIA PACIFIC Address : 51 SCIENCE PARK ROAD #01-01/05 THE ARIES CR17-048
    Title: SCIENCE PARK 2 Singapore 117586 : Calibration Location : Chamber Lab
    Title: Description : Environmental Chamber
    Title: Serial No. 199297
    Title: Manufacturer : Contherm
    Title: Model / Type : CTM.1900CSL
    UncategorizedText: Report Type : As Found Ambient Temperature 124.4+2°C Date of Calibration : 05-May-2017 Ambient Relative Humidity : 65 + 15 % rh
    Title: Method of Calibration
    NarrativeText: Quantum Technology Global Pte Ltd (QTG) certifies that calibration of the above testing machine has been verified in comparison of chamber working space temperature and humidity using calibrated reference sensor with reference to Calibration Method QTG-02-WP-004-03 Rev01.
    NarrativeText: The Calibration of Environmental Chamber was executed by comparing the air temperature of the chamber with the reference sensor in the empty working space for which the difference between air temperature and the indicated values is stated.
    NarrativeText: The calibration was performed in terms of the International Temperature Scale of 1990 (ITS-90)
    Title: Results of Calibration
    NarrativeText: The tabulated results of calibration are given on the following page(s) of this report.
    NarrativeText: The expanded uncertainties of measurement are 1.5°C and 3.9% relative humidity for the above mentioned Environmental Chamber's temperature and relative humidity respectively, estimated at a level of confidence of
    Title: approximately 95% with a coverage factor k=2.
    NarrativeText: The user should determine the suitability of the above mentioned chamber and its intended use.
    Title: Calibration Officer Approved By Dickson Ng Chong Tai Wei
    NarrativeText: The report shall not be reproduced wholly or in parts without the written approval of the issuing authority. No reference shall be made by the Client to Quantum Technologies Global Pte Ltd or to the report or results furnished by Quantum Technologies Global Pte Ltd in any advertisements or sales promotions.
    Title: Your Partner in Quality Testing Page 1 of 4
    Title: Certificate Number: CR17-048 HE vt Description
    NarrativeText: The reference sensor measuring location is distributed in the useful volume of the Environmental Chamber. The measurements was carried out after a steady state period with 30 minutes of measurement data recorded at an interval of 1 minutes.
    Title: UUT Description: Environmental Chamber
    Title: Manufacturer: Contherm
    Title: Model / Type: CTM.1900CSL
    Title: Serial Number: 99297
    NarrativeText: Distribution: Figure A shows the distribution of sensors placed in the UUT working
    NarrativeText: space with sensor P9 placed at the center of the chamber as reference & P10 placed near the control sensor
    Title: Figure A
    Title: M24 REFERENCE EQUIPMENT
    NarrativeText: The measurement was made in support of this certificate with reference standards which are traceable to the International System of Units (SI) through National Metrology Institutes and/or other accredited laboratory.
    NarrativeText: No Reference Equipment Model No Serial No Calibration Due i. Fluke Hydra III 2638A 32590011 27-Mar-2018 with PT100 Sensor Class A RTD VP74589 to VP72598 ii, Rotronics Hygrolog HL-NT2-D 61538118 08-Jun-2017 with Humidity Sensor HC2-S 20084767 BEMITERMs & DEFINITIONS
    UncategorizedText: |. Temperature Constancy in Time - Temperature Fluctuation, difference after stabilization between the maximum and minimum temperatures at any point in the working space during a specified interval of time.
    UncategorizedText: ll. Temperature Homogeneity in Space - Temperature Gradient, maximum difference after stabilization at any moment in time between two separate points in the working space.
    NarrativeText: lll. Humidity Constancy in Time - Relative Humidity Fluctuation, fluctuation calculated with the temperature sensor which has the largest fluctuation.
    NarrativeText: lV. Humidity Homogeneity in Space - Relative Humidity Gradient, gradient whose predominant contribution is caused by the temperature gradient in the working space.
    NarrativeText: V. Overall Mean Temperature/Humidity - Mean measured value in the chamber of 9 distributed location during the duration of measurement.
    Title: BZW Notes
    NarrativeText: Relative humidity of various test point were calculated based on humidity measurement with known input values of temperature and calculated dew point.
    ListItem: Correction of reference sensor has been applied
    ListItem: All measurement results are rounded up to the last decimal
    ListItem: Unit for %RH means % relative humidity, °C means degree celcius and d, means dew point in °C
    ListItem: The above terms & definitions are extracted from IEC60068-3-5:2001 & IEC60068-3-6:2001
    ListItem: The measurement uncertainties calculated was in accordance to IEC60068-3-11:2007
    ListItem: User should determine the suitability of the above mentioned chamber for its intended use.
    NarrativeText: The report shail not be reproduced wholly or in parts without the written approval of the issuing authority. No reference shall be made by the Client to Quantum Technologies Global Pte Ltd or to the report or results furnished by Quantum Technologies Global Pte Ltd in any advertisements or sales promotions.
    Title: Your Partner in Quality Testing Page 2 of 4
    Title: Certificate Number: 17-04
    Title: MG OVERALL RESULT OF ACHIEVED TEMPERATURE & RELATIVE HUMIDITY
    UncategorizedText: Results of Environmental Chamber Temperature / Humidity Set Point with Overall Mean Temperature / Humidity
    Title: Chamber Set Point Measured Overall Mean Correction (uur) (Ter) (Tre - Tuur)
    UncategorizedText: 30°C 29.9°C -0.1°C 30%RH 31.2%RH 1.2%RH
    UncategorizedText: 23°C 23.2°C 0.2°C 30%RH 26.3%RH -3.7%RH
    UncategorizedText: 23°C 23.4°C 0.4°C 50% RH 47.3%RH -2.7%RH
    UncategorizedText: 23°C 23.6°C 0.6°C 90%RH 89.7%RH -0.3%RH
    UncategorizedText: 30°C 30.4°C 0.4°C 90%RH 89.7%RH -0.3%RH
    UncategorizedText: 60°C 60.1°C 0.1°C 95%RH 95.9%RH 0.9%RH
    UncategorizedText: Results of Environmental Chamber Temperature / Humidity Performance within the usable working space
    UncategorizedText: Chamber Performance 30°C @ 23°C @ 23°C @ 23°C @ 30°C @ 60°C @ 30%RH 30%RH 50%RH 90%RH 90%RH 95%RH Temperature Constancy in Time 7 °, 7 ej Py ry i a3 were wading) save “tl ’ ° Temperature Homogeneity in Space 0.58°C 0.46°C 0.28°C 0.07°C 0.11°C 0.18°C relative to the nominal value . . . . : RH
    Title: Humidity Constancy over Time a e a
    NarrativeText: lat the center of usable space 0.3%RH 0.1%RH 0.1%RH 0.5%RH 0.6%RH 0.8%RH Paumicity Romogepet yl PISPece ms 1.0%RH 0.7%RH 0.8% 0.4%RH 0.6%RH 0.8%RH relative to temperature homogeneity
    NarrativeText: The report shail not be reproduced wholly or in parts without the written approval of the issuing authority. No reference shail be made by the Client to Quantum Technologies Global Pte Ltd or to the report or results furnished by Quantum Technologies Global Pte Ltd in any advertisements or sales promotions.
    Title: Your Partner in Quality Testing Page 3 of 4
    Title: Certificate Number: CR17-048 GEA TABULATION OF MEASURING LOCATION IN THE CHAMBER
    NarrativeText: Measured results of 10 individual measurement position distributed in the Environmental Chamber
    NarrativeText: ee eee amend y Pi | p2 [ps | pa | ps | pe | pr | pe | po | Pio |
    UncategorizedText: Mean Temperature(°C) Maximum Temperature(°C) Minimum Temperature(°C)}} Mean Dewpoint (°C) Mean Humidity(%rh) Maximum Humidity(%rh) Minimum Humidity(%rh) Mean Temperature(°C) Maximum Temperature(°C) Minimum Temperature(°C) @ Mean Dewpoint (°C) 30%RH | Mean Humidity(%rh) Maximum Humidity(%erh) Minimum Humidity(%rh) Mean Temperature(?C) Maximum Temperature(°C) Minimum Temperature(°C) @ Mean Dewpoint (°C) 50%RH_ = |Mean Humidity(%rh) Maximum Humidity(%rh) Minimum Humidity(%rh) Mean Temperature(°C) Maximum Temperature(°C) Minimum Temperature(°C) @ Mean Dewpoint (°C) 90%RH [Mean Humidity(%rh) Maximum Humidity(%rh) Minimum Humidity(%rh) Mean Temperature(?C) Maximum Temperature(°C) Minimum Temperature(°C) Mean Dewpoint (°C) Mean Humidity(%rh) Maximum Humidity(%rh) Minimum
    Humidity(%rh)
    NarrativeText: Mean Temperature(°C) Maximum Temperature(°C) Minimum Temperature(°C) @ Mean Dewpoint (°C) 95%RH =| Mean Humidity(%rh). Maximum Humidity(%rh) Minimum Humidity(%rh)
    NarrativeText: The report shail not be reproduced wholly or in parts without the written approval of the issuing authority. No reference shall be made by the Client to Quantum Technologies Global Pte Ltd or to the report or results furnished by Quantum Technologies Global Pte Ltd in any advertisements or sales promotions.
    Title: Your Partner in Quality Testing Page 4 of 4

**Output Format Example 9**
    **Information of Instrument Calibrated**
    - Instrument Calibrated: Environmental Chamber
    - Model Number of Calibrated Instrument: CTM.1900CSL
    - Serial Number of Calibrated Instrument: 99297
    - Date of Calibration: May 5th, 2017
    
    **Information of Calibration Device 1**
    - Calibration Device: Fluke Hydra III with PT100 Sensor
    - Model Number of Calibration Device: 2638A and Class A RTD
    - Serial Number of Calibration Device: 32590011 and VP74589 to VP72598
    - Due Date of Calibration Device: March 27th, 2018
    
    **Information of Calibration Device 2**
    - Calibration Device: Rotronics Hygrolog HL-NT2-D with Humidity Sensor
    - Model Number of Calibration Device: HL-NT2-D and HC2-S
    - Serial Number of Calibration Device: 61538118 and 20084767
    - Due Date of Calibration Device: June 8th, 2017

**Text Information Example 10**
    Title: ZAGA SERVICES PRIVATE LIMITED 613B Punggol Dr #03-847 Singapore 822613 RRO.
    UncategorizedText: T: (65) 6996 2878 = SZ W: www.zaga.com.sg jlac-MRA ACCREDITED E: zagaspl@gmail.com % ow A Re ny ye
    NarrativeText: ZAGA, -, seon no rrsoeuse CALIBRATION CERTIFICATE
    NarrativeText: Date: 02-11-2017 Cert No.: ZG-17072 Page No.: Page 1 of 2
    Title: CALIBRATION OF ELECTRONIC BALANCE
    Title: Issued To: DSO LABORATORIES Address: 12 Science Park Drive Singapore 118225
    Title: PARTICULARS OF UNIT UNDER TEST
    NarrativeText: Equipment: Electronic Balance Manufacturer: Precisa Model : LS 220A Serial No.: 7001726 WDNo.: - Scale Range(s): 0 to 220g Resolution: 0.0001g Date of Calibration: 01-11-2017 Recommended Due Date: 31-10-2018 Place of Calibration: SP12 #1-122-1 Ambient Conditions: 22°C 41°C 72%r.h +5%r.h
    Title: eS nm eee
    NarrativeText: Method of Measurement The described Electronic Balance was calibrated under the environmental condition stated above.
    NarrativeText: The Laboratory Management system maintained at ZAGA Services PTE LTD are in compliance with ISO/IEC 17025: 2005
    NarrativeText: The calibration was carried out using the following standards traceable to the SI units of measurements.
    NarrativeText: Standards: Serial/ /D No.: Traceability: Standard Weight Set 08343C NMIM(MY)
    NarrativeText: The equipment has been calibrated using weights of known mass. The method of measurement is generally as stated in procedure ZGTP-04 Ver. 3 (2013). The following parameters were verified during the calibration.
    NarrativeText: Repeatability Measured by making 10 repeated readings and calculating the resulting standard deviation.
    NarrativeText: Linearity Is the closeness of the indicated balance reading compared to the applied mass.
    Title: Pan Position Error
    NarrativeText: Max. difference from the centre in indicated weight when a sample weight is shifted to various positions on the weighing area of the sample pan.
    Title: Hysteresis
    NarrativeText: Difference in weight values indicated at a given test load depending on whether the test load was arrived at by increase or a decrease from the previous ioad on the scale.
    NarrativeText: The results reported herein have been performed In accordance with the terms of accreditation under the Singapore Accreditation Council.
    NarrativeText: The reports shall not be reproduced except in full & used in any pubicity materials unless the management representatives of ZAGA Services has given approval in writing.
    UncategorizedText: ZAGA SERVICES PRIVATE LIMITED 613B Punggol Dr #03-847 Singapore 822613 Tr (65) 6996 2878
    Title: W: www.zaga.com.sg E: ‘zagaspl@gmail. com
    Title: AGA Co, Regn. No. 201008343C
    UncategorizedText: Date: 02-11-2017
    Title: Results of Measurement:
    Title: REPEATABILITY
    Title: Nominal Load (g) Standard Deviation (g)
    Title: SW
    UncategorizedText: .
    Title: SS
    ListItem: 
    Title: ip ctipeiad LABORATORY
    Title: “USNS SAC-SINGLAS
    Title: CAINS
    Title: CALIBRATION CERTIFICATE
    Title: Cert No.: Page No.:
    Title: ZG-17072 Page 2 of 2
    Title: Max. Difference (g)
    UncategorizedText: 10 0.0000
    UncategorizedText: 0.0001
    UncategorizedText: 100 0.0000
    UncategorizedText: 0.0002
    UncategorizedText: 200 0.0000
    UncategorizedText: 0.0002
    Title: LINEARITY
    NarrativeText: The following table gives the measured correction (Applied mass value - balance reading), the associated expanded
    Title: uncertainty (for an approximately 95% confidence level).
    Title: Balance Readings
    Title: Applied Mass (g) (9)
    Title: Correction (g) Coverage Factor, k
    Title: Expanded Uncertainty, (g)
    UncategorizedText: 20.0000 19.9998 0.0002
    UncategorizedText: 0.0001
    UncategorizedText: 39.9999 39.9999 0.0000
    UncategorizedText: 0.0002
    UncategorizedText: 60.0003 60,0001 0.0002
    UncategorizedText: 0.0002
    UncategorizedText: 80.0003 80.0001 0.0002
    UncategorizedText: 0.0003
    UncategorizedText: 100.0003 100.0001 0.0002
    UncategorizedText: 0.0002
    UncategorizedText: 120.0003 120.0001 0.0002
    UncategorizedText: 0.0003
    UncategorizedText: 140.0002 140.0002 0.0000
    UncategorizedText: 0.0003
    UncategorizedText: 160.0007 160.0005 0.0002
    UncategorizedText: 0.0003
    UncategorizedText: 180.0006 180.0004 0,0002
    UncategorizedText: 200.0006 200.0004 0.0002
    Title: PAN POSITION ERROR
    Title: Nominal
    Title: Load (9) Centre Rear Left Front
    Title: NI NI NININ|N|NM Y/N] hy
    Title: Right
    UncategorizedText: 0.0004 0.0003
    Title: Centre
    UncategorizedText: 50 49.9999 50.0001 49.9999 49,9998
    Title: Average reading at centre: 50.0000g Pan Position error: 0.0002g
    Title: Measured Hysteresis: Less than 0.00019 General Comments
    ListItem: The user should determine the suitability of the balance for its intended use. * Keep Balance away from draft.
    UncategorizedText: 50.0002
    UncategorizedText: 50.0001

**Output Format Example 10:**
    **Information of Instrument Calibrated**
    - Instrument Calibrated: Electronic Balance
    - Model: LS 220A
    - Serial Number: 7001726
    - Date of Calibration: November 1st, 2017
    
    **Information of Calibration Device 1**
    - Calibration Device: Standard Weight Set
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 08343C
    - Due Date of Calibration Device: Not Mentioned

**Text Information Example 11:**
    TECHNOLOGIES
    : Certificate of Calibration es) KEYSIGHT Keysight Calibration
    i> 3\ i
    Certificate Number 1-8550569912-1
    Model Number 8752C
    Manufacturer Hewlett Packard Co Deseription RF Vector network analyzer Serial Number 3410A02579
    Options Installed 003 004
    Date of Calibration 4 Feb 2017
    Customer
    DSO National Laboratories
    12 Science Park Dr, The Mendel SINGAPORE 118225 Singapore
    Location of Calibration
    Procedure STE-50113374-A,05.02-T214DMW. Keysight Technologies Singapore (Sales) Pte. Ltd. Temperature (23 + 5) °C 1 Yishun Avenue 7 Humidity (50 + 20) %RH Registration No:201400782D
    Singapore 768923 Singapore
    This certifies that the equipment has been calibrated using applicable Keysight Technologies procedures in compliance with a quality management system registered to ISO 9001:2015.
    This calibration report is composed of a certificate of calibration and measurement report.
    As Received Conditions One or more measured values of the equipment were observed out of specification at the points tested.
    Action Taken - The equipment is outside of its support life. As a result, no actions were possible.
    As Completed Conditions One or more measured values of the equipment were observed out of specification at the points tested.
    A team of engineers and metrologists develops performance tests procedures and selects specific instruments considering the uncertainty of measurement. In this report, conformance statements of “Passed” or “Failed” are determined by simple comparison of observed measurements to the warranted specifications.
    Remarks or Special Requirements Unit failed system verification test. Conditional cal done. — eens
    This calibration certificate may refer to instruments manufactured by HP, Agilent and Keysight as being manufactured by Keysight Technologies, Inc.
    The test limits stated in the report correspond to the published specifications of the equipment, at the points tested.
    Based on the customer's request, the next calibration is due on 4 Feb 2019,
    Liu Biao Keysight Technologies Singapore (Sales)
    Pte. Ltd.
    1 Yishun Avenue 7
    Registration No:201400782D Co — Singapore 768923 ——
    Singapore Goh Jenn Hann. Service Centre Manager
    Issue Date 8 Feb 2017 Page | of 2
    This report shall not be reproduced except in full, without the written approval of the laboratory
    Certificate of Calibration
    KEYSIGHT Keysight Calibration Ee Certificate Number 1-8550569912-1
    Traceability Information Technician ID Number N5241850
    Measurements are traceable to the International System of Units (SI) via national metrology institutes (www.keysight.com/find/NMI) that are signatories to the CIPM Mutual Recognition Arrangement.
    This certificate shall not be reproduced, except in full, without prior written approval of the laboratory.
    Calibration Equipment Used
    Model Number Model Description Equipment ID Cal Due Date Certificate Number
    11667A DC-18 GHz power splitter, type N, 50 ohm 11667A15987 5 Feb 2018 1-7614034320-1
    SO71A Primary frequency standard 5071A01633 27 Jan 2018 1-7593541280-1
    53132A Universal Counter, 225 MHz, 12 digit/s, 150 ps. 53132A07171 7 Dec 2017 1-7480325004-1 GPIB, RS232
    8482A Power Sensor, 100 kHz to 4.2 GHz, -30 to +20 dBm 8482A14928 1 Jun 2017 1-6836670898-1
    8496H 0-110dB programmable step ATTENUATOR, 8496H00390 8 Jun 2018 1-7824369341-1 0-18GHz
    85032B 50-Ohm Type-N calibration kit 85032B00563 22 Jul 2017 1-7588002560-1
    E4419B Power meter - EPM series, dual channel E4419B12962 27 May 2018 1-7869427425-1
    _ S's LU U EEE EET
    Page 2 of 2
    KEYSIGHT Measurement Report -
    TECHNOLOGIES Certificate Number 1-8550569912-1 Model Number 8752C Location of Calibration Serial Number 3410A02579 KEYSIGHT TECHNOLOGIES SINGAPORE Options Tested 003 004 (SALES) PTE, LTD,
    Registration Number : 201400782D
    Test Date 4 Feb 2017 NO. 1 Yishun Ave 7 Temperature. (2345) °C Singapore 768923 Huinidity (30 to 70) %RH : Test Program Namie . HP8752A_C, 5011-3374 Test Program Version A,05.02 Test Executive STE/9000, C.08.94W Test Subsystem MENDOR, B.06.34
    i 7 Note: Traceability information can be found on the calibration certificate.
    me
    Page | of 9
    This report shall not be reproduced except in full, without the written approval of the laboratory
    KEYSIGHT Measurement Report
    TECHNOLOGIES Certificate Number 1-8550569912-1
    Compliance with Specification
    Measured values of the equipment that were observed in specification at the points tested are determined to have Passed ( ). Measured values of the equipment that were observed out of specification at the points tested are determined to have Failed (F).
    An overall statement of compliance for all tests performed as received, and as completed (if any adjustments / repairs were performed) is included at the beginning of this report. Statements of compliance apply only to warranted specifications, When functional verification tests are performed, results are reported in the “Functional Test” section, and do not affect these statements of compliance.
    The status summaries relate to the tested item only. A final decision about whether the item's performance actually satisfies requirements of the user can only be made by the user.
    Measurement results are reported as:
    Passed () - The measured values of the equipment were observed in specification at the points tested. « Failed (F) - One or more measured values of the equipment were observed out of specification at the points tested.
    Upper Specification mmm meee ces ns a ee ee
    ® Nominal
    Lower Specification ——— §— ee ee
    Measurement Result Passed ( ) Failed (F)
    () This result is indicated on the measurement report as a blank space in the column labeled “Status” or “Sts”
    eee
    Page 2 of 9
    KEYSIGHT Measurement Report
    TECHNOLOGIES Certificate Number 1-8550569912-1
    Pekformaiice Test Results Summary
    Test Name : As Received Status SYSTEM VERIFICATION Failed FREQUENCY RANGE AND ACCURACY Passed OUTPUT POWER ACCURACY - Passed OUTPUT POWER RANGE AND LINEARITY Passed INPUT NOISE FLOOR LEVEL Passed SYSTEM CROSSTALK Passed SYSTEM TRACE NOISE Passed COMPRESSION Passed DYNAMIC ACCURACY Passed
    inc ra Page 3 of 9
    This report shall not be reproduced except in full, without the written approval of the laboratory
    KEYSIGHT
    TECHNOLOGIES
    Model 8752C Options Tested 003 004
    Serial 3410A02579
    Measurement Report Certificate Number 1-8550569912-1
    Firmware Rev
    Test Date 4 Feb 2017 Condition As Received
    MAXIMUM Status
    TEST CONDITIONS MINIMUM MEASURED REFLECTION TRACKING 300kHz-1.3GHz ~0.20 dB -0.05 dB 1.3GHz-3,0GHz 0.30 dB ~0.09 dB DIRECTIVITY 300kHz- 10MHz +30.0 dB 43.6 dB 10MHz-1.3GHz +40.0 dB 53.8 dB 1.3GHz-3.0GHz +35.0 dB 42.4 dB SOURCE MATCH (REFLECTION) 300kHz- 1.3GHz +30.0 dB 25.6 dB 1.3GHz-3.0GHz +25.0 dB 20.0 dB SOURCE MATCH (TRANSMISSION) 300kHz- 1.3GHz +23.0 dB 33.6 dB 1.3GHz-3.0GHz +20.0 dB 26.5 dB LOAD MATCH 300kHz- 1.3GHz +23.0 dB 29.1 dB 1.3GHz-3.0GHz +20.0 dB 27.3 dB TRANSMISSION TRACKING 300kHz-1.3GHz ~0.20 dB 0.13 dB 1.3GHz-3.0GHz ~0.30 dB 0.21 dB
    FREQUENCY RANGE AND ACCURACY
    TEST CONDITIONS
    0.300000 MHz 5.000000 MHz 16.000000 MHz 31.000000 MHz 60.999999 MHz 121.000000 MHz 180.000000 MHz
    MEASURED
    +0.20 dB +0.30 dB
    +0.20 dB +0,30 dB
    Passed
    MAXIMUM Status
    MINIMUM -3.00 Hz —2.04 Hz —50 Hz -34 Hz -160 Hz -109 Hz ~310 Hz —211 Hz 610 Hz -415 Hz -1210 Hz -823 Hz —1800 Hz —1224 Hz
    +160 Hz +310 Hz +610 Hz +1210 Hz +1800 Hz
    Page 4 of 9
    KEYSIGHT Measurement Report
    TECHNOLOGIES Certificate Number 1-8550569912-1
    Model 8752C Serial 3410A02579 —‘ Firmware Rev Test Date 4 Feb 2017 Options Tested 003 004 Condition As Received FREQUENCY RANGE AND ACCURACY (cont.)
    TEST CONDITIONS MINIMUM MEASURED MAXIMUM Status
    310,000000 MHz -3100 Hz —2108 Hz +3100 Hz
    700.000000 MHz ~7000 Hz -4761 Hz +7000 Hz 1300.000000 MHz -~13000 Hz -8844 Hz +13000 Hz 2000,000000 MHz 20000 Hz -13610 Hz +20000 Hz 3000.000000 MHz 30000 Hz —20416 Hz +30000 Hz OUTPUT POWER ACCURACY Passed
    TEST CONDITIONS MINIMUM MEASURED MAXIMUM Status
    POWER ACCURACY (dB)
    Output = -10 dBM
    0.300 MHz —1.00 dB 0.34 dB +1.00 dB 20.000 MHz —1.00 dB 0.03 dB +1,00 dB 50,000 MHz —1.00 dB —0.03 dB +1.00 dB 100.000 MHz -1.00 dB 0.11 dB +1,00 dB 200.000 MHz —1.00 dB —0.10 dB +1,00 dB 500.000 MHz —1,00 dB —0.22 dB +1.00 dB 1000.000 MHz —1.00 dB -0,19 dB +1,00 dB 1300.000 MHz. -1.00 dB 0.15 dB +1.00 dB 2000.000 MHz —1.00 dB -0.14 dB +1,00 dB 3000.000 MHz -1,00 dB -0,10 dB +1.00 dB OUTPUT POWER RANGE AND LINEARITY Passed TEST CONDITIONS MINIMUM MEASURED MAXIMUM Status
    LINEARITY (dB from linear) Power Level (dBm)
    Frequency = 300 KHz
    —-15 dBm —0,20 dB —0.03 dB +0.20 dB 12 dBm —0.20 dB —0.03 dB +0.20 dB -10 dBm ~0.20 dB —0.03 dB +0,20 dB -8 dBm —0,20 dB —0.01 dB +0.20 dB —6 dBm -0.20 dB 0.00 dB +0.20 dB —4 dBm —0.20 dB 0.00 dB +0.20 dB —2 dBm -0,20 dB 0.02 dB +0.20 dB 0 dBm —0.50 dB 0,02 dB +0.50 dB
    i UEEEEEENEE: SSapay-apea- pad
    Page 5 of 9
    This report shall not be reproduced except in full, without the written approval of the laboratory
    KEYSIGHT Measurement Report
    Certificate Number 1-8550569912-1
    TECHNOLOGIES
    Model 8752C — Serial 3410A02579 — Firmware Rev
    Options Tested 003 004
    Test Date 4 Feb 2017 Condition As Received
    OUTPUT POWER RANGE AND LINEARITY (cont.)
    TEST CONDITIONS MINIMUM
    +2 dBm -0.50 dB +4dBm -0.50 dB +5 dBm —0.50 dB +10 dBm -0,50 dB
    Frequency = 1.3 GHz
    15 dBm -0.20 dB —12 dBm —0.20 dB -10 dBm —0.20 dB -8 dBm —0.20 dB 6 dBm -0.20 dB —4 dBm —0.20 dB —2 dBm —0,20 dB 0 dBm 0.50 dB +2 dBm 0.50 dB +4 dBm ~0.50 dB +5 dBm —0.50 dB +10 dBm —0.50 dB
    Frequency = 3.0 GHz
    15 dBm —0.20 dB -12 dBm —0.20 dB —10 dBm —0.20 dB -8 dBm —0.20 dB ~6 dBm —0.20 dB —4 dBm —0.20 dB —2 dBm -0.20 dB 0 dBm ~0.50 dB +2 dBm -0.50 dB +4 dBm —0,50 dB +5 dBm —0.50 dB +10 dBm —0.50 dB POWER RANGE (Option 004) RANGE LEVEL -15to+10 -10 —1.00 dB —25to+0 -20 -1.50 dB -35to-10 -30 -1.70 dB 45 to-20 -40 -1.90 dB 55 to-30 -50 —2.20 dB -65to-40 -60 ~2.50 dB -75 to -50 -70 —2.80 dB -85 to -60 -80 -3.10 dB
    MEASURED
    —0.04 dB ~0.03 dB —0.03 dB -0,02 dB -0.01 dB
    0.00 dB
    0.00 dB
    0.00 dB -0.01 dB —0.02 dB —0.04 dB —0.11 dB
    —0.05 dB —0.04 dB —0.04 dB —0.03 dB -0.01 dB 0.00 dB 0.01 dB 0.00 dB 0.00 dB 0,00 dB -0.01 dB -0.04 dB
    0.00 dB 0.05 dB 0.01 dB 0.05 dB —0.05 dB 0.01 dB —0.03 dB 0.00 dB
    MAXIMUM Status
    +0.50 dB +0.50 dB +0.50 dB +0.50 dB
    +0,20 dB +0,20 dB +0.20 dB +0.20 dB +0,20 dB +0.20 dB +0,20 dB +0.50 dB +0.50 dB +0,50 dB +0,50 dB +0.50 dB
    +0.20 dB +0,20 dB +0,20 dB +0,20 dB +0.20 dB +0.20 dB +0,20 dB +0.50 dB +0.50 dB +0,50 dB +0.50 dB +0,50 dB
    +1,00 dB +1.50 dB +1,70 dB +1,90 dB +2.20 dB +2,50 dB +2.80 dB +3,10 dB
    Page 6 of 9
    KEYSIGHT Measurement Report
    HECTINGEOGIES Certificate Number 1-8550569912-1 Model 8752C Serial 3410A02579 — Firmware Rev Test Date 4 Feb 2017 Options Tested 003 004 Condition As Received INPUT NOISE FLOOR LEVEL Passed TEST CONDITIONS MEASURED MAX Status
    TRANSMISSION TEST PORT
    FREQUENCY IFBW
    300kHz-3.0GHz 3000 Hz -100 dBm -90 dBm 300kHz-3.0GHz 10 Hz -123 dBm -110 dBm SYSTEM CROSSTALK Passed TEST CONDITIONS MEASURED MAXIMUM Status FREQUENCY 300kHz-3.0GHz -119.6 dB —100.0 dB SYSTEM TRACE NOISE Passed TEST CONDITIONS MEASURED MAXIMUM Status At 0 dBm Output Power 3kHz IF Bandwidth CW Sweep MAGNITUDE in dB(RMS) PHASE in Deg(RMS) REFLECTION: 300kHz-3.0GHz 0.0033 dB 0.0060 dB 300kHz-3.0GHz 0.023 Deg 0.038 deg TRANSMISSION: 300kHz-3.0GHz 0.0024 dB 0.0060 dB 300kHz-3.0GHz 0.016 Deg 0.038 deg
    aS Page 7 of 9
    This report shall not be reproduced except in full, without the written approval of the laboratory
    KEYSIGHT
    TECHNOLOGIES
    Model 8752C _ Serial 3410A02579
    Options Tested 003 004
    TEST COND. MEASURED MAGNITUDE 0.05 GHz 0.021 dB +0.450 dB 1.00 GHz 0.058 dB +0.450 dB 1.30 GHz 0.062 dB +0.450 dB PHASE 0.05 GHz 0.32 Deg +6.00 deg 1.00 GHz 1.00 Deg +6.00 deg 1.30 GHz 1.19 Deg +6,00 deg TEST CONDITIONS MINIMUM MEASURED TRANSMISSION INPUT POWER 20 dBm -0.058 dB 0.016 dB ~30 dBm (REF) -0,050 dB 0.012 dB 40 dBm —0.050 dB 0.008 dB 50 dBm 0.053 dB 0.023 dB -60 dBm ~0.060 dB 0.022 dB -70 dBm —0.115 dB 0.022 dB -80 dBm 0.285 dB —0.007 dB -90 dBm —0.860 dB —0.043 dB -100 dBm —2.500 dB —0.068 dB ~110 dBm —5.400 dB 0.884 dB (PHASE) (CALCULATED) INPUT POWER -20 dBm ~0.460 deg -0.104 Deg -30 dBm —0.350 deg —0.078 Deg —40 dBm 0.360 deg —0.050 Deg —50 dBm —0.380 deg 0.149 Deg -60 dBm ~0.400 deg 0.142 Deg -70 dBm -0.700 deg -0.143 Deg -80 dBm -1.900 deg 0.047 Deg
    Measurement Report Certificate Number 1-8550569912-1
    Firmware Rey
    MAXIMUM Status
    MAXIMUM Status
    +0.058 dB +0.050 dB +0.050 dB +0.053 dB +0.060 dB +0.115 dB +0.285 dB +0.860 dB +2,500 dB +5,400 dB
    +0.460 deg +0.350 deg +0.360 deg +0.380 deg +0.400 deg +0.700 deg +1.900 deg
    Test Date 4 Feb 2017 Condition As Received
    Passed
    Passed
    Page 8 of 9
    KEYSIGHT Measurement Report
    TECHNOLOGIES Certificate Number 1-8550569912-1
    Model 8752C — Serial 3410A02579 +‘ Firmware Rev Test Date 4 Feb 2017 Options Tested 003 004
    Condition As Received DYNAMIC ACCURACY (cont.)
    TEST CONDITIONS MINIMUM
    MEASURED MAXIMUM _ Status -90 dBm 6.000 deg 0.286 Deg +6,000 deg -100 dBm —18.00 deg 0.44 Deg +18,00 deg -110 dBm 55,00 deg 5.55 Deg +55.00 deg
    LEU UUUEEtEIEEEIEE ESE SSSSEESEESSSSSSSSSSNNE | >5">5E7 WPF Ts
    Page 9 of 9
    This report shall not be reproduced except in full, without the written approval of the laboratory

**Output Format Example 11:**
    **Information of Instrument Calibrated**
    - Instrument Calibrated: RF Vector network analyzer
    - Model: 8752C
    - Serial Number: 3410A02579
    - Date of Calibration: February 4th, 2017
    
    **Information of Calibration Device 1**
    - Calibration Device: DC-18 GHz power splitter, type N, 50 ohm
    - Model Number of Calibration Device: 11667A
    - Serial Number of Calibration Device: 11667A15987
    - Due Date of Calibration Device: February 5th, 2018
    
    **Information of Calibration Device 2**
    - Calibration Device: Primary frequency standard
    - Model Number of Calibration Device: 5071A
    - Serial Number of Calibration Device: 5071A01633
    - Due Date of Calibration Device: January 27th, 2018
    
    **Information of Calibration Device 3**
    - Calibration Device: Universal Counter, 225 MHz, 12 digit/s, 150 ps. GPIB, RS232
    - Model Number of Calibration Device: 53132A
    - Serial Number of Calibration Device: 53132A07171
    - Due Date of Calibration Device: December 7th, 2017

    **Information of Calibration Device 4**
    - Calibration Device: Power Sensor, 100 kHz to 4.2 GHz, -30 to +20 dBm
    - Model Number of Calibration Device: 8482A 
    - Serial Number of Calibration Device: 8482A14928
    - Due Date of Calibration Device: June 1st, 2017

    **Information of Calibration Device 5**
    - Calibration Device: 0-110dB programmable step ATTENUATOR 0-18GHz
    - Model Number of Calibration Device: 8496H 
    - Serial Number of Calibration Device: 8496H00390
    - Due Date of Calibration Device: June 8th, 2018

    **Information of Calibration Device 6**
    - Calibration Device: 50-Ohm Type-N calibration kit
    - Model Number of Calibration Device: 85032B 
    - Serial Number of Calibration Device: 85032B00563
    - Due Date of Calibration Device: July 22nd, 2017

    **Information of Calibration Device 7**
    - Calibration Device: Power meter - EPM series, dual channel
    - Model Number of Calibration Device: E4419B 
    - Serial Number of Calibration Device: E4419B12962
    - Due Date of Calibration Device: May 27th, 2018

**Text Information Example 12**
    Bruel & Kjzer +
    The Calibration Laboratory yy, = 3 Skodsborgvej 307, DK-2850 Nerum, Denmark “thy Tiel iw
    = % CAL Regan. 307 “,
    CERTIFICATE OF CALIBRATION No.: cpK1801974 Page 1 of 10
    CALIBRATION OF:
    Conditioning Amplifier: 2692 E 2400305 Identification: VISDOE
    CUSTOMER:
    DSO National Laboratories 14 Science Park Drive 118226 Singapore Singapore
    CALIBRATION CONDITIONS:
    Preconditioning: 4 hours at 23° C+3°C
    Environment conditions: Air Temperature: +3°C Air Pressure: +5kPa Relative Humidity: +25 % RH
    PROCEDURE:
    The instrument has been calibrated in accordance with the requirements as specified by vendor, using Calibration Procedure No. P_2692_A11.
    RESULTS: [| Initial calibration [| Calibration prior to repair/adjustment
    Calibration without repair/adjustment L ] Calibration after repair/adjustment
    The reported expanded uncertainty of measurement is stated as the standard uncertainty of measurement multiplied by the coverage factor k = 2, which for a normal distribution corresponds to a coverage probability of approximate- ly 95 %. The standard uncertainty of measurement has been determined in accordance with EA-4/02
    The accreditation assures the traceability to the international units system SI.
    Measurements marked with an asterisk (*) are outside our range of accreditation.
    Date of Calibration: 2018-03-09 Certificate issued: 2018-03-09
    “er.
    Mikail 6nder engaard Hansen Calibration Technician Approved signatory
    Reproduction of the complete certificate is allowed. Parts of the certificate may only be reproduced after written permission.
    Bruel & Kjzr
    The Calibration Laboratory Skodsborgyej 307, DK-2850 Nerum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 2 of 10
    RESULTS:
    Serial number: 2400305
    Date: 2018.03.09 Calibration software: 170557 ver.2.86 Nexus software vers.: 02 02 00
    Nexus configuration:
    Channel 1: CHARGE INPUT 2X2692 NO AUX Channel 2: CHARGE INPUT 2X2692 NO AUX Channel 3: CHARGE INPUT ZX2692 NO AUX Channel 4: CHARGE INPUT 2X2692 NO AUX
    NOTE: Measurements marked with an asterisk (*) are outside our scope of accreditation.
    Channel Type: CHARGE INPUT LOW NOISE ZX 2692 Channel No: 1
    All measurements made non floating on input and output. Transducer sensitivity: 1 nC/ms-2. All signals applied via 1 nF adaptor.
    Calibrated output: The gain from input to calibrated output, is calculated as measured output level, relative to measured input level. Levels are measured by means of a DMM.
    Generator frequency: 1 kHz
    When applying amplitudes below 31.62 mv (90 dBuV) a 40 @B attenuator is used. Nexus: LP 100kHz
    Output bandwidth limited with external 22.4 kHz LP filter.
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty Nexus setting Input Level HP 10 100m 5.01187 volt V/ms-2 0.0989 0.1012 0.0999 0.0003 HP 10 316m 5.01187 volt V/ms-2 0.3126 0.3199 0.3160 0.0008 HP 10 1 1.77828 Volt V/ms-2 0.9886 1.0116 1.0018 0.0025 HP 10 3.16 0.56234 Volt v/ms-2 3.1261 3.1989 3.1682 0.0077 HP 10 10 0.17783 Volt vV/ms-2 9.8855 10.1158 9.9970 0.0254 HP 10 31.6 0.05623 volt V/ms-2 31.2608 31.9890 31.6051 0.1022 HP 10 100 0.01778 Volt vV/ms-2 98.8553 101.1579 99.8718 0.2537 HP 10 316 0.00562 volt V/ms -2 312.6079 319,8895 316.9964 0.8020 HP 10 1k 0.00178 Volt V/ms-2 988.5531 1011.5795 1003.9835 2.5361 HP 10 3.16k 0.00056 Volt V/ms-2 3126.0794 3198.8951 3172.6089 10.2105 HP O01 1 1.77828 Volt V/ms-2 0.9886 1.0116 1.0017 0.0025 HP 01 10 0.17783 Volt V/ms-2 9.8855 10.1158 9.9977 0.0254
    Lowpass filters: The frequency response of Lowpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: 1 Volt (120 dBuv) Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 0.1Hz (LP 100 k results not valid with WH 3219 option)
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency
    LP 0.1k 20 Hz % -1.14 1.16 -0.06 *
    LP O.1k 100 Hz % -14.89 6.67 -10.91 0.42
    Lp 1k 200 Hz % -1.14 1.16 0.07 0.25
    Lp 1k 1000 Hz % -14.89 -6.67 -10.47 0.42
    LP 3k 600 Hz % -1.14 1.16 0.12 0.25
    LP 3k 3000 Hz % -14.89 -6.67 -10.49 0.42
    LP 10k 600 Hz % -1.14 1.16 0.15 0.25
    LP 10k 3000 Hz % 14.89 -6.67 -10.44 0.42
    LP 30k 6000 Hz % -1.14 1.16 0.32 0.25
    LP 30k 30000 Hz % 7-14.89 -6.67 -9.67 *
    LP 100 k 20000 Hz % -1.14 1.16 0.60 Ld
    LP 100 k 60000 Hz % -4.50 4.71 0.45 *
    LP 100 k 100000 Hz % -18.72 -2,28 7-14.13 *
    9
    Rev, 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nerum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 P
    ge 3 of 10
    Highpass filters: The frequency response of Highpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: see below (2.239 Volt = 127 dBuVv) Nexus: LP 100kHz
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency Input
    HP 0.1 10 0.1 Hz 223.9mV % 16.82 -4.50 -11.38 * HP 0.1 1 0.1 Hz 2.239 V % -16.82 74.50 -11.79 x HP 0. 1 0.5 Hz 2.239 V % -2.28 2.33 -0.68 bl HP 1 1 1.0 Hz 2.239 V % -16.82 -4.50 714.62 ied HP 1 1 5.0 Hz 2.239 V % -2.28 2.33 -0.70 * HP 1 1 10.0 Hz 2.239 V % 715.86 -5.59 -10.42 0.53 HP 1 1 50.0 Hz 2.239 V % -1.14 1.16 -0.21 0.25 Inherent noise: The Inherent Noise is measured by connecting a short-circuit plug to the input, and measuring the output level by means of a DMM. Nexus: Sens. 31.6 V/ms-2 (90dB Gain), HP 1Hz, LP 100kHz Input shorted via 1 nF Output bandwidth limited with external filter. Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty 2 Hz - 22.4 kHz uv 5.01 1.98 ty Reference Generator: Measure output level from internal generator. Lower Upper Measured Calibration Unit Limit Limit Value Uncertainty dBuv 119.90 120.10 120.03 * Test Tone dBuv 119.90 120.10 120.03 a
    Distortion:
    Generator signal: 127 dBuV (2.24 volt), 1 kHz
    Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 1Hz, LP 30kHz
    Basetone is rejected with a notchfilter.
    Output of the notch filter is digitized with the HP3458A voltmeter, and 2. harmonic and 3. harmonic are determined with a DFT.
    Upper Measured Calibration Parameter Unit Limit Value Uncertainty
    oS — Rey. 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nzrum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 4 of 10
    Channel Type: CHARGE INPUT LOW NOISE ZX 2692 Channel No: 2
    All measurements made non floating on input and output. Transducer sensitivity: 1 nC/ms-2. All signals applied via 1 nF adaptor.
    Calibrated output: The gain from input to calibrated output, ig calculated as measured output level, relative to measured input level. Levels are measured by means of a DMM,
    Generator frequency: 1 kHz
    When applying amplitudes below 31.62 mv (90 dBuv) a 40 dB attenuator ig used. Nexus: LP 100kHz
    Output bandwidth limited with external 22.4 kHz LP filter.
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Input Level
    HP 10 100m 5.01187 volt V/ms-2 0.0989 0.1012 0.0999 0.0003 HP 100 0=(316m 5.01187 volt V/ms-2 0.3126 0.3199 0.3159 0.0008 HP 10 1 1.77828 Volt V/ms-2 0.9886 1,0116 1.0016 0.0025 HP 10 3.16 0.56234 Volt V/ms-2 3.1261 3.1989 3.1674 0.0077 HP 10 10 0.17783 Volt V/ms -2 9.8855 10.1158 9.9956 0.0254 HP 10 31.6 0.05623 Volt V/ms -2 31.2608 31.9890 31.5996 0.1022 HP 10 100 0.01778 Volt V/ms -2 98.8553 101.1579 99.8617 0.2537 HP 10 060316 0.00562 volt V/ms-2 312.6079 319.8895 317.0015 0.8020 HP 10 1k 0.00178 Volt V/ms-2 988.5531 1011.5795 1003.7014 2.5361 HP 10 = 43.16k 0.00056 Volt V/ms-2 3126.0794 3198.8951 3170.3610 10.2105 HP 01 1 1.77828 Volt V/ms-2 0.9886 1.0116 1,0014 0.0025 HP OL 10 0.17783 Volt V/ms-2 9.8855 10.1158 9.9954 0.0254
    Lowpass filters: The frequency response of Lowpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: 1 volt (120 dBuv) Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 0.1Hz (LP 100 k results not valid with WH 3219 option) Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency
    LP 0.1k 20 Hz % -1,14 1.16 -0.02 * LP O0.1k 100 Hz % ~14.89 -6.67 -10.82 0.42 LP ok 200 Hz % -1.14 1.16 0.04 0.25 LP ok 1000 Hz % 714.89 -6.67 -10.85 0.42 LP 3k 600 Hz % 71.14 1.16 0.07 0.25 LPoO3k 3000 Hz % 14.89 -6.67 -10,62 0.42 LP 10k 600 Hz % -1,14 1.16 0.11 0.25 LP 10k 3000 Hz % 714.89 -6.67 -10.71 0.42 LP 30k 6000 Hz % 71.14 1.16 0.27 0.25 LP 30k 30000 Hz % -14.89 6.67 9.94 * LP 100 k 20000 Hz % -1.14 1.16 0.57 hd LP 100 k 60000 Hz % -4.50 4.71 0.48 hd LP 100 k 100000 Hz % 18,72 72.28 -14.02 *
    SOC -- r SSSSSSSSSSSFSFSMMSSSSMMmmmfMseF Rev, 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nzrum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 5 of 10
    Highpass filters: The frequency response of Highpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by meane of a DMM.
    Input Level: see below (2.239 Volt = 127 dBuv) Nexus: LP 100kHz
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency Input
    HP 0.1 10 0.1 Hz 223.9mv % -16.82 -4.50 -10.98 *
    EP 0.1 1 0.1 Hz 2.239 V % -16.82 -4.50 -11.98 *
    HP 0.1 1 0.5 Hz 2.239 V % -2.28 2.33 -0.54 bed
    HP 1 1 1.0 Hz 2,239 V % -16.82 -4.50 -14.44 a
    HP 1 1 5.0 Hz 2.239 V % 2.28 2.33 70.61 i
    HP 10 1 10.0 Hz 2.239 V % -15.86 5.59 -10.32 0.53
    HP 10 1 50.0 Hz 2.239 V % -1.14 1.16 -0.20 0.25 Inherent noise: The Inherent Noise is measured by connecting a short-circuit plug to the input, and measuring the output level by means of a DMM. Nexus: Sens. 31.6 V/ms-2 (90dB Gain), HP 1Hz, LP 100kHz Input shorted via 1 nF Output bandwidth limited with external filter.
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    2 Hz - 22.4 kHz uv 5.01 2.02 be Reference Generator: Measure output level from internal generator.
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    Ref Tone dBuv 119.90 120.10 120.03 *
    Test Tone dBuv 119.90 120.10 120.03 bed Distortion:
    Generator signal: 127 dBuv (2.24 Volt), 1 kHz
    Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 1Hz, LP 30kHz
    Basetone ie rejected with a notchfilter.
    Output of the notch filter is digitized with the HP3458A voltmeter, and 2. harmonic and 3. harmonic are determined with a DFT.
    Upper Measured Calibration
    Parameter Unit Limit Value Uncertainty 2. Harmonic % 0.0030 0.0002 J 3. Harmonic % 0.0030 0.0001 a
    Rev, 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nerum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 6 of 10
    Channel Type: CHARGE INPUT LOW NOISE 2X 2692 Channel No: 3
    All measurements made non floating on input and output, Transducer sensitivity: 1 nC/ms-2. All signals applied via 1 nF adaptor.
    Calibrated output: The gain from input to calibrated output, is calculated as measured output level, relative to measured input level. Levels are measured by means of a DMM.
    Generator frequency: 1 kHz
    When applying amplitudes below 31.62 mv (90 dBuV) a 40 dB attenuator is used. Nexus: LP 100kHz
    Output bandwidth limited with external 22.4 kHz LP filter.
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Input Level
    HP 10 8=6100m 5.01187 Volt V/ms-2 0.0989 0.1012 0.1000 0.0003 HP 10 0 8=6316m 5.01187 volt V/ms-2 0.3126 0.3199 0.3162 0.0008 HP 10 1 1.77828 Volt v/ms-2 0.9886 1.0116 1.0024 0.0025 HP 10 «3.16 0.56234 volt V/ms-2 3.1261 3.1989 3.1697 0.0077 HP 10 10 0.17783 volt V/ms-2 9.8855 10.1158 9.9967 0.0254 HP 10 «(31.6 0.05623 Volt V/ms-2 31.2608 31.9890 31.6036 0.1022 HP 10 100 0.01778 Volt V/mp -2 98.8553 101.1579 99.8795 0.2537 HP 10 = 60316 0.00562 Volt V/ms-2 312.6079 319.8895 317.0511 0.8020 HP 10 1k 0.00178 volt V/ms-2 988.5531 1011.5795 1003.7189 2.5361 EHP 10 3.16k 0.00056 Volt V/ms-2 3126.0794 3198.8951 3166.6839 10.2105 HP 01 1 1.77828 Volt V/ms-2 0.9886 1.0116 1.0021 0.0025 HP O01 10 0.17783 Volt V/ms-2 9.8855 10.1158 9.9960 0.0254
    Lowpass filters: The frequency response of Lowpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: 1 volt (120 dBuv) Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 0.1Hz (LP 100 k results not valid with WH 3219 option) Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency
    LP 0.1k 20 Hz % -1,14 1.16 0.12 * LP 0.1k 100 Hz % 14.89 -6.67 -10.69 0,42 LP 1k 200 Hz % 71.14 1.16 0.13 0.25 LP Ok 1000 Hz % -14,89 -6.67 -10.61 0.42 LP 3k 600 Hz % -1.14 1.16 0.14 0.25 LP 3k 3000 Hz % -14.869 ~6.67 -10.55 0.42 LP 10k 600 Hz % -1.14 1.16 0.21 0.25 LP 10k 3000 Hz % 714.89 -6.67 -9.82 0.42 LP 30k 6000 Hz % 71.14 1,16 0.33 0.25 LP 30k 30000 Hz % -14,89 -6.67 -9.67 * LP 100 k 20000 Hz % -1.14 1.16 0.63 hal LP 100 k 60000 Hz % -4.50 4.71 0.60 * LP 100 k 100000 Hz % -18.72 -2.28 -13.82 ia
    oe ESSE Rev. 2016-05-17
    Bruel. & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Narum, Denmark
    CERTIFICATE OF CALIBRATION
    No.; CDK1801974 Page 7 of 10
    Highpass filters: The frequency response of Highpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: see below (2.239 Volt = 127 dBuv) Nexus: LP 100kHz
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency Input i
    HP 0.1 10 1 Hz 223.9mV % -16.82 -4.50 711.49 *
    HP 0.1 1 0.1 Hz 2.239 V % -16.82 4.50 -11.91 *
    HP 0.1 1 0.5 Hz 2.239 V % -2.28 2.33 -0.35 2
    HP 1 1 1.0 Hz 2.239 V % -16.82 -4.50 -14.12 *
    HP 1 1 5.0 Hz 2.239 V % -2,28 2.33 -0.44 ha
    HP 10 1 0.0 Hz 2.239 V % -15.86 =5.59 -10.17 0.53
    HP 10 1 0.0 Hz 2.239 V % -1.14 1.16 -0.09 0.25 Inherent noise: The Inherent Noise is measured by connecting a short-circuit plug to the input, and measuring the output level by means of a DMM. Nexus: Sens. 31.6 V/ms-2 (90dB Gain), HP 1Hz, LP 100kHz Input shorted via 1 nF Output bandwidth limited with external filter.
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    2 Hz - 22.4 kHz uv 5.01 2.13 id Reference Generator: Measure output level from internal generator.
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    Ref Tone dBuv 119.90 120.10 120.03 *
    Test Tone dBuv 119.90 120.10 120.03 * Distortion:
    Generator signal: 127 dBuV (2.24 Volt), 1 kHz Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 1Hz, LP 30kHz Basetone is rejected with a notchfilter. Output of the notch filter is digitized with the HP3458A voltmeter, and 2. harmonic and 3. harmonic are determined with a DFT. Upper Measured Calibration
    Parameter Unit Limit Value Uncertainty 2. Harmonic % 0.0030 0.0001 e 3. Harmonic % 0.0030 0.0001 My
    SS SSS Rev. 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nerum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 8 of 10
    Channel Type: CHARGE INPUT LOW NOISE ZX 2692 Channel No: 4
    All measurements made non floating on input and output. Transducer sensitivity: 1 nC/ms-2. All signals applied via 1 nF adaptor.
    Calibrated output: The gain from input to calibrated output, is calculated as measured output level, relative to measured input level. Levels are measured by means of a DMM.
    Generator frequency: 1 kHz
    When applying amplitudes below 31.62 mV (90 dBuv) a 40 dB attenuator is used. Nexus: LP 100kHz
    Output bandwidth limited with external 22.4 kHz LP filter.
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Input Level
    HP 1000=«-100m 5.01187 Volt vV/ms -2 0.0989 0.1012 0.03999 0.0003 HP 10 316m 5.01187 volt V/ms-2 0.3126 0.3199 0.3158 0.0008 HP 10 1 1.77828 Volt vV/ms-2 0.9886 1.0116 1.0012 0.0025 HP 10 «3.16 0.56234 Volt V/ms-2 3.1261 3.1989 3.1662 0.0077 EP 10 10 0.17783 volt V/ms -2 9.8855 10.1158 9.9909 0.0254 HP 10 31.6 0.05623 Volt V/ms-2 31.2608 31.9890 31.5861 0.1022 HP 10 = 8=6100 0.01778 Volt V/ms-2 98.8553 101.1579 99.8230 0.2537 HP 1000©=«(316 0.00562 Volt V/ma -2 312.6079 319.8895 316.8838 0.8020 HP 10 1k 0.00178 volt V/ms -2 988.5531 1011.5795 1003.6042 2.5361 HP 10 = 3.16k 0.00056 Volt V/ms-2 3126.0794 3198.8951 3166.7119 10.2105 HP O01 1 1.77828 Volt V/ms-2 0.9886 1.0116 1.0009 0.0025 HP 01 10 0.17783 Volt V/ms-2 9.8855 10.1158 9.98681 0.0254
    Lowpass filtera: The frequency response of Lowpass filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: 1 Volt (120 dBuv) Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 0.1Hz (LP 100 k results not valid with WH 3219 option) Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency
    LP 0.1k 20 Hz % -1.14 1.16 70.05 ¥ LP 0,1k 100 Hz % 14.89 6.67 711.00 0.42 LP ok 200 Hz % 71.14 1.16 0.01 0.25 LPO k 1000 Hz % -14,89 -6.67 -10.39 0.42 LP O3k 600 Hz % -1.14 1.16 0.04 0.25 LPoo3 k 3000 Hz % -14.89 ~6.67 -10.40 0.42 LP 10k 600 Hz % -1.14 1.16 0.06 0.25 LP 10k 3000 Hz % 714.89 -6.67 -10.64 0.42 LP 30k 6000 Hz % 71.14 1.16 0.22 0.25 LP 30 k 30000 Hz % -14,89 -6.67 -9.83 * LP 100 k 20000 Hz % -1.14 1.16 0.53 w LP 100 k 60000 Hz % -4.50 4.71 0.58 * LP 100 k 100000 Hz % 18.72 2.28 ~13.86 bd
    Sor :C KC Sa SSFSFSSSSSSSSSSSSSSSSSSSSeheFeFeFesFsSSSSSSSSSSSSSSSe Rev. 2016-05-17
    Bruel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nztum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 9 of 10
    Highpass filters: The frequency response of Highpasa filters is calculated as measured output level relative to measured input level as percentage. Levels are measured by means of a DMM.
    Input Level: see below (2.239 Volt = 127 dBuv) Nexus: LP 100kHz
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty
    Nexus setting Frequency Input
    HP 0.1 10 0.1 Hz 223.9mV % -16.82 -4.50 7-11.50 *
    HP O.1 1 0.1 Hz 2.239 V % -16.82 -4.50 712.38 bel
    HP 0.1 1 0.5 Hz 2.239 V % -2.28 2.33 ~0.57 Ld
    HP 1 1 1.0 Hz 2.239 V % -16.82 -4.50 -14,75 *
    HP 1 1 5.0 Hz 2.239 V % -2.28 2.33 -0.65 Ld
    HP 10 1 10.0 Hz 2,239 V % 715.86 -5.59 -10.46 0.53
    HP 10 1 50.0 Hz 2.239 V % -1.14 1.16 70.26 0.25 Inherent noise: The Inherent Noise is measured by connecting a short-circuit Plug to the input, and measuring the output level by means of a DMM. Nexus: Sens. 31.6 V/ms-2 (90dB Gain), HP 1Hz, LP 100kHz Input shorted via 1 nF Output bandwidth limited with external filter.
    Lower Upper Measured Calibration
    Parameter Unit Limit Limit Value Uncertainty
    2 Hz - 22.4 kHz uv 5.01 1.92 *
    Reference Generator: Measure output level from internal generator.
    Lower Upper Measured Calibration Parameter Unit Limit Limit Value Uncertainty Ref Tone dBuv 119.90 120.10 120.03 i Test Tone dBuv 119.90 120.10 120.03 * Distortion:
    Generator signal: 127 dBuV (2.24 volt), 1 kHz Nexus: Sens. 1 V/ms-2 (0 dB Gain), HP 1Hz, LP 30kHz Basetone is rejected with a notchfilter. Output of the notch filter is digitized with the HP3458A voltmeter, and 2. harmonic and 3. harmonic are determined with a DFT. Upper Measured Calibration
    Parameter Unit Limit Value Uncertainty 2. Harmonic % 0.0030 0.0001 = 3. Harmonic % 0.0030 0.0001 *
    Calibration Equipment:
    Type Serial No. Reg. No. DMM 3458A 2823A20845 132527037 Generator DS360 123404 131300033 ATAC Filter 014 116504014 1kHz Notch Filter 001 115162001 Inductive Divider 007 115161007 InF Input Adapter 010 110652010 InF Input Adapter 024 110652024 InF Input Adapter 036 110652036 InF Input Adapter 041 110652041
    Rev, 2016-05-17
    Briel & Kjzer
    The Calibration Laboratory Skodsborgvej 307, DK-2850 Nerum, Denmark
    CERTIFICATE OF CALIBRATION
    No.: CDK1801974 Page 10 of 10
    DANAK
    DANAK is the national accreditation body in Denmark in compliance with EU regulation No. 765/2008.
    DANAK participates in the multilateral agreements for testing and calibration under European co-operation for Accreditation (EA) and under International Laboratory Accreditation Cooperation (ILAC) based on peerevaluation. Accredited test reports and calibration certificates issued by laboratories accredited by DANAK are recognized cross border by members of EA and ILAC equal to test reports and calibration certificates issued by these members’ accredited laboratories.
    The use of the accreditation mark on test reports and calibration certificates or reference to accreditation, documents that the service is provided as an accredited service under the company's DANAK accreditation.
    a Rev. 2016-05-17

**Output Format Example 12**
    **Information of Instrument Calibrated**
    - Instrument Calibrated: Conditioning Amplifier
    - Model: 2692
    - Serial Number: E 2400305
    - Date of Calibration: March 9th, 2018
    
    **Information of Calibration Device 1**
    - Calibration Device: DMM 3458A
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 2823A20845
    - Due Date of Calibration Device: Not Mentioned
    
    **Information of Calibration Device 2**
    - Calibration Device: Generator DS360
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 123404
    - Due Date of Calibration Device: Not Mentioned
    
    **Information of Calibration Device 3**
    - Calibration Device: ATAC Filter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 014
    - Due Date of Calibration Device: Not Mentioned
    
    **Information of Calibration Device 4**
    - Calibration Device: 1kHz Notch Filter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 001
    - Due Date of Calibration Device: Not Mentioned
    
    **Information of Calibration Device 5**
    - Calibration Device: Inductive Divider
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 007
    - Due Date of Calibration Device: Not Mentioned

    **Information of Calibration Device 6**
    - Calibration Device: Inf Input Adapter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 010
    - Due Date of Calibration Device: Not Mentioned

    **Information of Calibration Device 7**
    - Calibration Device: Inf Input Adapter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 024
    - Due Date of Calibration Device: Not Mentioned

    **Information of Calibration Device 8**
    - Calibration Device: Inf Input Adapter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 036
    - Due Date of Calibration Device: Not Mentioned

    **Information of Calibration Device 9**
    - Calibration Device: Inf Input Adapter
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 041
    - Due Date of Calibration Device: Not Mentioned
    
"""

# LLM 2 Prompt
system_message_entity_prompt = """
**Task:** Your task is to analyze the given text information and generate a structured representation with identified nodes and relationships.

**Instructions:**
    1. Identify key entities, concepts, or objects mentioned in the text. These will serve as nodes in the structured representation.
    2. Determine the relationships between these entities. Relationships can include actions, associations, dependencies, or any other relevant connections mentioned in the text.
    3. Organize the information into a structured format, where nodes are represented as entities, and relationships are represented as connections between these entities.
    4. Provide a clear and coherent output that effectively communicates the structured representation of the given text information.
    5. Do not use single quotation.
    6. Represent relationships in triplets where the first element represents the starting node, the second element represents the relationship name, and the third element represents the end node.
    7. The name of the relationship must always be "was calibrated by".
    8. The relationship always has one attributes which is the calibration date.
    9. Below is a list of examples. Strictly follow the format of the examples provided.

**Text Information Example 1**
    --Information of Instrument Calibrated--
    Instrument Calibrated: DC Power Supply
    Model Number of Calibrated Instrument: QL355T
    Serial Number of Calibrated Instrument: 243382
    Date of Calibration: June 21st, 2023

    --Information of Calibration Device 1--
    Calibration Device: Digital Precision Multimeter
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: 3501005
    Due Date of Calibration Device: September 15th, 2023

**Output Format Example 1:**
    Nodes:
    1: ["DC Power Supply", "device", {{"modelNumber":"QL355T", "serialNumber":"243382"}}]
    2: ["Digital Precision Multimeter", "device", {{"modelNumber":"Not Mentioned", "serialNumber":"3501005", "dueDate":"September 15th, 2023"}}]
    
    Relationships:
    1: ["DC Power Supply", "was calibrated by", "Digital Precision Multimeter" {{"calibrationDate":"June 21st, 2023"}}]

**Example Output Explanation 1:**
    - **Nodes:**
      - Node 1: Represents "DC Power Supply" as a device with the attributes "model number" and "serial number".
      - Node 2: Represents "Digital Precision Multimeter" as a device with the attributes "model number", "serial number" and "due date".
    
    - **Relationships:**
      - Relationship 1: Indicates that "DC Power Supply" was calibrated by "Digital Precision Multmeter" with the attribute "calibration date".

**Text Information Example 2**
    --Information of Instrument Calibrated--
    Instrument Calibrated: MMM Oven
    Model Number of Calibrated Instrument: VC 111 ECO
    Serial Number of Calibrated Instrument: H190449
    Date of Calibration: May 2nd, 2023

    --Information of Calibration Device 1--
    Calibration Device: Yokogawa Recorder with TC Sensors
    Model Number of Calibration Device: FX1012-7-2-L
    Serial Number of Calibration Device: S5W211878
    Due Date of Calibration Device: June 17, 2023

**Output Format Example 2:**
    **Nodes:**
    1: ["MMM Oven", "device", {{"modelNumber":"VC 111 ECO", "serialNumber":"H190449"}}]
    2: ["Yokogawa Recorder with TC Sensors", "device", {{"modelNumber":"FX1012-7-2-L", "serialNumber":S5W211878", "dueDate":"June 17th, 2023"}}]

    **Relationships:**
    1: ["MMM Oven", "was calibrated by", "Yokogawa Recorder with TC Sensors", {{"calibrationDate":"May 2nd, 2023"}}]

**Example Output Explanation 2:**
    - **Nodes:**
      - Node 1: Represents "MMM Oven" as a device with attributes "model number" and "serial number".
      - Node 2: Represents "Yokogawa Recorder with TC Sensors" as a device with the attributes "model number", "serial number" and "due date".
      
    - **Relationships:**
      - Relationship 1: Indicates that "MMM Oven" was calibrated by "Yokogawa Recorder with TC Sensors" with attribute "calibration date".

**Text Information Example 3: **
    --Information of Instrument Calibrated--
    Instrument Calibrated: Caliper
    Model Number of Calibrated Instrument: SERIES 530
    Serial Number of Calibrated Instrument: Not Mentioned
    Date of Calibration: Not Mentioned

    --Information of Calibration Device 1--
    Calibration Device: Not Mentioned
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: K112231Q
    Due Date of Calibration Device: Not Mentioned

**Output Format Example 3: **
    **Nodes:**
    1: ["Caliper", "device", {{"modelNumber":"SERIES 530", "serialNumber":"Not Mentioned"}}]
    2: ["Anonymous Calibration Device 1", "device", {{"modelNumber": "Not Mentioned", "serialNumber":"K112231Q", "dueDate": "Not Mentioned"}}]

    **Relationships:**
    1: ["Caliper", "was calibrated by", "Anonymous Calibration Device 1", {{"calibrationDate":"Not Mentioned"}}]

**Example Output Explanation 3:**
    - **Nodes:**
      - Node 1: Represents "Caliper" as a device with attributes "model number" and "serial number".
      - Node 2: Represents "Anonymous Calibration Device 1" as a device with the attributes "model number", "serial number" and "due date".
      
    - **Relationships:**
      - Relationshp 1: Indicates that "Caliper" was calibrated by "Anonymous Calibration Device 1" with attribute "calibration date".

**Text Information Example 4: **
    --Information of Instrument Calibrated--
    Instrument Calibrated: Digital multimeter, 6.5 digit
    Model Number of Calibrated Instrument: 34401A
    Serial Number of Calibrated Instrument: MY44007940
    Date of Calibration: 13 Mar 2015

    --Information of Calibration Device 1--
    Calibration Device: Function/Arbitrary Waveform Generator, 80 MHz
    Model Number of Calibration Device: 33250A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 31 Oct 2015

    --Information of Calibration Device 2--
    Calibration Device: Calibrator
    Model Number of Calibration Device: 5720A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 19 Apr 2015

    --Information of Calibration Device 3--
    Calibration Device: Amplifier
    Model Number of Calibration Device: 5725A
    Serial Number of Calibration Device: Not Mentioned
    Due Date of Calibration Device: 19 Apr 2015

**Output Format Example 4: **
    **Nodes:**
    1: ["Digital multimeter, 6.5 digit", "device", {{"modelNumber":"34401A", "serialNumber":"MY44007940"}}]
    2: ["Function/Arbitrary Waveform Generator, 80 MHz", "device", {{"modelNumber": "33250A", "serialNumber":"Not Mentioned", "dueDate": "31 Oct 2015"}}]
    3: ["Calibrator", "device", {{"modelNumber": "5720A", "serialNumber":"Not Mentioned", "dueDate": "19 Apr 2015"}}]    
    4: ["Amplifier", "device", {{"modelNumber": "5725A", "serialNumber":"Not Mentioned", "dueDate": "19 Apr 2015"}}]
    
    **Relationships:**
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", "Function/Arbitrary Waveform Generator, 80 MHz", {{"calibrationDate":"13 Mar 2015"}}]
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", " Calibrator", {{"calibrationDate":"13 Mar 2015"}}]
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", "Amplifier", {{"calibrationDate":"13 Mar 2015"}}]

**Example Output Explanation 4:**
    - **Nodes:**
      - Node 1: Represents "Digital multimeter, 6.5 digit" as a device with attributes "model number" and "serial number".
      - Node 2: Represents "Function/Arbitrary Waveform Generator, 80 MHz" as a device with the attributes "model number", "serial number" and "due date".
      - Node 3: Represents "Calibrator" as a device with the attributes "model number", "serial number" and "due date".
      - Node 4: Represents "Amplifier" as a device with the attributes "model number", "serial number" and "due date".
      
    - **Relationships:**
      - Relationshp 1: Indicates that "Digital multimeter, 6.5 digit" was calibrated by "Function/Arbitrary Waveform Generator, 80 MHz" with attribute "calibration date".
      - Relationshp 2: Indicates that "Digital multimeter, 6.5 digit" was calibrated by "Calibrator" with attribute "calibration date".
      - Relationshp 3: Indicates that "Digital multimeter, 6.5 digit" was calibrated by "Amplifier" with attribute "calibration date".

**Text Information Example 5: **
    **Information of Instrument Calibrated**
    - Instrument Calibrated: Electronic Balance
    - Model: LS 220A
    - Serial Number: 7001726
    - Date of Calibration: November 1st, 2017
    - Manufacturer: ETLV
    
    **Information of Calibration Device 1**
    - Calibration Device: Standard Weight Set
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 08343C

**Output Format Example 5: 
    **Nodes:**
    1: ["Electronic Balance", "device", {{"modelNumber":"LS 220A", "serialNumber":"7001726"}}]
    2: ["Standard Weight Set", "device", {{"modelNumber": "Not Mentioned", "serialNumber":"08343C", "dueDate": "Not Mentioned"}}]
    
    **Relationships:**
    1: ["Electronic Balance", "was calibrated by", "Standard Weight Set", {{"calibrationDate":"November 1st, 2017"}}]
    
**Example Output Explanation 5: **
    - **Nodes:**
      - Node 1: Represents "Electronic Balance" as a device with attributes "model number" and "serial number".
      - Node 2: Represents "Standard Weight Set" as a device with the attributes "model number", "serial number", and "due date".
    
    - **Relationships:**
      - Relationship 1: Indicates that "Electronic Balance" was calibrated by "Standard Weight Set" with attribute "calibration date".
    
"""

# LLM 3 Prompt
system_message_cypher_prompt = """
**Task:** You are a data scientist working for a company that is building a graph database. Your task is to generate Cypher queries to populate the database based on the given text information that has the nodes and relationships identified.

**Instructions:**
    1. Translate the identified nodes and relationships into Cypher queries to populate the graph database.
    2. Ensure that the Cypher queries are structured and adhere to the Cypher query language syntax.
    3. Provide clear and coherent Cypher queries that effectively represent the given text information in the graph database.
    4. Ensure that there is no trailing comma at the end of the generated Cypher query.
    5. Please do one statement per query. No multiquery should be allowed.
    6. The node label for the nodes have to be "Device".
    7. Output should be a valid cypher query. Do not add any remarks or explanations.
    8. Below is a list of examples. Strictly follow the format of the examples provided.
    9. Do not create duplicate nodes in the graph database

**Text Information Example 1:** 
    Nodes:
    1: ["DC Power Supply", "device", {{"modelNumber":"QL355T", "serialNumber":"243382"}}]
    2: ["Digital Precision Multimeter", "device", {{"modelNumber":"Not Mentioned", "serialNumber":"3501005", "dueDate":"September 15th, 2023"}}]
    
    Relationships:
    1: ["DC Power Supply", "was calibrated by", "Digital Precision Multimeter" {{"calibrationDate":"June 21st, 2023"}}]

**Output Format Example 1:**
    CREATE (:Device {{name: "DC Power Supply", type: "device", modelNumber: "QL355T", serialNumber: "243382"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "June 21st, 2023"}}]->(:Device {{name: "Digital Precision Multimeter", type: "device", modelNumber: "Not Mentioned", serialNumber: "3501005", dueDate: "September 15th, 2023"}})

**Example Output Explanation 1:**
    - Nodes Created:
      - Node "DC Power Supply" of type "device".
      - Node "Digital Precision Multimeter" of type "device".
    
    - Relationships Created:
      - Relationship indicating that "DC Power Supply" was calibrated by "Digital Precision Multimeter.

**Text Information Example 2:**
    Nodes:
    1: ["MMM Oven", "device", {{"modelNumber":"VC 111 ECO", "serialNumber":"H190449"}}]
    2: ["Yokogawa Recorder with TC Sensors", "device", {{"modelNumber":"FX1012-7-2-L", "serialNumber":S5W211878", "dueDate":"June 17th, 2023"}}]

    **Relationships:**
    1: ["MMM Oven", "was calibrated by", "Yokogawa Recorder with TC Sensors", {{"calibrationDate":"May 2nd, 2023"}}]

**Output Format Example 2:**
    CREATE (:Device {{name: "MMM Oven", type: "device", modelNumber: "VC 111 ECO", serialNumber: "H190449"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "May 2nd, 2023"}}]->(:Device {{name: "Yokogawa Recorder with TC Sensors", type: "device", modelNumber: "FX1012-7-2-L", serialNumber: "S5W211878", dueDate:"June 17th, 2023"}})

**Example Output Explanation 2:**
    - Nodes Created:
      - Node "MMM Oven" of type "device".
      - Node "Yokogawa Recorder with TC Sensors" of type "device".

    - Relationships Created:
      - Relationship indicating that "MMM Oven" was calibrated by "Yokogawa Recorder with TC Sensors".

**Text Information Example 3:**
    Nodes:
    1: ["Caliper", "device", {{"modelNumber":"SERIES 530", "serialNumber":"Not Mentioned"}}]
    2: ["Calibration Device 1", "device", {{"modelNumber":"Not Mentioned", ""serialNumber":"K112231Q", "dueDate": "Not Mentioned"}}]

    Relationships:
    1: ["Caliper", "was calibrated by", "Calibration Device 1", {{"calibrationDate":"Not Mentioned"}}]

**Output Format Example 3:**
    CREATE (:Device {{name: "Caliper", type: "device", modelNumber: "SERIES 530", serialNumber: "Not Mentioned"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "Not Mentioned"}}]->(:Device {{name: "Calibration Device 1", type: "device", modelNumber:"Not Mentioned", serialNumber: "K112231Q", dueDate: "Not Mentioned"}})

**Example Output Explanation 3:**
    - Nodes Created:
      - Node "Caliper" of type "device".
      - Node "Calibration Device 1" of type "device".

    - Relationship Created:
      - Relationship indicating that "Caliper" was calibrated by "Calibration Device 1".

**Text Information Example 4:**
    **Nodes:**
    1: ["Digital multimeter, 6.5 digit", "device", {{"modelNumber":"34401A", "serialNumber":"MY44007940"}}]
    2: ["Function/Arbitrary Waveform Generator, 80 MHz", "device", {{"modelNumber": "33250A", "serialNumber":"Not Mentioned", "dueDate": "31 Oct 2015"}}]
    3: ["Calibrator", "device", {{"modelNumber": "5720A", "serialNumber":"Not Mentioned", "dueDate": "19 Apr 2015"}}]    
    4: ["Amplifier", "device", {{"modelNumber": "5725A", "serialNumber":"Not Mentioned", "dueDate": "19 Apr 2015"}}]
    
    **Relationships:**
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", "Function/Arbitrary Waveform Generator, 80 MHz", {{"calibrationDate":"13 Mar 2015"}}]
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", " Calibrator", {{"calibrationDate":"13 Mar 2015"}}]
    1: ["Digital multimeter, 6.5 digit", "was calibrated by", "Amplifier", {{"calibrationDate":"13 Mar 2015"}}]  

**Output Format Example 4:**
    CREATE (dmm:Device {{name: "Digital multimeter, 6.5 digit", type: "device", modelNumber: "34401A", serialNumber: "MY44007940"}}), (gen:Device {{name: "Function/Arbitrary Waveform Generator, 80 MHz", type: "device", modelNumber: "33250A", serialNumber: "Not Mentioned", dueDate: "31 Oct 2015"}}), (cal:Device {{name: "Calibrator", type: "device", modelNumber: "5720A", serialNumber: "Not Mentioned", dueDate: "19 Apr 2015"}}), (amp:Device {{name: "Amplifier", type: "device", modelNumber: "5725A", serialNumber: "Not Mentioned", dueDate: "19 Apr 2015"}}), (dmm)-[:WAS_CALIBRATED_BY {{calibrationDate: "13 Mar 2015"}}]->(gen), (dmm)-[:WAS_CALIBRATED_BY {{calibrationDate: "13 Mar 2015"}}]->(cal), (dmm)-[:WAS_CALIBRATED_BY {{calibrationDate: "13 Mar 2015"}}]->(amp)
    
**Example Output Explanation 4:**
    - Nodes Created:
        - Node "Digital Multimeter, 6.5 digit" of type "device".
        - Node "Function/Arbitrary Waveform Generator, 80MHz" of type "device".
        - Node "Calibrator" of type "device".
        - Node "Amplifier" of type "device".
    - Relationships Created:
        - Relationshp Indicating that "Digital Multimeter, 6.5 digit" was calibrated by "Function/Arbitrary Waveform Generator, 80 MHz".
        - Relationshp Indicating that "Digital Multimeter, 6.5 digit" was calibrated by "Calibrator".
        - Relationshp Indicating that "Digital Multimeter, 6.5 digit" was calibrated by "Amplifier".
    - Extra Note:
        - Only one note of "Digital Multimeter" is created. There should be no duplicate nodes in cypher query.

**Text Information Example 5:**
    **Nodes:**
    1: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "device", {{"modelNumber":"MSO70404C", "serialNumber":"C301182"}}]
    2: ["Anonymous Calibration Device 1", "device", {{"modelNumber":"K241C", "serialNumber":"1301244", "dueDate":"December 22nd, 2019"}}]
    3: ["Anonymous Calibration Device 2", "device", {{"modelNumber":"MG3694C", "serialNumber":"152403", "dueDate":"May 15th, 2020"}}]
    4: ["Anonymous Calibration Device 3", "device", {{"modelNumber":"9530", "serialNumber":"43146", "dueDate":"March 26th, 2019"}}]
    5: ["Anonymous Calibration Device 4", "device", {{"modelNumber":"9530", "serialNumber":"43158", "dueDate":"March 26th, 2019"}}]
    6: ["Anonymous Calibration Device 5", "device", {{"modelNumber":"9530", "serialNumber":"43160", "dueDate":"March 26th, 2019"}}]
    
    **Relationships:**
    1: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "was calibrated by", "Anonymous Calibration Device 1", {{"calibrationDate":"November 5th, 2018"}}]
    2: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "was calibrated by", "Anonymous Calibration Device 2", {{"calibrationDate":"November 5th, 2018"}}]
    3: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "was calibrated by", "Anonymous Calibration Device 3", {{"calibrationDate":"November 5th, 2018"}}]
    4: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "was calibrated by", "Anonymous Calibration Device 4", {{"calibrationDate":"November 5th, 2018"}}]
    5: ["4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", "was calibrated by", "Anonymous Calibration Device 5", {{"calibrationDate":"November 5th, 2018"}}]

**Output Format Example 5:**
    CREATE (osc:Device {{name: "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels", type: "device", modelNumber: "MSO70404C", serialNumber: "C301182"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "November 5th, 2018"}}]->(calDevice1:Device {{name: "Anonymous Calibration Device 1", type: "device", modelNumber: "K241C", serialNumber: "1301244", dueDate: "December 22nd, 2019"}}), (osc)-[:WAS_CALIBRATED_BY {{calibrationDate: "November 5th, 2018"}}]->(calDevice2:Device {{name: "Anonymous Calibration Device 2", type: "device", modelNumber: "MG3694C", serialNumber: "152403", dueDate: "May 15th, 2020"}}), (osc)-[:WAS_CALIBRATED_BY {{calibrationDate: "November 5th, 2018"}}]->(calDevice3:Device {{name: "Anonymous Calibration Device 3", type: "device", modelNumber: "9530", serialNumber: "43146", dueDate: "March 26th, 2019"}}), (osc)-[:WAS_CALIBRATED_BY {{calibrationDate: "November 5th, 2018"}}]->(calDevice4:Device {{name: "Anonymous Calibration Device 4", type: "device", modelNumber: "9530", serialNumber: "43158", dueDate: "March 26th, 2019"}}), (osc)-[:WAS_CALIBRATED_BY {{calibrationDate: "November 5th, 2018"}}]->(calDevice5:Device {{name: "Anonymous Calibration Device 5", type: "device", modelNumber: "9530", serialNumber: "43160", dueDate: "March 26th, 2019"}})

**Example Output Explanation 5:**
    - Nodes Created:
        - Node "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" of type "device".
        - Node "Anonymous Calibration Device 1" of type "device".
        - Node "Anonymous Calibration Device 2" of type "device".
        - Node "Anonymous Calibration Device 3" of type "device".
        - Node "Anonymous Calibration Device 4" of type "device".
        - Node "Anonymous Calibration Device 5" of type "device".
    - Relationships Created:
        - Relationshp Indicating that "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" was calibrated by "Anonymous Calibration Device 1".
        - Relationshp Indicating that "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" was calibrated by "Anonymous Calibration Device 2".
        - Relationshp Indicating that "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" was calibrated by "Anonymous Calibration Device 3".
        - Relationshp Indicating that "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" was calibrated by "Anonymous Calibration Device 4".
        - Relationshp Indicating that "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" was calibrated by "Anonymous Calibration Device 5".
    - Extra Note:
        - Only one note of "4 GHz Mixed Signal Oscilloscope; 4 analog / 16 logic channels" is created. There should be no duplicate nodes in cypher query.

**Text Information Example 6:**
    **Nodes:**
    1: ["2.92MM(F) CALIBRATION KIT", "device", {{"modelNumber":"ZV-Z129", "serialNumber":"101243"}}]
    2: ["Digital Multimeter", "device", {{"modelNumber":"UDSS", "serialNumber":"879700/058", "dueDate":"September 30th, 2021"}}]
    3: ["Vector Network Analyzer 4-Port", "device", {{"modelNumber":"ZVA40", "serialNumber":"100380", "dueDate":"August 31st, 2019"}}]
    4: ["Calibration Kit 2.92mm (f)", "device", {{"modelNumber":"ZV-Z129", "serialNumber":"101108", "dueDate":"July 31st, 2019"}}]
    5: ["Calibration Kit 2.92mm", "device", {{"modelNumber":"ZV-Z129", "serialNumber":"101108", "dueDate":"July 31st, 2019"}}]
    
    **Relationships:**
    1: ["2.92MM(F) CALIBRATION KIT", "was calibrated by", "Digital Multimeter", {{"calibrationDate":"January 31st, 2019"}}]
    2: ["2.92MM(F) CALIBRATION KIT", "was calibrated by", "Vector Network Analyzer 4-Port", {{"calibrationDate":"January 31st, 2019"}}]
    3: ["2.92MM(F) CALIBRATION KIT", "was calibrated by", "Calibration Kit 2.92mm (f)", {{"calibrationDate":"January 31st, 2019"}}]
    4: ["2.92MM(F) CALIBRATION KIT", "was calibrated by", "Calibration Kit 2.92mm", {{"calibrationDate":"January 31st, 2019"}}]

**Output Format Example 6:**
    CREATE (calibrationKit:Device {{name: "2.92MM(F) CALIBRATION KIT", type: "device", modelNumber: "ZV-Z129", serialNumber: "101243"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "January 31st, 2019"}}]->(:Device {{name: "Digital Multimeter", type: "device", modelNumber: "UDSS", serialNumber: "879700/058", dueDate: "September 30th, 2021"}}), (calibrationKit)-[:WAS_CALIBRATED_BY {{calibrationDate: "January 31st, 2019"}}]->(:Device {{name: "Vector Network Analyzer 4-Port", type: "device", modelNumber: "ZVA40", serialNumber: "100380", dueDate: "August 31st, 2019"}}), (calibrationKit)-[:WAS_CALIBRATED_BY {{calibrationDate: "January 31st, 2019"}}]->(:Device {{name: "Calibration Kit 2.92mm (f)", type: "device", modelNumber: "ZV-Z129", serialNumber: "101108", dueDate: "July 31st, 2019"}}), (calibrationKit)-[:WAS_CALIBRATED_BY {{calibrationDate: "January 31st, 2019"}}]->(:Device {{name: "Calibration Kit 2.92mm", type: "device", modelNumber: "ZV-Z129", serialNumber: "101108", dueDate: "July 31st, 2019"}})

**Example Output Explanation 6:**
    - Nodes Created:
        - Node "2.92MM(F) CALIBRATION KIT" of type "device".
        - Node "Digital Multimeter" of type "device".
        - Node "Vector Network Analyzer 4-Port" of type "device".
        - Node "Calibration Kit 2.92mm (f)" of type "device".
        - Node "Calibration Kit 2.92mm" of type "device".

    - Relationships Created:
        - Relationshp Indicating that "2.92MM(F) CALIBRATION KIT" was calibrated by "Digital Multimeter".
        - Relationshp Indicating that "2.92MM(F) CALIBRATION KIT" was calibrated by "Vector Network Analyzer 4-Port".
        - Relationshp Indicating that "2.92MM(F) CALIBRATION KIT" was calibrated by "Calibration Kit 2.92mm (f)".
        - Relationshp Indicating that "2.92MM(F) CALIBRATION KIT" was calibrated by "Calibration Kit 2.92mm"".   

    - Extra Note:
        - Only one note of "2.92MM(F) CALIBRATION KIT" is created. There should be no duplicate nodes in cypher query.

**Text Information Example 7:**
    **Nodes:**
    1: ["Power Supply", "device", {{"modelNumber":"PSU-100", "serialNumber":"ABC123"}}]
    2: ["Voltage Meter", "device", {{"modelNumber":"VM-200", "serialNumber":"XYZ789"}}]
    3: ["Signal Generator", "device", {{"modelNumber":"SG-300", "serialNumber":"DEF456"}}]
    4: ["Frequency Counter", "device", {{"modelNumber":"FC-400", "serialNumber":"GHI789"}}]
    5: ["Current Probe", "device", {{"modelNumber":"CP-500", "serialNumber":"JKL012"}}]

    **Relationships:**
    1: ["Power Supply", "was calibrated by", "Voltage Meter", {{"calibrationDate":"April 10th, 2023"}}]
    2: ["Power Supply", "was calibrated by", "Signal Generator", {{"calibrationDate":"April 10th, 2023"}}]
    3: ["Power Supply", "was calibrated by", "Frequency Counter", {{"calibrationDate":"April 10th, 2023"}}]
    4: ["Power Supply", "was calibrated by", "Current Probe", {{"calibrationDate":"April 10th, 2023"}}]

**Output Format Example 7:**
    CREATE (ps:Device {{name: "Power Supply", type: "device", modelNumber: "PSU-100", serialNumber: "ABC123"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "April 10th, 2023"}}]->(:Device {{name: "Voltage Meter", type: "device", modelNumber: "VM-200", serialNumber: "XYZ789"}}), (ps)-[:WAS_CALIBRATED_BY {{calibrationDate: "April 10th, 2023"}}]->(:Device {{name: "Signal Generator", type: "device", modelNumber: "SG-300", serialNumber: "DEF456"}}), (ps)-[:WAS_CALIBRATED_BY {{calibrationDate: "April 10th, 2023"}}]->(:Device {{name: "Frequency Counter", type: "device", modelNumber: "FC-400", serialNumber: "GHI789"}}), (ps)-[:WAS_CALIBRATED_BY {{calibrationDate: "April 10th, 2023"}}]->(:Device {{name: "Current Probe", type: "device", modelNumber: "CP-500", serialNumber: "JKL012"}})

**Example Output Explanation 7:**
    - Nodes Created:
        - Node "Power Supply" of type "device".
        - Node "Voltage Meter" of type "device".
        - Node "Signal Generator" of type "device".
        - Node "Frequency Counter" of type "device".
        - Node "Current Probe" of type "device".
    - Relationships Created:
    - Relationshp Indicating that "Power Supply" was calibrated by "Voltage Meter".
    - Relationshp Indicating that "Power Supply" was calibrated by "Signal Generator".
    - Relationshp Indicating that "Power Supply" was calibrated by "Frequency Counter".
    - Relationshp Indicating that "Power Supply" was calibrated by "Current Probe".

**Text Information Example 8:**
    **Nodes:**
    1: ["Temperature Controller", "device", {{"modelNumber":"TC-1000", "serialNumber":"TEMP123"}}]
    2: ["Thermocouple", "device", {{"modelNumber":"THC-200", "serialNumber":"TC123"}}]
    3: ["Heat Gun", "device", {{"modelNumber":"HG-300", "serialNumber":"HG123"}}]
    4: ["Data Logger", "device", {{"modelNumber":"DL-400", "serialNumber":"DL123"}}]

    **Relationships:**
    1: ["Temperature Controller", "was calibrated by", "Thermocouple", {{"calibrationDate":"May 5th, 2023"}}]
    2: ["Temperature Controller", "was calibrated by", "Heat Gun", {{"calibrationDate":"May 5th, 2023"}}]
    3: ["Temperature Controller", "was calibrated by", "Data Logger", {{"calibrationDate":"May 5th, 2023"}}]

**Output Format Example 8:**
    CREATE (tc:Device {{name: "Temperature Controller", type: "device", modelNumber: "TC-1000", serialNumber: "TEMP123"}})-[:WAS_CALIBRATED_BY {{calibrationDate: "May 5th, 2023"}}]->(:Device {{name: "Thermocouple", type: "device", modelNumber: "THC-200", serialNumber: "TC123"}}), (tc)-[:WAS_CALIBRATED_BY {{calibrationDate: "May 5th, 2023"}}]->(:Device {{name: "Heat Gun", type: "device", modelNumber: "HG-300", serialNumber: "HG123"}}), (tc)-[:WAS_CALIBRATED_BY {{calibrationDate: "May 5th, 2023"}}]->(:Device {{name: "Data Logger", type: "device", modelNumber: "DL-400", serialNumber: "DL123"}})    

**Example Output Explanation 8:**
    - Nodes Created:
        - Node "Temperature Controller" of type "device".
        - Node "Thermocouple" of type "device".
        - Node "Heat Gun" of type "device".
        - Node "Data Logger" of type "device".
        
    - Relationships Created:
        - Relationship indicating that "Temperature Controller" was calibrated by "Thermocouple".
        - Relationship indicating that "Temperature Controller" was calibrated by "Heat Gun".
        - Relationship indicating that "Temperature Controller" was calibrated by "Data Logger".
        
"""

contextualized_query_forward = """
MATCH (node:Device)-[calibrated:WAS_CALIBRATED_BY]->(sc:Device)
WITH node, collect(DISTINCT {device: sc, date: calibrated.calibrationDate}) AS calibrations, score, {} AS metadata
RETURN '---Below give information about the instrument that was calibrated---\n' +
       'Name of Instrument Calibrated: ' + node.name + '\n' +
       'Instrument Model Number: ' + node.modelNumber + '\n' +
       'Instrument Serial Number: ' + node.serialNumber + '\n\n' +
       REDUCE(s = '', idx in RANGE(0, SIZE(calibrations) - 1) |
           s + '---Below show information about a calibration device used to calibrate the above instrument ' + '---' +
           '\n' + 'Calibration Device Name: ' + calibrations[idx].device.name + '\n' +
           'Calibration Device Serial Number: ' + calibrations[idx].device.serialNumber + '\n' +
           'Calibration Device Type: ' + calibrations[idx].device.type + '\n' +
           'Calibration Device Due Date: ' + calibrations[idx].device.dueDate + '\n' +
           'Calibration Date: ' + calibrations[idx].date + '\n' +'\n'
       ) AS text,
       score,
       metadata
LIMIT 1
"""

contextualized_query_backward = """
MATCH (node:Device)<-[calibrated:WAS_CALIBRATED_BY]-(sc:Device)-[calibrated1:WAS_CALIBRATED_BY]->(sc1:Device)
WITH node, sc, calibrated, collect(DISTINCT {device: sc1, date: calibrated1.calibrationDate}) AS calibrations, score, {} AS metadata
RETURN '---Below give information about the instrument that was calibrated---\n' +
       'Name of Instrument Calibrated: ' + sc.name + '\n' +
       'Instrument Model Number: ' + sc.modelNumber + '\n' +
       'Instrument Serial Number: ' + sc.serialNumber + '\n\n' +
       '---Below show information about a calibration device used to calibrate the above instrument ' + '---' +
       '\n' + 'Calibration Device Name: ' + node.name + '\n' +
       'Calibration Device Serial Number: ' + node.serialNumber + '\n' +
       'Calibration Device Type: ' + node.type + '\n' +
       'Calibration Device Due Date: ' + node.dueDate + '\n' +
       'Calibration Date: ' + calibrated.calibrationDate + '\n' + '\n' +
       REDUCE(s = '', idx in RANGE(0, SIZE(calibrations) - 1) |
           s + '---Below show information about a calibration device used to calibrate the above instrument ' + '---' +
           '\n' + 'Calibration Device Name: ' + calibrations[idx].device.name + '\n' +
           'Calibration Device Serial Number: ' + calibrations[idx].device.serialNumber + '\n' +
           'Calibration Device Type: ' + calibrations[idx].device.type + '\n' +
           'Calibration Device Due Date: ' + calibrations[idx].device.dueDate + '\n' +
           'Calibration Date: ' + calibrations[idx].date + '\n' +'\n'
       ) AS text,
       score,
       metadata
LIMIT 1
"""

system_basic_check_prompt = """
**Task:** Your task is to analyze the given information about calibration and generate a response to indicate whether the calibration certificate passes basic checks.

**Instructions**
    1. When evaluating the calibration certificate, consider only the calibration due date and the date of calibration.
    2. If the due date of the calibration device is on or after the calibration date, the calibration certificate passes all basic checks.
    3. If the due date of the calibration device is before the calibration date, the calibration certificate fails the basic checks.
    4. If basic checks pass, just respond with 'The calibration certificate has passed all basic checks'.

**Text Information Example 1**

print(key_components)
    **Information of Instrument Calibrated**
    - Instrument Calibrated: RF Power Meter
    - Model: 4220A
    - Serial Number: 303603AA
    - Date of Calibration: April 6th, 2018
    
    **Information of Calibration Device 1**
    - Calibration Device: SYNTHESIZED SIGNAL GENERATOR
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 3417A02046
    - Due Date of Calibration Device: December 8th, 2018
    
    **Information of Calibration Device 2**
    - Calibration Device: FREQUENCY COUNTER
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 7991
    - Due Date of Calibration Device: December 8th, 2018
    
    **Information of Calibration Device 3**
    - Calibration Device: POWER METER
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 3125U05443
    - Due Date of Calibration Device: May 16th, 2018
    
    **Information of Calibration Device 4**
    - Calibration Device: STEP ATTENUATOR / 110dB (OPT H18)
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 2827A18296
    - Due Date of Calibration Device: April 28th, 2018
    
    **Information of Calibration Device 5**
    - Calibration Device: POWER SENSOR
    - Model Number of Calibration Device: Not Mentioned
    - Serial Number of Calibration Device: 2652A21894
    - Due Date of Calibration Device: May 17th, 2018


**Output Example 1**
    The calibration certificate has passed all the basic checks.

**Example Output Explanation 1:**
    The calibration device due date for each calibration device is after the calibration date which is April 6th, 2018. Therefor the calibration certificate has passes all the basic checks.
    
**Text Information Example 2**
    **Information of Instrument Calibrated**
    Instrument Calibrated: Multimeter 
    Model: GCCBA
    Serial Number: P12345L
    Date of Calibration: May 22nd, 2023
    
    **Information of Calibration Device 1**
    Calibration Device: Sensor 
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: T342221
    Calibration Device Due Date: February 11th, 2023

    **Information of Calibration Device 2**
    Calibration Device: FREQUENCY COUNTER
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: 7991
    Calibration Device Due Date: December 8th, 2023
    
**Output Example 2**
    The calibration certificate failed to meet all the basic criteria. The calibration device due date for the Sensor which is Feb 11th, 2023 is after the date of calibration which is May 22nd, 2023.

**Example Output Explanation 2:**
    For one of the calibration device, the calibration date is after the calibration device due date; therefore, the calibration certificate did not pass all the basic checks.
    
**Text Information Example 3**
    **Information of Instrument Calibrated**
    Instrument Calibrated: Multimeter 
    Model: GCCBA
    Serial Number: P12345L
    Date of Calibration: February 10th, 2023
    
    **Information of Calibration Device 1**
    Calibration Device: Sensor 
    Model Number of Calibration Device: Not Mentioned
    Serial Number of Calibration Device: T342221
    Calibration Device Due Date: Not Mentioned

**Output Example 3**
    The calibration certificate did not pass all the basic checks. The calibration date is February 10th, 2023, but the due date of the calibration device is not mentioned.

**Example Output Explanation 3**
    The calibration device due date is not mentioned, so it can't be determined whether it falls before or after the calibration date; therefore, the calibration certificate did not pass all the basic checks.

"""

convo_prompt_template = """
** Task: Your task is to answer the user query to the best of your ability**
** Notes ** 
The meaning of instrument is the same meaning as device in this context

Context: {context}

Question: {question}


Answer:
"""
