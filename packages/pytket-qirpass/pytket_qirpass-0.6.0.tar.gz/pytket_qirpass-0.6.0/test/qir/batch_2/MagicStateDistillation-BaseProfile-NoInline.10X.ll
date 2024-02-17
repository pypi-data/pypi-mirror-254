; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque
%String = type opaque

@PauliZ = internal constant i2 -2
@PauliX = internal constant i2 1
@PauliY = internal constant i2 -1
@0 = internal constant [18 x i8] c"Unsupported input\00"
@1 = internal constant [3 x i8] c"()\00"

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth10InX__Interop() #0 {
entry:
  call void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth10InX__body()
  ret void
}

define internal void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth10InX__body() {
entry:
  %q = call %Qubit* @__quantum__rt__qubit_allocate()
  call void @Microsoft__Quantum__Samples__PrepareDistilledT__body(i64 10, %Qubit* %q)
  %0 = call %Result* @Microsoft__Quantum__Measurement__MResetX__body(%Qubit* %q)
  call void @__quantum__rt__result_update_reference_count(%Result* %0, i32 -1)
  call void @__quantum__rt__qubit_release(%Qubit* %q)
  ret void
}

declare %Qubit* @__quantum__rt__qubit_allocate()

define internal void @Microsoft__Quantum__Samples__PrepareDistilledT__body(i64 %maxDepth, %Qubit* %target) {
entry:
  %aux1 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux2 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux3 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux4 = call %Qubit* @__quantum__rt__qubit_allocate()
  call void @Microsoft__Quantum__Samples__Distill__body(i64 %maxDepth, %Qubit* %target, %Qubit* %aux1, %Qubit* %aux2, %Qubit* %aux3, %Qubit* %aux4)
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %target)
  call void @Microsoft__Quantum__Intrinsic__Y__body(%Qubit* %target)
  call void @__quantum__rt__qubit_release(%Qubit* %aux1)
  call void @__quantum__rt__qubit_release(%Qubit* %aux2)
  call void @__quantum__rt__qubit_release(%Qubit* %aux3)
  call void @__quantum__rt__qubit_release(%Qubit* %aux4)
  ret void
}

define internal %Result* @Microsoft__Quantum__Measurement__MResetX__body(%Qubit* %target) {
entry:
  %0 = load i2, i2* @PauliZ, align 1
  %1 = load i2, i2* @PauliX, align 1
  call void @Microsoft__Quantum__Intrinsic____QsRef23__MapPauli____body(%Qubit* %target, i2 %0, i2 %1)
  %result = call %Result* @__quantum__qis__m__body(%Qubit* %target)
  call void @__quantum__qis__reset__body(%Qubit* %target)
  ret %Result* %result
}

declare void @__quantum__rt__result_update_reference_count(%Result*, i32)

declare void @__quantum__rt__qubit_release(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic____QsRef23__MapPauli____body(%Qubit* %qubit, i2 %from, i2 %to) {
entry:
  %0 = icmp eq i2 %from, %to
  br i1 %0, label %then0__1, label %test1__1

then0__1:                                         ; preds = %entry
  br label %continue__1

test1__1:                                         ; preds = %entry
  %1 = load i2, i2* @PauliZ, align 1
  %2 = icmp eq i2 %from, %1
  br i1 %2, label %condTrue__1, label %condContinue__1

condTrue__1:                                      ; preds = %test1__1
  %3 = load i2, i2* @PauliX, align 1
  %4 = icmp eq i2 %to, %3
  br label %condContinue__1

condContinue__1:                                  ; preds = %condTrue__1, %test1__1
  %5 = phi i1 [ %4, %condTrue__1 ], [ %2, %test1__1 ]
  %6 = xor i1 %5, true
  br i1 %6, label %condTrue__2, label %condContinue__2

condTrue__2:                                      ; preds = %condContinue__1
  %7 = load i2, i2* @PauliX, align 1
  %8 = icmp eq i2 %from, %7
  br i1 %8, label %condTrue__3, label %condContinue__3

condTrue__3:                                      ; preds = %condTrue__2
  %9 = load i2, i2* @PauliZ, align 1
  %10 = icmp eq i2 %to, %9
  br label %condContinue__3

condContinue__3:                                  ; preds = %condTrue__3, %condTrue__2
  %11 = phi i1 [ %10, %condTrue__3 ], [ %8, %condTrue__2 ]
  br label %condContinue__2

condContinue__2:                                  ; preds = %condContinue__3, %condContinue__1
  %12 = phi i1 [ %11, %condContinue__3 ], [ %5, %condContinue__1 ]
  br i1 %12, label %then1__1, label %test2__1

then1__1:                                         ; preds = %condContinue__2
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  br label %continue__1

test2__1:                                         ; preds = %condContinue__2
  %13 = load i2, i2* @PauliZ, align 1
  %14 = icmp eq i2 %from, %13
  br i1 %14, label %condTrue__4, label %condContinue__4

condTrue__4:                                      ; preds = %test2__1
  %15 = load i2, i2* @PauliY, align 1
  %16 = icmp eq i2 %to, %15
  br label %condContinue__4

condContinue__4:                                  ; preds = %condTrue__4, %test2__1
  %17 = phi i1 [ %16, %condTrue__4 ], [ %14, %test2__1 ]
  br i1 %17, label %then2__1, label %test3__1

then2__1:                                         ; preds = %condContinue__4
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  call void @Microsoft__Quantum__Intrinsic__S__body(%Qubit* %qubit)
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  br label %continue__1

test3__1:                                         ; preds = %condContinue__4
  %18 = load i2, i2* @PauliY, align 1
  %19 = icmp eq i2 %from, %18
  br i1 %19, label %condTrue__5, label %condContinue__5

condTrue__5:                                      ; preds = %test3__1
  %20 = load i2, i2* @PauliZ, align 1
  %21 = icmp eq i2 %to, %20
  br label %condContinue__5

condContinue__5:                                  ; preds = %condTrue__5, %test3__1
  %22 = phi i1 [ %21, %condTrue__5 ], [ %19, %test3__1 ]
  br i1 %22, label %then3__1, label %test4__1

then3__1:                                         ; preds = %condContinue__5
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  call void @Microsoft__Quantum__Intrinsic__S__adj(%Qubit* %qubit)
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  br label %continue__1

test4__1:                                         ; preds = %condContinue__5
  %23 = load i2, i2* @PauliY, align 1
  %24 = icmp eq i2 %from, %23
  br i1 %24, label %condTrue__6, label %condContinue__6

condTrue__6:                                      ; preds = %test4__1
  %25 = load i2, i2* @PauliX, align 1
  %26 = icmp eq i2 %to, %25
  br label %condContinue__6

condContinue__6:                                  ; preds = %condTrue__6, %test4__1
  %27 = phi i1 [ %26, %condTrue__6 ], [ %24, %test4__1 ]
  br i1 %27, label %then4__1, label %test5__1

then4__1:                                         ; preds = %condContinue__6
  call void @Microsoft__Quantum__Intrinsic__S__body(%Qubit* %qubit)
  br label %continue__1

test5__1:                                         ; preds = %condContinue__6
  %28 = load i2, i2* @PauliX, align 1
  %29 = icmp eq i2 %from, %28
  br i1 %29, label %condTrue__7, label %condContinue__7

condTrue__7:                                      ; preds = %test5__1
  %30 = load i2, i2* @PauliY, align 1
  %31 = icmp eq i2 %to, %30
  br label %condContinue__7

condContinue__7:                                  ; preds = %condTrue__7, %test5__1
  %32 = phi i1 [ %31, %condTrue__7 ], [ %29, %test5__1 ]
  br i1 %32, label %then5__1, label %else__1

then5__1:                                         ; preds = %condContinue__7
  call void @Microsoft__Quantum__Intrinsic__S__adj(%Qubit* %qubit)
  br label %continue__1

else__1:                                          ; preds = %condContinue__7
  %33 = call %String* @__quantum__rt__string_create(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__fail(%String* %33)
  unreachable

continue__1:                                      ; preds = %then5__1, %then4__1, %then3__1, %then2__1, %then1__1, %then0__1
  ret void
}

declare %Result* @__quantum__qis__m__body(%Qubit*)

declare void @__quantum__qis__reset__body(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__h__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__S__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__s__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__S__adj(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__s__adj(%Qubit* %qubit)
  ret void
}

declare %String* @__quantum__rt__string_create(i8*)

declare void @__quantum__rt__fail(%String*)

declare void @__quantum__qis__s__adj(%Qubit*)

declare void @__quantum__qis__s__body(%Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

define internal void @Microsoft__Quantum__Samples__Distill__body(i64 %maxNIterations, %Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4) {
entry:
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q0)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q1)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q2)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q3)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q4)
  call void @Microsoft__Quantum__Samples__Encode__adj(%Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4)
  %s0 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q1)
  %s1 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q2)
  %s2 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q3)
  %s3 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q4)
  %0 = icmp sgt i64 %maxNIterations, 1
  br i1 %0, label %then0__1, label %continue__1

then0__1:                                         ; preds = %entry
  %1 = call i1 @__quantum__qis__anynonzero__body(%Result* %s0, %Result* %s1, %Result* %s2, %Result* %s3)
  br i1 %1, label %then0__2, label %continue__2

then0__2:                                         ; preds = %then0__1
  call void @__quantum__qis__reset__body(%Qubit* %q0)
  %2 = sub i64 %maxNIterations, 1
  call void @Microsoft__Quantum__Samples__Distill__body(i64 %2, %Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4)
  call void @__quantum__rt__result_update_reference_count(%Result* %s0, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s1, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s2, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s3, i32 -1)
  ret void

continue__2:                                      ; preds = %then0__1
  br label %continue__1

continue__1:                                      ; preds = %continue__2, %entry
  call void @__quantum__rt__result_update_reference_count(%Result* %s0, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s1, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s2, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s3, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Y__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__y__body(%Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__y__body(%Qubit*)

define internal void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %target) {
entry:
  call void @Microsoft__Quantum__Intrinsic__Ry__body(double 0x3FEE91F42805715E, %Qubit* %target)
  call void @Microsoft__Quantum__Intrinsic__Rz__body(double 0xC015FDBBE9BBA775, %Qubit* %target)
  ret void
}

define internal void @Microsoft__Quantum__Samples__Encode__adj(%Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4) {
entry:
  call void @Microsoft__Quantum__Intrinsic__Y__adj(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__Z__adj(%Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__SWAP__adj(%Qubit* %q3, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q2, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q0)
  ret void
}

define internal %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %target) {
entry:
  %result = call %Result* @__quantum__qis__m__body(%Qubit* %target)
  call void @__quantum__qis__reset__body(%Qubit* %target)
  ret %Result* %result
}

declare i1 @__quantum__qis__anynonzero__body(%Result*, %Result*, %Result*, %Result*)

define internal void @Microsoft__Quantum__Intrinsic__Y__adj(%Qubit* %qubit) {
entry:
  call void @Microsoft__Quantum__Intrinsic__Y__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Z__adj(%Qubit* %qubit) {
entry:
  call void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %qubit) {
entry:
  call void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %control, %Qubit* %target) {
entry:
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control, %Qubit* %target)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %qubit) {
entry:
  call void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__SWAP__adj(%Qubit* %qubit1, %Qubit* %qubit2) {
entry:
  call void @Microsoft__Quantum__Intrinsic__SWAP__body(%Qubit* %qubit1, %Qubit* %qubit2)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__SWAP__body(%Qubit* %qubit1, %Qubit* %qubit2) {
entry:
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %qubit1, %Qubit* %qubit2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %qubit2, %Qubit* %qubit1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %qubit1, %Qubit* %qubit2)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control, %Qubit* %target) {
entry:
  call void @__quantum__qis__cnot__body(%Qubit* %control, %Qubit* %target)
  ret void
}

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__x__body(%Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__x__body(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__z__body(%Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__z__body(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__Ry__body(double %theta, %Qubit* %qubit) {
entry:
  call void @__quantum__qis__ry__body(double %theta, %Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Rz__body(double %theta, %Qubit* %qubit) {
entry:
  call void @__quantum__qis__rz__body(double %theta, %Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__rz__body(double, %Qubit*)

declare void @__quantum__qis__ry__body(double, %Qubit*)

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth10InX() #1 {
entry:
  call void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth10InX__body()
  %0 = call %String* @__quantum__rt__string_create(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__message(%String* %0)
  call void @__quantum__rt__string_update_reference_count(%String* %0, i32 -1)
  ret void
}

declare void @__quantum__rt__message(%String*)

declare void @__quantum__rt__string_update_reference_count(%String*, i32)

attributes #0 = { "InteropFriendly" }
attributes #1 = { "EntryPoint" }

